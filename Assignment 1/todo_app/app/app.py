from todo_app.app.models import Task

def main():
    while True:
        print("\n1. Add Task\n2. Complete Task\n3. View Tasks\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            category = input("Category: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            task = Task(title, category, deadline)
            task.save()
            print("Task added.")
        
        elif choice == "2":
            title = input("Task title to complete: ")
            task = Task(title)
            task.mark_completed()
            print("Task marked as completed.")

        elif choice == "3":
            conn = task.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            for row in cursor.fetchall():
                print(row)
            conn.close()

        elif choice == "4":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
