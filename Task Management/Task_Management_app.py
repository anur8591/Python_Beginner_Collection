def task():
    tasks = []
    print("--- Welcome to the Task Management App ---")

    total_tasks = int(input("Enter the total number of tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter the name of task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks: \n{tasks}")

    while True:
        operation = int(input("Enter: \n1-ADD\n2-UPDATE\n3-DELETE\n4-VIEW\n5-EXIT/stop/"))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task {add} has been successfully added.... ")
        
        elif operation == 2:
            update = input("Enter task you want to update = ")
            if update in tasks:
                new_task = input("Enter the new task name = ")
                index = tasks.index(update)
                tasks[index] = new_task
                print(f"updated task {new_task}")

        elif operation == 3:
            delete = input("Enter task you want to delete = ")
            if delete in tasks:
                index = tasks.index(delete)
                del tasks[index]
                print(f"Task {delete} has been successfully deleted.... ")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("closing the app....")
            break

        else:
            print("Invalid input, please try again.")


task()