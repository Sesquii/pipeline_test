import json
import random
import time
import threading
import sys
import os

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        else:
            # Return empty list if file doesn't exist
            return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(description):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append({"description": description, "timestamp": time.time()})
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    """Display all current tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['description']}")

def delete_random_task():
    """Delete one randomly chosen task from the list."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return
    
    # Choose a random index
    index = random.randint(0, len(tasks) - 1)
    deleted_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted task: {deleted_task['description']}")

def automatic_deletion():
    """Run automatic deletion every hour."""
    while True:
        try:
            # Wait for an hour (3600 seconds)
            time.sleep(3600)
            delete_random_task()
        except KeyboardInterrupt:
            print("\nAutomatic deletion stopped.")
            break
        except Exception as e:
            print(f"Error in automatic deletion: {e}")
            break

def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python intermittent_todo.py [add <task> | list]")
        return
    
    command = sys.argv[1]
    
    if command == "add" and len(sys.argv) >= 3:
        task_description = " ".join(sys.argv[2:])
        add_task(task_description)
    elif command == "list":
        list_tasks()
    else:
        print("Usage: python intermittent_todo.py [add <task> | list]")

if __name__ == "__main__":
    # Start the automatic deletion in a separate thread
    deletion_thread = threading.Thread(target=automatic_deletion, daemon=True)
    deletion_thread.start()
    
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
