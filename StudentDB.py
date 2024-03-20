# Tadg O'Hare 101198108
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
host = "localhost"
database = "student_a3"
user = "postgres"
password = os.getenv('DB_PASSWORD')

def connect_to_db():
    """Connects to the PostgreSQL database and returns the connection object"""
    try:
        connection = psycopg2.connect(host=host, database=database, user=user, password=password)
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL database:", error)
        return None

def get_all_students():
    """Retrieves all student records and returns them as a list"""
    connection = connect_to_db()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()  # Fetch all results
        return students
    except (Exception, psycopg2.Error) as error:
        print("Error retrieving students:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
    return None

def add_student(first_name, last_name, email, enrollment_date):
    """Inserts a new student record into the database"""
    connection = connect_to_db()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        insert_query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (first_name, last_name, email, enrollment_date))
        connection.commit()  # Save changes
        print("Student added successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error adding student:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

def update_student_email(student_id, new_email):
    """Updates the email address for a student with the specified student_id"""
    connection = connect_to_db()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        update_query = "UPDATE students SET email = %s WHERE student_id = %s"
        cursor.execute(update_query, (new_email, student_id))
        connection.commit()
        print("Student email updated successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error updating student email:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

def delete_student(student_id):
    """Deletes the record of the student with the specified student_id"""
    connection = connect_to_db()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        delete_query = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(delete_query, (student_id,))
        connection.commit()
        print("Student deleted successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error deleting student:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

def populate_students():
    """Populates the students table with initial data"""
    students = [
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
    ]
    connection = connect_to_db()
    if not connection:
        return None
    cursor = connection.cursor()
    try:
        insert_query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
        cursor.executemany(insert_query, students)
        connection.commit()  # Save changes
        print("Students added successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error adding students:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

def get_input():
    while True:
        command = input("Enter a command (or 'exit' to quit), run 'help' for a list of commands: ")
        if command.lower() == 'exit':
            break
        elif command.lower() == 'help':
            get_help()
        elif command.lower() == 'add_student':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date: ")
            add_student(first_name, last_name, email, enrollment_date)
        elif command.lower() == 'get_all_students':
            students = get_all_students()
            if students:
                print("All Students:")
                for student in students:
                    print(student)
        elif command.lower() == 'populate_students':
            populate_students()
        elif command.lower() == 'update_student_email':
            student_id = input("Enter student id: ")
            new_email = input("Enter new email: ")
            update_student_email(student_id, new_email)
        elif command.lower() == 'delete_student':
            student_id = input("Enter student id: ")
            delete_student(student_id)
        else:
            print("Unknown command, run 'help' for a list of commands, or 'exit' to quit.")

def get_help():
    print("Available commands:")
    print("  exit - Quit the program")
    print("  add_student - Add a new student")
    print("  get_all_students - Display all students")
    print("  populate_students - Add initial students")
    print("  update_student_email - Update a student's email")
    print("  delete_student - Delete a student")
    print("  help - Display this help message")

def main():
    connect_to_db()
    get_input()


if __name__ == "__main__":
    main()