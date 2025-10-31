def main():
    print("Welcome to the Simple To-Do App!")
    tasks = []

    while True:
        command = input("Enter a command (add, remove, list, exit): ").strip().lower()

        if command == "add":
            title = input("Enter the task title: ")
            tasks.append({"title": title, "completed": False})
            print(f"Task '{title}' added.")

        elif command == "remove":
            task_id = int(input("Enter the task ID to remove: "))
            if 0 <= task_id < len(tasks):
                removed_task = tasks.pop(task_id)
                print(f"Task '{removed_task['title']}' removed.")
            else:
                print("Invalid task ID.")

        elif command == "list":
            print("Tasks:")
            for idx, task in enumerate(tasks):
                status = "✓" if task["completed"] else "✗"
                print(f"{idx}: {task['title']} [{status}]")

        elif command == "exit":
            print("Exiting the Simple To-Do App. Goodbye!")
            break

        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()