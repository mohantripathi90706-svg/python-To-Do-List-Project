file_name="tasks.txt"

def load_tasks():

    try:

        with open(file_name,"r") as f:

            return f.readlines()

    except:

        return []

def save_tasks(tasks):

    with open(file_name,"w") as f:

        for task in tasks:

            f.write(task)

def show_tasks(tasks):

    if len(tasks)==0:

        print("No tasks")

    else:

        for i in range(len(tasks)):

            print(i+1,tasks[i])

def add_task(tasks):

    task=input("Enter task:")

    tasks.append(task+"\n")

    print("Task added")

def delete_task(tasks):

    show_tasks(tasks)

    num=int(input("Enter task number:"))

    if num<=len(tasks):

        tasks.pop(num-1)

        print("Deleted")

    else:

        print("Invalid")

tasks=load_tasks()

while True:

    print("\nTO DO LIST")

    print("1 Show")

    print("2 Add")

    print("3 Delete")

    print("4 Exit")

    choice=input("Enter choice:")

    if choice=='1':

        show_tasks(tasks)

    elif choice=='2':

        add_task(tasks)

        save_tasks(tasks)

    elif choice=='3':

        delete_task(tasks)

        save_tasks(tasks)

    elif choice=='4':

        break

    else:

        print("Wrong choice")