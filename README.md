 **Todo List Application – Class Description**

The **`TodoList`** class is a simple Python-based application designed to manage and organize daily tasks. It allows users to add new tasks, mark tasks as completed, remove tasks, and display all tasks with their completion status.

---

**Class: `TodoList`**

🔧 **Constructor:**

* **`__init__(self)`**
  Initializes an empty task list called `self.tasks`. Each task is stored as a dictionary with two keys:

  * `"task"`: the task description (a string)
  * `"completed"`: a boolean indicating whether the task is completed (`False` by default)

---

 **Methods:**

 ➕ `add_task(self, task)`

* Adds a new task to the list.
* Input: `task` (string) — the description of the task.
* Adds the task as a dictionary with `"completed": False`.

 ✅ `complete_task(self, index)`

* Marks a task as completed based on its index in the list.
* Input: `index` (integer) — the position of the task (0-based).
* Sets `"completed": True` if the index is valid.

 ❌ `remove_task(self, index)`

* Removes a task from the list using its index.
* Input: `index` (integer).
* Deletes the task if the index is within range.

 📋 `display_tasks(self)`

* Displays all tasks with their completion status.
* Uses a checkmark `✓` to indicate completed tasks.
* Format:
  `1. [✓] Learn Python`
  `2. [ ] Build projects`

---

 **Example Usage:**

```python
todo = TodoList()
todo.add_task("Learn Python")
todo.add_task("Build projects")
todo.complete_task(0)
todo.display_tasks()
```

**Output:**

```
1. [✓] Learn Python
2. [ ] Build projects
```

---

✅ **Features Summary:**

* Add unlimited tasks.
* Mark any task as completed.
* Remove tasks easily.
* Clear visual display of task status.

