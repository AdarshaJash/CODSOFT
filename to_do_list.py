import json
import os

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        task = {
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(" Task added.")

    def view_tasks(self):
        if not self.tasks:
            print(" Sorry...! No tasks available.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{idx}. {task['description']} - {status}")

    def update_task(self, task_number, description=None, completed=None):
        if 0 < task_number <= len(self.tasks):
            if description is not None:
                self.tasks[task_number - 1]['description'] = description
            if completed is not None:
                self.tasks[task_number - 1]['completed'] = completed
            self.save_tasks()
            print(" Task updated Successfully ")
        else:
            print(" Sorry...! Invalid task number.")
            print(" Please try with different task number")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            self.save_tasks()
            print(" The task is deleted.")
        else:
            print(" Invalid task number.")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTo-Do List ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input(" Choose an option:  ")
        
        if choice == '1':
            description = input(" \nEnter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input(" \nEnter the task number to update: "))
            new_description = input(" Write the new description for the task (leave empty to keep unchanged): ")
            completed = input(" Mark as completed? (yes/no/leave empty to keep unchanged): ")
            completed = True if completed.lower() == 'yes' else (False if completed.lower() == 'no' else None)
            todo_list.update_task(task_number, description=new_description if new_description else None, completed=completed)
        elif choice == '4':
            task_number = int(input("\n Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("\n Thank you.")
            print(" Have a productive day.")
            print(" Designed by ADARSHA JASH ")
            break
        else:
            print(" Invalid choice.  Please try again. ")

if __name__ == '__main__':
    main()