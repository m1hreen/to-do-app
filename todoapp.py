def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

while True:
    print("\n--- TO DO APP ---")
    print("1. Add")
    print("2. View")
    print("3. Delete")
    print("4. Complete")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for i in range(len(tasks)):
                print(i+1, tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete")
        else:
            for i in range(len(tasks)):
                print(i+1, tasks[i])

            try:
                num = int(input("Enter task number: "))
                if 0 < num <= len(tasks):
                    tasks.pop(num-1)
                    save_tasks(tasks)
                    print("Task deleted")
                else:
                    print("Invalid number")
            except:
                print("Enter a number")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks")
        else:
            for i in range(len(tasks)):
                print(i+1, tasks[i])

            try:
                num = int(input("Enter task number: "))
                if 0 < num <= len(tasks):
                    tasks[num-1] = "[Done] " + tasks[num-1]
                    save_tasks(tasks)
                    print("Marked complete")
                else:
                    print("Invalid number")
            except:
                print("Enter a number")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
