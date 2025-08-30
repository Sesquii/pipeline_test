```markdown
```python
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
```