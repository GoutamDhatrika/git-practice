tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")
    print("4. Delete task")
    print("5. Complete task")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, 1):
                print(f"{number}. {task}")

    elif choice == "3":
        break

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for number, task in enumerate(tasks, 1):
                print(f"{number}. {task}")

            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")
        elif choice == "5":
            if not tasks:
                print("No tasks to complete.")
            else:
                for number, task in enumerate(tasks, 1):
                    print(f"{number}. {task}")

                number = int(input("Enter task number to complete: "))

                if 1 <= number <= len(tasks):
                    print(f"Completed: {tasks[number - 1]}")
                else:
                    print("Invalid task number.")
    else:
        print("Invalid choice.")