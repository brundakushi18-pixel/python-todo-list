# todo_cli.py
# Simple command-line To-Do List app

import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for t in tasks:
            f.write(t + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task added: {task}")
    else:
        print("Empty task not added.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Quit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

