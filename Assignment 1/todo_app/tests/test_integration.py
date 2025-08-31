import pytest
from app.db import get_connection
from app.models import Task
from datetime import date

# --- Integration Test 1: Insert and Fetch a Task ---
def test_insert_and_fetch_task():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert test record
    cursor.execute(
        "INSERT INTO tasks (title, category, deadline, completed) VALUES (%s, %s, %s, %s)",
        ("Integration Test", "Testing", "2025-09-01", False)
    )
    conn.commit()

    # Fetch it back
    cursor.execute(
        "SELECT title, category, deadline, completed FROM tasks WHERE title=%s",
        ("Integration Test",)
    )
    result = cursor.fetchone()

    # Assert the values
    assert result[0] == "Integration Test"
    assert result[1] == "Testing"
    assert str(result[2]) == "2025-09-01"
    assert result[3] == 0  # MySQL stores False as 0

    # Cleanup
    cursor.execute("DELETE FROM tasks WHERE title=%s", ("Integration Test",))
    conn.commit()

    cursor.close()
    conn.close()


# --- Integration Test 2: Update a Task's Completed Status ---
def test_update_task_completed():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert test record
    cursor.execute(
        "INSERT INTO tasks (title, category, deadline, completed) VALUES (%s, %s, %s, %s)",
        ("Update Test", "Testing", "2025-09-02", False)
    )
    conn.commit()

    # Update completed status
    cursor.execute(
        "UPDATE tasks SET completed=%s WHERE title=%s",
        (True, "Update Test")
    )
    conn.commit()

    # Fetch updated task
    cursor.execute(
        "SELECT completed FROM tasks WHERE title=%s",
        ("Update Test",)
    )
    result = cursor.fetchone()
    assert result[0] == 1  # True stored as 1 in MySQL

    # Cleanup
    cursor.execute("DELETE FROM tasks WHERE title=%s", ("Update Test",))
    conn.commit()

    cursor.close()
    conn.close()
