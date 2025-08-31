import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="",
        password=""
        database="todo_app"
    )
