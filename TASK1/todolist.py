todo_list=[]

def show_menu():
    print("1. Add Task")
    print("2. view Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit Task")

def add_task():
    task = input("Enter task:")
    todo_list.append([task,False])
    print("Task added!")

def view_tasks():
    if len(todo_list) == 0:
       print("No tasks yet.")
       return
    for i, t in enumerate(todo_list):
        status = "Completed" if t[1] else "Pending"
        print(f"{i+1}. {t[0]} - {status}")

def update_task():
    view_tasks()
    num = int(input("Task number to update;"))
    new = input("Enter new task:")
    todo_list[num - 1][0] = new
    print("Task updated!")

def delete_task():
    view_tasks()
    num = int(input("Task number to delete:"))
    todo_list.pop(num-1)
    print("Task deleted!")

def mark_complete():
    view_tasks()
    num = int(input("Task number to mark completed:"))
    todo_list[num - 1][1] = True
    print("Task marked completed!")

while True:
    show_menu()
    ch = input("Enter choice: ")

    if ch == "1":
        add_task()
    elif ch == "2":
        view_tasks()
    elif ch == "3":
        update_task()
    elif ch == "4":
        delete_task()
    elif ch == "5":
        mark_complete()
    elif ch == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")
