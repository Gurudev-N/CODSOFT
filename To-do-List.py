class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{completed_task}" completed and removed.')
        else:
            print("Invalid task index.")

todo_list = ToDoList()

todo_list.add_task("Complete project")
todo_list.add_task("Buy groceries")
todo_list.view_tasks()
todo_list.complete_task(1)
todo_list.view_tasks()
