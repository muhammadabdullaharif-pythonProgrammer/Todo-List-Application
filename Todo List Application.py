# Define the TodoList class
class TodoList:
    # Constructor to initialize the task list
    def __init__(self):
        self.tasks = []  # Empty list to store tasks
    
    # Method to add a new task
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})  # Add task with 'completed' set to False
    
    # Method to mark a task as completed
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):  # Check if index is valid
            self.tasks[index]["completed"] = True  # Mark the task as completed
    
    # Method to remove a task by index
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):  # Check if index is valid
            del self.tasks[index]  # Delete the task from the list
    
    # Method to display all tasks with their status
    def display_tasks(self):
        for i, task in enumerate(self.tasks):  # Loop through all tasks
            status = "✓" if task["completed"] else " "  # Set status symbol based on completion
            print(f"{i+1}. [{status}] {task['task']}")  # Print task with status

# Example usage of the TodoList class
todo = TodoList()  # Create a new TodoList object
todo.add_task("Learn Python")  # Add first task
todo.add_task("Build projects")  # Add second task
todo.complete_task(0)  # Mark the first task as completed
todo.display_tasks()  # Display all tasks
