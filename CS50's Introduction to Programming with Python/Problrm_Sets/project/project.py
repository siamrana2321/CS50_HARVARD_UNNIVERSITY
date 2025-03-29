import json
from datetime import datetime

def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Task description: ")
            category = input("Category: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            priority = input("Priority (High, Medium, Low): ")
            add_task(tasks, task, category, due_date, priority)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(tasks, task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

def add_task(tasks, task, category, due_date, priority):
    tasks.append({
        "id": len(tasks) + 1,
        "task": task,
        "category": category,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    })
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        print(f"{task['id']}. {task['task']} | {task['category']} | Due: {task['due_date']} | Priority: {task['priority']} | Status: {status}")

def mark_task_completed(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("Task marked as completed!")
            return
    print("Task ID not found.")

def delete_task(tasks, task_id):
    global task_list
    tasks[:] = [task for task in tasks if task["id"] != task_id]
    print("Task deleted successfully!")

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    main()
