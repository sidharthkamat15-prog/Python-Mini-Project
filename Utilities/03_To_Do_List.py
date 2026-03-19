                                # Simple To-Do List Application

print("\n--- TO-DO LIST MENU ---")
print("1. View To-Do List")
print("2. Add Task")
print("3. Remove Task")
print("4. Exit")

task = []

while True:   # loop keeps running until user chooses 4
    user = input("\nEnter your choice (1-4): ")

    if user == '1':
        if not task:
            print("\nYour to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for idx, item in enumerate(task, start=1):
                print(f"{idx}. {item}")

    elif user == '2':
        new_task = input("Enter the task you want to add: ")
        task.append(new_task)
        print(f'"{new_task}" has been added to your to-do list.')

    elif user == '3':
        if not task:
            print("\nYour to-do list is empty. No tasks to remove.")
        else:
            print("\nYour To-Do List:")
            for idx, item in enumerate(task, start=1):
                print(f"{idx}. {item}")
            try:
                task_num = int(input("Enter the task number you want to remove: "))
                if 1 <= task_num <= len(task):
                    removed_task = task.pop(task_num - 1)
                    print(f'"{removed_task}" has been removed from your to-do list.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif user == '4':
        print("Exiting the To-Do List application. Goodbye!")
        break   # exits the while loop

    else:
        print("Invalid option. Please choose a number between 1 and 4.")