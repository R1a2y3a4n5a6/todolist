import sqlite3

def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    task TEXT,
                    completed BOOLEAN NOT NULL DEFAULT 0,
                    due_time TEXT)''')
    conn.commit()
    conn.close()

def mark_task_as_completed(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()

def set_due_time(task_id, due_time):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET due_time = ? WHERE id = ?", (due_time, task_id))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, completed, due_time FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()


def renumber_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM tasks")
    tasks = c.fetchall()

    for new_id, task in enumerate(tasks, start=1):
        old_id = task[0]
        c.execute("UPDATE tasks SET id=? WHERE id=?", (new_id, old_id))

    conn.commit()
    conn.close()
