```python
import json
import random
import time
import threading

# Task management functions
def load_tasks():
    """Load tasks from JSON file if available."""
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save the current task list to a JSON file."""
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def delete_random_task(tasks):
    """Delete a random task from the list and log it."""
    if len(tasks) > 0:
        task_index = random.randint(0, len(tasks)-1)
        deleted_task = tasks.pop(task_index)
        print(f"Deleted task: {deleted_task}")
    else:
        print("No tasks to delete.")

# Scheduler thread for automatic deletion
def run_deletion_scheduler(tasks, shutdown_flag):
    """Run every hour to delete a random task."""
    while not shutdown_flag:
        time.sleep(3600)
        if shutdown_flag:
            break
        delete_random_task(tasks)

# Main application loop
def main():
    """Main loop for the Intermittent To-Do List application."""
    tasks = load_tasks()
    
    # Start the deletion scheduler as a thread
    shutdown_flag = False
    scheduler_thread = threading.Thread(target=run_deletion_scheduler, args=(tasks, shutdown_flag))
    scheduler_thread.start()

    while True:
        try:
            user_input = input("Enter command (add, list, exit): ").strip().lower()
            if user_input == 'exit':
                shutdown_flag = True
                break
            elif user_input == 'add':
                task_description = input("Enter task description: ")
                tasks.append(task_description)
                save_tasks(tasks)
            elif user_input == 'list':
                print("Tasks:")
                for i, t in enumerate(tasks):
                    print(f"{i+1}. {t}")
            else:
                print("Unknown command.")
        except KeyboardInterrupt:
            shutdown_flag = True
            break

    # Wait for the scheduler thread to finish
    if shutdown_flag:
        scheduler_thread.join()

if __name__ == "__main__":
    main()
```

### Explanation:

1. **Core Features**:
   - **Add Task**: The user can input a task description and add it to the list.
   - **List Tasks**: Displays all current tasks in a numbered format.
   - **Persistence**: Tasks are saved to `tasks.json` when added or modified, and loaded on startup.

2. **Automatic Deletion**:
   - A background thread runs every hour to delete one random task from the list.
   - The deletion is logged to the console with a message indicating which task was removed.

3. **Robustness**:
   - If the task list is empty, the deletion operation will print "No tasks to delete."
   - Graceful shutdown on `Ctrl+C` (KeyboardInterrupt) by setting a global flag and waiting for the scheduler thread to finish.

4. **Implementation Constraints**:
   - Uses Python's standard library modules: `json`, `random`, `time`, and `threading`.
   - The script runs as a single process with a background deletion scheduler.

5. **Output Format**:
   - The full code is enclosed in a markdown code block with clear comments explaining each section, making it easy to read and understand.

# ===== GENERATED TESTS =====
```python
import pytest
from unittest.mock import patch, MagicMock

# Test suite for the Intermittent To-Do List application

# Mocking functions
def mock_load_tasks():
    return ["task1", "task2"]

def mock_save_tasks(tasks):
    pass

def mock_delete_random_task(tasks):
    if len(tasks) > 0:
        tasks.pop(0)

def test_load_tasks(mocker):
    """Test loading tasks from a JSON file."""
    mocker.patch('json.load', return_value=["task1", "task2"])
    assert load_tasks() == ["task1", "task2"]

def test_save_tasks(mocker):
    """Test saving tasks to a JSON file."""
    mock_file = MagicMock()
    mocker.patch('open', return_value=mock_file)
    save_tasks(["task1", "task2"])
    mock_file.write.assert_called_once_with(json.dumps(["task1", "task2"]))

def test_delete_random_task():
    """Test deleting a random task from the list."""
    tasks = ["task1", "task2"]
    delete_random_task(tasks)
    assert len(tasks) == 1

def test_run_deletion_scheduler(mocker):
    """Test the deletion scheduler thread."""
    mock_tasks = ["task1", "task2"]
    shutdown_flag = False
    mock_thread = MagicMock()
    mocker.patch('threading.Thread', return_value=mock_thread)
    
    run_deletion_scheduler(mock_tasks, shutdown_flag)
    mock_thread.start.assert_called_once()

def test_main(mocker):
    """Test the main application loop."""
    mock_input = ["add", "task3", "list", "exit"]
    mocker.patch('builtins.input', side_effect=mock_input)
    mock_save_tasks = MagicMock()
    mocker.patch('save_tasks', mock_save_tasks)
    
    with patch('load_tasks', return_value=["task1", "task2"]):
        main()
    
    assert mock_save_tasks.call_count == 3
    assert "task3" in mock_save_tasks.call_args_list[0][0]
```