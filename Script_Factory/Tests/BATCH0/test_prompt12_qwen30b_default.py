import json
import os
import tempfile
import pytest
import sys, os
from datetime import datetime
from unittest.mock import patch, mock_open

# Import the functions to test


from Script_Factory.Script_Factory_Runs.all_runs.prompt12_qwen30b_default import (
    add_task,
    automatic_deletion_worker,
    delete_random_task,
    list_tasks,
    load_tasks,
    main,
    save_tasks
)


def test_load_tasks_file_exists_and_valid():
    """Test loading tasks when the file exists and contains valid JSON."""
    # Create a temporary JSON file with sample data
    sample_tasks = [
        {"id": 1, "description": "Test task 1", "timestamp": "2023-01-01T00:00:00"},
        {"id": 2, "description": "Test task 2", "timestamp": "2023-01-02T00:00:00"}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(sample_tasks, f)
        temp_file = f.name
    
    # Mock the TASKS_FILE to point to our temporary file
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        result = load_tasks()
        
        assert result == sample_tasks
        os.unlink(temp_file)

def test_load_tasks_file_does_not_exist():
    """Test loading tasks when the file doesn't exist."""
    # Create a temporary file name that doesn't exist
    temp_file = "nonexistent_file.json"
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        # Mock os.path.exists to return False
        with patch('os.path.exists', return_value=False):
            result = load_tasks()
            
            assert result == []
            # Check that save_tasks was called to create the file
            # This requires mocking the save_tasks function or checking file creation

def test_load_tasks_invalid_json():
    """Test loading tasks when the file exists but contains invalid JSON."""
    # Create a temporary file with invalid JSON content
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write("invalid json content")
        temp_file = f.name
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        # Mock print to capture output
        with patch('builtins.print') as mock_print:
            result = load_tasks()
            
            assert result == []
            # Verify that an error was printed
            mock_print.assert_called()

def test_save_tasks_normal_case():
    """Test saving tasks to a JSON file."""
    sample_tasks = [
        {"id": 1, "description": "Test task 1", "timestamp": "2023-01-01T00:00:00"},
        {"id": 2, "description": "Test task 2", "timestamp": "2023-01-02T00:00:00"}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        save_tasks(sample_tasks)
        
        # Read the file back to verify content
        with open(temp_file, 'r') as f:
            saved_content = json.load(f)
            
        assert saved_content == sample_tasks
        os.unlink(temp_file)

def test_save_tasks_io_error():
    """Test saving tasks when an IOError occurs."""
    sample_tasks = [
        {"id": 1, "description": "Test task 1", "timestamp": "2023-01-01T00:00:00"}
    ]
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', 'nonexistent_dir/nonexistent_file.json'):
        with patch('builtins.print') as mock_print:
            save_tasks(sample_tasks)
            
            # Verify that an error was printed
            mock_print.assert_called()

def test_add_task_normal_case():
    """Test adding a new task to the list."""
    sample_tasks = [
        {"id": 1, "description": "Existing task", "timestamp": "2023-01-01T00:00:00"}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(sample_tasks, f)
        temp_file = f.name
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        with patch('builtins.print') as mock_print:
            add_task("New task")
            
            # Read the file back to verify content
            with open(temp_file, 'r') as f:
                saved_content = json.load(f)
            
            assert len(saved_content) == 2
            assert saved_content[1]['description'] == "New task"
            assert 'timestamp' in saved_content[1]
            mock_print.assert_called()

def test_add_task_empty_description():
    """Test adding a task with empty description."""
    # This should not add anything to the tasks list
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump([], f)
        temp_file = f.name
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        with patch('builtins.print') as mock_print:
            add_task("")
            
            # Read the file back to verify content
            with open(temp_file, 'r') as f:
                saved_content = json.load(f)
            
            assert saved_content == []
            mock_print.assert_called()

def test_list_tasks_empty():
    """Test listing tasks when there are no tasks."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump([], f)
        temp_file = f.name
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        with patch('builtins.print') as mock_print:
            list_tasks()
            
            mock_print.assert_called_with("No tasks in the list.")

def test_list_tasks_with_tasks():
    """Test listing tasks when there are tasks."""
    sample_tasks = [
        {"id": 1, "description": "Task 1", "timestamp": "2023-01-01T00:00:00"},
        {"id": 2, "description": "Task 2", "timestamp": "2023-01-02T00:00:00"}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(sample_tasks, f)
        temp_file = f.name
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        with patch('builtins.print') as mock_print:
            list_tasks()
            
            # Verify that print was called multiple times
            assert mock_print.call_count >= 2

def test_delete_random_task_empty_list():
    """Test deleting a random task when the list is empty."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump([], f)
        temp_file = f.name
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        with patch('builtins.print') as mock_print:
            delete_random_task()
            
            # Should print "No tasks to delete"
            mock_print.assert_called_with("No tasks to delete - list is empty.")

def test_delete_random_task_normal_case():
    """Test deleting a random task when there are tasks."""
    sample_tasks = [
        {"id": 1, "description": "Task 1", "timestamp": "2023-01-01T00:00:00"},
        {"id": 2, "description": "Task 2", "timestamp": "2023-01-02T00:00:00"},
        {"id": 3, "description": "Task 3", "timestamp": "2023-01-03T00:00:00"}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(sample_tasks, f)
        temp_file = f.name
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        # Mock random.randint to return a specific index for predictable testing
        with patch('random.randint', return_value=1):  # Delete second task
            with patch('builtins.print') as mock_print:
                delete_random_task()
                
                # Read the file back to verify content
                with open(temp_file, 'r') as f:
                    saved_content = json.load(f)
                
                # Should have one less task
                assert len(saved_content) == 2
                # Should not contain the deleted task (Task 2)
                descriptions = [task['description'] for task in saved_content]
                assert "Task 2" not in descriptions
                mock_print.assert_called()

def test_delete_random_task_single_task():
    """Test deleting a random task when there is only one task."""
    sample_tasks = [
        {"id": 1, "description": "Only task", "timestamp": "2023-01-01T00:00:00"}
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(sample_tasks, f)
        temp_file = f.name
    
    with patch('Script_Factory.Script_Factory_runs.all_runs.recipe.TASKS_FILE', temp_file):
        with patch('random.randint', return_value=0):  # Delete first (and only) task
            with patch('builtins.print') as mock_print:
                delete_random_task()
                
                # Read the file back to verify content
                with open(temp_file, 'r') as f:
                    saved_content = json.load(f)
                
                # Should be empty now
                assert saved_content == []
                mock_print.assert_called()
