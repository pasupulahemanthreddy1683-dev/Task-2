FILE_NAME = "tasks.txt"

def load():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save(tasks)
    print("Task added successfully!\n")

def view(tasks):
    if not tasks:
        print("No tasks available.\n")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()

def remove(tasks):
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to remove: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save(tasks)
            print(f"Task '{removed}' removed successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

if __name__ == "__main__":
    tasks = load()
    while True:
        print("---------- TO-DO LIST MENU ----------")
        print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add(tasks)
        elif choice == "2":
            view(tasks)
        elif choice == "3":
            remove(tasks)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")