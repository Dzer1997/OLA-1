from app.db import get_connection
from app.models import Task

def test_task_workflow():

    
    # Step 1: Create Task object
    task = Task("Write report", "Work", "2025-09-05")
    
    # Step 2: Mark task as completed
    task.mark_completed()
    
    # Step 3: Verify object attributes
    assert task.title == "Write report"
    assert task.category == "Work"
    assert task.deadline == "2025-09-05"
    assert task.completed is True
    
    # Step 4: Insert into database
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, category, deadline, completed) VALUES (%s, %s, %s, %s)",
        (task.title, task.category, task.deadline, task.completed)
    )
    conn.commit()
    
    # Step 5: Verify in database
    cursor.execute("SELECT title, category, deadline, completed FROM tasks WHERE title=%s", (task.title,))
    result = cursor.fetchone()
    assert result[0] == task.title
    assert result[1] == task.category
    assert str(result[2]) == task.deadline
    assert result[3] == 1  # True stored as 1 in MySQL
    
    # Step 6: Cleanup
    cursor.execute("DELETE FROM tasks WHERE title=%s", (task.title,))
    conn.commit()
    cursor.close()
    conn.close()
