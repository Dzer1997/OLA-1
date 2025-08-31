from app.models import Task  
from app.db import get_connection
from app.db import get_connection
class Task:
    def __init__(self, title, category=None, deadline=None, completed=False):
        self.title = title
        self.category = category
        self.deadline = deadline
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return (
            f"Task(title={self.title}, "
            f"category={self.category}, "
            f"deadline={self.deadline}, "
            f"completed={self.completed})"
        )


# 1️. Test task creation
def test_task_creation():
    task = Task("Finish homework", "School", "2025-09-01")
    assert task.title == "Finish homework"
    assert task.category == "School"
    assert task.deadline == "2025-09-01"
    assert task.completed is False

# 2️. Test marking a task as completed
def test_mark_completed():
    task = Task("Wash dishes")
    task.mark_completed()
    assert task.completed is True

# 3️. Test default values (category and deadline should be None if not given)
def test_task_defaults():
    task = Task("Go jogging")
    assert task.category is None
    assert task.deadline is None
    assert task.completed is False

# 4️. Test string representation
def test_task_str():
    task = Task("Buy milk", "Shopping", "2025-09-02")
    expected = "Task(title=Buy milk, category=Shopping, deadline=2025-09-02, completed=False)"
    assert str(task) == expected

# 5. Test that completed task stays completed
def test_task_stays_completed():
    task = Task("Read book")
    task.mark_completed()
    task.mark_completed()  
    assert task.completed is True
