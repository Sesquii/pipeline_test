import json
import random
import time
import threading
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file, return empty list if file doesn't exist or is invalid."""
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        else:
            # Create file with empty list if it doesn't exist
            save_tasks([])
            return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=2)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def add_task(description):
    """Add a new task to the list."""
    tasks = load_tasks()
    # Add task with timestamp and unique ID
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "timestamp": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    """Display all current tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Current tasks:")
        for task in tasks:
            print(f"  [{task['id']}] {task['description']} (Added: {task['timestamp']})")

def delete_random_task():
    """Delete one randomly chosen task from the list."""
    tasks = load_tasks()
    
    # Check if there are any tasks to delete
    if not tasks:
        print("No tasks to delete - list is empty.")
        return
    
    # Choose a random task index
    random_index = random.randint(0, len(tasks) - 1)
    deleted_task = tasks.pop(random_index)
    
    # Save updated task list
    save_tasks(tasks)
    
    # Log the deletion
    print(f"Deleted task: {deleted_task['description']} (ID: {deleted_task['id']})")

def automatic_deletion_worker():
    """Background thread that deletes a random task every hour."""
    while True:
        try:
            # Wait for 1 hour (3600 seconds)
            time.sleep(3600)
            
            # Delete one random task
            delete_random_task()
            
        except KeyboardInterrupt:
            # Handle graceful shutdown
            print("\nAutomatic deletion stopped.")
            break
        except Exception as e:
            print(f"Error in automatic deletion: {e}")

def main():
    """Main application loop."""
    print("Intermittent To-Do List Application")
    print("Commands: add <task>, list, quit")
    
    # Start automatic deletion thread
    deletion_thread = threading.Thread(target=automatic_deletion_worker, daemon=True)
    deletion_thread.start()
    
    try:
        while True:
            try:
                user_input = input("\nEnter command: ").strip().lower()
                
                if user_input == "quit":
                    print("Goodbye!")
                    break
                elif user_input.startswith("add "):
                    description = user_input[4:].strip()
                    if description:
                        add_task(description)
                    else:
                        print("Please provide a task description.")
                elif user_input == "list":
                    list_tasks()
                else:
                    print("Unknown command. Use 'add <task>', 'list', or 'quit'.")
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
                
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure we clean up threads properly
        pass

if __name__ == "__main__":
    main()
