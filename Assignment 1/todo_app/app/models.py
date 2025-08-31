
from app.db import get_connection
class Task:
    def __init__(self, title, category=None, deadline=None):
        self.title = title
        self.category = category
        self.deadline = deadline
        self.completed = False

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, category, deadline, completed) VALUES (%s, %s, %s, %s)",
            (self.title, self.category, self.deadline, self.completed)
        )
        conn.commit()
        conn.close()

    def mark_completed(self):
        self.completed = True
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET completed = %s WHERE title = %s",
            (self.completed, self.title)
        )
        conn.commit()
        conn.close()
