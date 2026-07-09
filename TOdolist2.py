# To-Do List with File Storage

# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)

        with open("tasks.txt", "w") as file:
            for item in tasks:
                file.write(item + "\n")

        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            delete_num = int(input("Enter task number to delete: "))

            if 1 <= delete_num <= len(tasks):
                removed_task = tasks.pop(delete_num - 1)

                with open("tasks.txt", "w") as file:
                    for item in tasks:
                        file.write(item + "\n")

                print(f"'{removed_task}' deleted successfully!")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Please enter 1-4.")