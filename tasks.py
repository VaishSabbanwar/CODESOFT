tasks = []

def add_task():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def list_tasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"Task #{index}. {task}")

def delete_task():
    list_tasks()
    try:
        task_to_delete = int(input("Enter the # to delete: "))
        if task_to_delete > 0 and task_to_delete <= len(tasks):
            tasks.pop(task_to_delete - 1)
            print(f"Task {task_to_delete} has been removed.")
        else:
            print(f"Task # {task_to_delete} was not found.")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    print("Welcome to your to-do list!")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List of tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("See you soon!")
            break
        else:
            print("Invalid input. Please try once again.")