import os
import json

# File to store tasks
TASKS_FILE = 'tasks.json'


def load_tasks():
    # Load tasks from the file
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
        return tasks
    else:
        return []


def save_tasks(tasks):
    # save tasks to file
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)


def display_tasks(tasks):
    # Display tasks along with their status.
    print("To-Do list:")
    for index, task in enumerate(tasks, start=1):
        status = "[X]" if task['completed'] else " [ ]"
        print(f"{index}. {task['description']}{status}")


def add_task(description, tasks):
    # Add a new task.
    task = {'description': description, 'completed': False}
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{description}" added to the to-do list. ')


def delete_task(index, tasks):
    # Delete task by index
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f'Task "{deleted_task["description"]}" deleted.')
    else:
        print("Invalid task index.")


def mark_completed(index, tasks):
    # Mark as completed by index
    if 1 <= index <= len(tasks):
        tasks[index - 1]['completed'] = True
        save_tasks(tasks)
        print(f'Task marked as completed: "{tasks[index - 1]["description"]}"')
    else:
        print("Invalid task index")


def main():
    tasks = load_tasks()
    while True:
        display_tasks(tasks)

        print("\nOptions:\n1. Add Task \n2. Delete Task\n3. Mark as completed \n4. Exit\n")

        choice = input("Enter your choice:")

        if choice == '1':
            description = input("Enter description:")
            add_task(description, tasks)
        elif choice == '2':
            index = int(input("Enter task number to delete:"))
            delete_task(index, tasks)
        elif choice == '3':
            index = int(input("Enter task number to mark as completed:"))
            mark_completed(index, tasks)
        elif choice == '4':
            print("Exiting the to-do application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
