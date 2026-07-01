def task():
    tasks = []
    print("--- Welcome to the Task Management App ---")

    total_tasks = int(input("Enter the total number of tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter the name of task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks: \n{tasks}")