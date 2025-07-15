import json;

def save_tasks():
    with open("shabbat_checklist.txt", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
    print("Tasks saved.")


def load_tasks():
    global tasks
    try:
        with open("shabbat_checklist.txt", "r", encoding="utf-8") as file:
            tasks = json.load(file)
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved checklist found. Starting fresh.")


tasks = [
    {"name": "Buy challah", "done": False},
    {"name": "Cook cholent", "done": False},
    {"name": "Light candles", "done": False},
    {"name": "Set the table", "done": False},
    {"name": "Turn off phone", "done": False}
]

def show_tasks():
    print("\nShabbat Preparation Checklist:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["done"] else ""
        print(f"{i}. {task['name']} {status}")

def mark_task_done():
    show_tasks()
    choice = int(input("Enter the task number to mark as done: "))
    if 1 <= choice <= len(tasks):
        tasks[choice - 1]["done"] = True
        print("Task marked as done.")
    else:
        print("Invalid choice.")


def add_task():
    new_task_name = input("Enter the name of the new task: ")
    new_task = {"name": new_task_name, "done": False}
    tasks.append(new_task)
    print("Task added.")

def remove_task():
    show_tasks()
    choice = int(input("Enter the task number to remove: "))
    if 1 <= choice <= len(tasks):
        tasks.pop(choice - 1)
        print("Task removed.")
    else:
        print("Invalid choice.")
   


load_tasks()

while True:
    print("\n--- Shabbat Checklist Menu ---")
    print("1. Show tasks")
    print("2. Mark task as done")
    print("3. Add task")
    print("4. Remove task")
    print("5. Save and Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        mark_task_done()
    elif choice == "3":
        add_task()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        save_tasks()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

