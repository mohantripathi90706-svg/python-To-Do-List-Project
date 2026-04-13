Project Structure : - 
 
Planning
Logic Design
Code Writing
File Storage


STEP - 1     Project Idea OR Planning



Task add kare
Task dekhe
Task Delete kare
Tasks Save ho jaye

 for example :
1 Study Python
2 Complete assignment
3 Revise DSA


Step 2:     Logic design 


Sabse pehle socho data kaha store hoga?

Python me:

List use karenge → tasks = []

Example:

tasks = ["Study", "Gym", "Revision"]


Step 3:    Functions decide karo


Project me functions hone chahiye:

show_tasks()
add_task()
delete_task()
save_tasks()
load_tasks()

"I used modular programming using functions"


Step 4:    Basic structure code 


   Step 4.1 Import file handling

       file_name = "tasks.txt"

   Step 4.2 Load tasks function

       Program start hote hi file read hogi:

      def load_tasks():

          try:
              with open("tasks.txt","r") as f:
               return f.readlines()

          except:
                 return []

Concept used:

File handling
Exception handling

"Try except used to avoid file not found error"

Step 4.3 Save task function

def save_tasks(tasks):

    with open("tasks.txt","w") as f:

        for task in tasks:
            f.write(task)

Concept:

File write mode
Loop

Step 4.4 Show tasks

def show_tasks(tasks):

    if len(tasks)==0:
        print("No tasks")

    else:

        for i in range(len(tasks)):

            print(i+1 , tasks[i])

Concept:

Loop
Indexing

Step 4.5 Add task

def add_task(tasks):

    task=input("Enter task: ")

    tasks.append(task+"\n")

    print("Task added")

Concept:

List append
Input

Step 4.6 Delete task

def delete_task(tasks):

    show_tasks(tasks)

    num=int(input("Enter task number: "))

    if num<=len(tasks):

        tasks.pop(num-1)

        print("Task removed")

    else:

        print("Invalid")

Concept:

Pop
Condition

Step 5:    Main program (most important part)


tasks = load_tasks()

while True:

    print("\nTO DO LIST")

    print("1 Show")
    print("2 Add")
    print("3 Delete")
    print("4 Exit")

    choice=input("Enter choice: ")

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



        FINAL PROJECT COMPLETE CODE 



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
