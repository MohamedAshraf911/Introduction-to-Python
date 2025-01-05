import os
import datetime

TASK_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    task = input("Enter the task: ")
    while not task:
        print("Task cannot be empty.")
        task = input("Enter the task: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append(f"{task} (added on {timestamp})")
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            save_tasks(tasks)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTask List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()