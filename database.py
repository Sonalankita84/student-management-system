import sqlite3


def create_table():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_no TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        course TEXT NOT NULL,
        marks REAL NOT NULL,
        email TEXT
    )
    """)

    connection.commit()
    connection.close()


def add_student(roll_no, name, course, marks, email):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    try:
        cursor.execute("""
        INSERT INTO students (roll_no, name, course, marks, email)
        VALUES (?, ?, ?, ?, ?)
        """, (roll_no, name, course, marks, email))

        connection.commit()
        print("\nStudent added successfully!")

    except sqlite3.IntegrityError:
        print("\nError: This roll number already exists.")

    connection.close()


def view_students():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    return students
def search_student(roll_no):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    connection.close()

    return student

def update_student(roll_no, name, course, marks, email):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE students
    SET name = ?, course = ?, marks = ?, email = ?
    WHERE roll_no = ?
    """, (name, course, marks, email, roll_no))

    connection.commit()

    if cursor.rowcount > 0:
        print("\nStudent updated successfully!")
    else:
        print("\nStudent not found.")

    connection.close()

def delete_student(roll_no):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("\nStudent deleted successfully!")
    else:
        print("\nStudent not found.")

    connection.close()