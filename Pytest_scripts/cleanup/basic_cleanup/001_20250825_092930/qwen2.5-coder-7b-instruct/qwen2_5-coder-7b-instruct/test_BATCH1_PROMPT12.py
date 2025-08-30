markdown
import json
import random
import time
import threading

# Constants
TASKS_FILE = 'tasks.json'
LOG_FILE = 'deletion_log.txt'

def load_tasks():
    """Load tasks from a JSON file."""
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(task_description):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append(task_description)
    save_tasks(tasks)
    print(f"Task added: {task_description}")

def list_tasks():
    """List all current tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}: {task}")

def delete_random_task():
    """Delete a random task and log the action."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    task_to_delete = random.choice(tasks)
    tasks.remove(task_to_delete)
    save_tasks(tasks)

    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"Deleted: {task_to_delete} at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"Task deleted: {task_to_delete}")

def scheduled_task():
    """Scheduled task to run every hour."""
    while True:
        delete_random_task()
        time.sleep(3600)  # Wait for one hour

def main():
    """Main function to handle user input and call the appropriate functions."""
    try:
        if len(sys.argv) < 2:
            print("Usage: python intermittent_todo.py [add <task> | list]")
            return

        command = sys.argv[1]

        if command == 'add':
            if len(sys.argv) > 2:
                add_task(' '.join(sys.argv[2:]))
            else:
                print("Usage: python intermittent_todo.py add <task>")
        elif command == 'list':
            list_tasks()
        else:
            print(f"Invalid command: {command}")
    except KeyboardInterrupt:
        print("\nGracefully shutting down...")
    finally:
        save_tasks(load_tasks())  # Ensure tasks are saved before exiting

if __name__ == "__main__":
    import sys
    main()

# Schedule the deletion task to run every hour in a separate thread
deletion_thread = threading.Thread(target=scheduled_task)
deletion_thread.daemon = True
deletion_thread.start()

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Constants
TASKS_FILE = 'tasks.json'
LOG_FILE = 'deletion_log.txt'

def load_tasks():
    """Load tasks from a JSON file."""
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(task_description: str):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append(task_description)
    save_tasks(tasks)
    print(f"Task added: {task_description}")

def list_tasks():
    """List all current tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}: {task}")

def delete_random_task():
    """Delete a random task and log the action."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    task_to_delete = random.choice(tasks)
    tasks.remove(task_to_delete)
    save_tasks(tasks)

    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"Deleted: {task_to_delete} at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"Task deleted: {task_to_delete}")

def scheduled_task():
    """Scheduled task to run every hour."""
    while True:
        delete_random_task()
        time.sleep(3600)  # Wait for one hour

def main():
    """Main function to handle user input and call the appropriate functions."""
    try:
        if len(sys.argv) < 2:
            print("Usage: python intermittent_todo.py [add <task> | list]")
            return

        command = sys.argv[1]

        if command == 'add':
            if len(sys.argv) > 2:
                add_task(' '.join(sys.argv[2:]))
            else:
                print("Usage: python intermittent_todo.py add <task>")
        elif command == 'list':
            list_tasks()
        else:
            print(f"Invalid command: {command}")
    except KeyboardInterrupt:
        print("\nGracefully shutting down...")
    finally:
        save_tasks(load_tasks())  # Ensure tasks are saved before exiting

if __name__ == "__main__":
    import sys
    main()

# Schedule the deletion task to run every hour in a separate thread
deletion_thread = threading.Thread(target=scheduled_task)
deletion_thread.daemon = True
deletion_thread.start()

# Test cases
def test_load_tasks():
    """Test loading tasks from a JSON file."""
    save_tasks(['task1', 'task2'])
    assert load_tasks() == ['task1', 'task2']

def test_save_tasks():
    """Test saving tasks to a JSON file."""
    tasks = ['task3', 'task4']
    save_tasks(tasks)
    with open(TASKS_FILE, 'r') as file:
        loaded_tasks = json.load(file)
    assert loaded_tasks == tasks

def test_add_task():
    """Test adding a new task."""
    initial_tasks = load_tasks()
    add_task('new_task')
    final_tasks = load_tasks()
    assert len(final_tasks) == len(initial_tasks) + 1
    assert 'new_task' in final_tasks

def test_list_tasks():
    """Test listing all tasks."""
    save_tasks(['task5', 'task6'])
    list_tasks()

def test_delete_random_task():
    """Test deleting a random task."""
    initial_tasks = load_tasks()
    add_task('task7')
    delete_random_task()
    final_tasks = load_tasks()
    assert len(final_tasks) == len(initial_tasks)
    assert 'task7' not in final_tasks

def test_scheduled_task(mocker):
    """Test the scheduled task to run every hour."""
    mocker.patch('time.sleep', return_value=None)
    initial_tasks = load_tasks()
    add_task('task8')
    delete_random_task()
    final_tasks = load_tasks()
    assert len(final_tasks) == len(initial_tasks)
    assert 'task8' not in final_tasks

def test_main_add_command():
    """Test the main function with the 'add' command."""
    initial_tasks = load_tasks()
    add_task('task9')
    final_tasks = load_tasks()
    assert len(final_tasks) == len(initial_tasks) + 1
    assert 'task9' in final_tasks

def test_main_list_command():
    """Test the main function with the 'list' command."""
    save_tasks(['task10'])
    list_tasks()

def test_main_invalid_command():
    """Test the main function with an invalid command."""
    initial_tasks = load_tasks()
    add_task('task11')
    with pytest.raises(SystemExit):
        main()
