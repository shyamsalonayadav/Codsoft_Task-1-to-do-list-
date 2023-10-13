#Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to list all tasks
def list_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

# Function to remove a task by its index
def remove_task(index):
    try:
        task = tasks.pop(index)
        print(f"Task '{task}' removed!")
    except IndexError:
        print("Invalid task index. Use 'list' to see available tasks.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        list_tasks()
        index = input("Enter the index of the task to remove: ")
        if index.isdigit():
            remove_task(int(index) - 1)
        else:
            print("Invalid input. Please enter a valid index.")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose a valid option.")

# End of the program
print("Goodbye!")





