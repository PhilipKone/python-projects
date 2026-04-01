import json
import os
import sys

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_menu():
    print("\n--- Python To-Do CLI ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "[x]" if task.get("done") else "[ ]"
        print(f"{idx}. {status} {task['title']} - {task.get('description', '')}")

def add_task(tasks):
    title = input("Enter task title: ")
    desc = input("Enter description (optional): ")
    tasks.append({"title": title, "description": desc, "done": False})
    save_tasks(tasks)
    print("Task added!")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        tasks = load_tasks()
        show_menu()
        choice = input("Select an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
