import json

# Initialize an empty task list (tasks will be loaded from a file if available)
tasks = []

def load_tasks():
    """Loads tasks from a JSON file if it exists."""
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks():
    """Saves the current task list to a JSON file."""
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task():
    """Prompts user to add a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks()
    print(f"Task '{task}' added successfully!")

def view_tasks():
    """Displays all tasks in the list."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(tasks, 1):
            status = "Completed" if task['completed'] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")

def update_task():
    """Allows the user to update the completion status of a task."""
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete/incomplete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['completed'] = not tasks[task_num]['completed']
            save_tasks()
            print(f"Task '{tasks[task_num]['task']}' updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    """Deletes a task from the list."""
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            save_tasks()
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main loop for the to-do list application."""
    global tasks
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting application... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
