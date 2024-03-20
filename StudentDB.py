import psycopg2
from dotenv import load_dotenv
import os
# Database connection details (replace with your own)
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

# Example usage
# students = get_all_students()
# if students:
#     print("All Students:")
#     for student in students:
#         print(student)  # Output student data in a suitable format

# add_student("Alice", "Wonderland", "alice@wonderland.com", "2023-10-01")
# update_student_email(2, "jane.updated@example.com")
# delete_student(3)

def getInput():
    while True:
        command = input("Enter a command (or 'exit' to quit): ")
        if command.lower() == 'exit':
            break
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
        else:
            print("Unknown command")


def main():
    connect_to_db()
    getInput()


if __name__ == "__main__":
    main()