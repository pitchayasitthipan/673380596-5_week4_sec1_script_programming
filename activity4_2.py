# activity4_2.py
# Activity 4.2: Interactive To-Do List (using List Operations)

todo_list = []

while True:
    print("\n=== To-Do List ===")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Exit")
    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        task = input("Task: ").strip()
        if task:
            todo_list.append(task)
            print(f"Added '{task}'")
        else:
            print("Task cannot be empty")
    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks yet")
        else:
            print(f"You have {len(todo_list)} task(s):")
            for i in range(len(todo_list)):
                print(f"  {i + 1}. {todo_list[i]}")
    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to complete")
        else:
            for i in range(len(todo_list)):
                print(f"  {i + 1}. {todo_list[i]}")
            number = input("Enter task number or name to complete: ").strip()
            if number.isdigit() and 1 <= int(number) <= len(todo_list):
                done = todo_list.pop(int(number) - 1)
                print(f"Completed '{done}'")
            elif number in todo_list:
                todo_list.remove(number)
                print(f"Completed '{number}'")
            else:
                print("Task not found")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1-4")
