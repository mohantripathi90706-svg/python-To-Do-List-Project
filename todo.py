from datetime import datetime

file_name = "tasks.txt"

# Load tasks
def load_tasks():
    try:
        with open(file_name, "r") as f:
            return f.readlines()
    except:
        return []

# Save tasks
def save_tasks(tasks):
    with open(file_name, "w") as f:
        for task in tasks:
            f.write(task)

# Show tasks
def show_tasks(tasks):
    print("\n===== YOUR TASKS =====")

    if len(tasks) == 0:
        print("No tasks available")
    else:
        pending = 0
        done = 0

        for task in tasks:
            if "[Pending]" in task:
                pending += 1
            elif "[Done]" in task:
                done += 1

        print("Total:", len(tasks), "| Pending:", pending, "| Completed:", done)

        for i in range(len(tasks)):
            print(i+1, ".", tasks[i].strip())

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    priority = input("Enter priority (High/Medium/Low): ")

    time = datetime.now().strftime("%d-%m-%Y %H:%M")

    tasks.append(f"[Pending] || [{priority}] ||  {task}  || ({time})\n")

    print("Task added")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)

    try:
        num = int(input("Enter task number to delete: "))
    except:
        print("Enter valid number")
        return

    if 0 < num <= len(tasks):
        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() == 'y':
            tasks.pop(num-1)
            print("Task deleted")
        else:
            print("Cancelled")
    else:
        print("Invalid number")

# Delete all
def delete_all(tasks):
    confirm = input("Delete ALL tasks? (y/n): ")
    if confirm.lower() == 'y':
        tasks.clear()
        print("All tasks deleted")

# Edit task
def edit_task(tasks):
    show_tasks(tasks)

    try:
        num = int(input("Enter task number to edit: "))
    except:
        print("Enter valid number")
        return

    if 0 < num <= len(tasks):
        new_task = input("Enter new task: ")
        priority = input("Enter new priority (High/Medium/Low): ")

        time = datetime.now().strftime("%d-%m-%Y %H:%M")

        tasks[num-1] = f"[Pending][{priority}] {new_task} ({time})\n"

        print("Task updated")
    else:
        print("Invalid number")

# Mark complete
def mark_complete(tasks):
    show_tasks(tasks)

    try:
        num = int(input("Enter task number to mark complete: "))
    except:
        print("Enter valid number")
        return

    if 0 < num <= len(tasks):
        if "[Pending]" in tasks[num-1]:
            tasks[num-1] = tasks[num-1].replace("[Pending]", "[Done]")
            print("Task completed")
        else:
            print("Already completed")
    else:
        print("Invalid number")

# Search task
def search_task(tasks):
    keyword = input("Enter keyword to search: ").lower()

    found = False

    for task in tasks:
        if keyword in task.lower():
            print(task.strip())
            found = True

    if not found:
        print("No matching task found")

# MAIN
tasks = load_tasks()

while True:

    print("\n==============================")
    print("      TASK MANAGER     ")
    print("==============================")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Mark Complete")
    print("6. Search Task")
    print("7. Delete All Tasks")
    print("8. Exit")
    print("==============================")

    choice = input("Enter choice: ")

    if choice == '1':
        show_tasks(tasks)

    elif choice == '2':
        add_task(tasks)
        save_tasks(tasks)

    elif choice == '3':
        delete_task(tasks)
        save_tasks(tasks)

    elif choice == '4':
        edit_task(tasks)
        save_tasks(tasks)

    elif choice == '5':
        mark_complete(tasks)
        save_tasks(tasks)

    elif choice == '6':
        search_task(tasks)

    elif choice == '7':
        delete_all(tasks)
        save_tasks(tasks)

    elif choice == '8':
        save_tasks(tasks)
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")