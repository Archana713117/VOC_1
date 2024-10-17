import json
import os

# Task class to represent each task
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        status = 'Completed' if self.completed else 'Pending'
        return f"{self.title} [{self.category}] - {status}: {self.description}"

# Save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Load tasks from a JSON file
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            tasks_data = json.load(f)
            return [Task(**data) for data in tasks_data]
    return []

# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

# Command-line interface for the To-Do List application
def main():
    tasks = load_tasks()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category (Work, Personal, Urgent): ")
            tasks.append(Task(title, description, category))
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            display_tasks(tasks)
            task_num = int(input("Enter task number to edit: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num].title = input(f"Edit title (current: {tasks[task_num].title}): ")
                tasks[task_num].description = input(f"Edit description (current: {tasks[task_num].description}): ")
                tasks[task_num].category = input(f"Edit category (current: {tasks[task_num].category}): ")
            else:
                print("Invalid task number.")
        elif choice == '4':
            display_tasks(tasks)
            task_num = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num].mark_completed()
                print(f"Task '{tasks[task_num].title}' marked as completed.")
            else:
                print("Invalid task number.")
        elif choice == '5':
            display_tasks(tasks)
            task_num = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                print(f"Task '{tasks[task_num].title}' deleted.")
                tasks.pop(task_num)
            else:
                print("Invalid task number.")
        elif choice == '6':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

# Ensure this block is called when running the script
if __name__ == "__main__":
    main()