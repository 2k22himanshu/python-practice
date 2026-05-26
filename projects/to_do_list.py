# Simple To-Do List

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added")

    elif choice == "2":
        print("\nTasks:")
        for task in tasks:
            print("-", task)

    elif choice == "3":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")
