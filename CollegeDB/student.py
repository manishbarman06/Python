from database import con, cursor

def add_student():
    try:
        name = input("Enter name: ")
        email = input("Enter email: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        query = """
        INSERT INTO students (name, email, age, course)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, email, age, course)

        cursor.execute(query, values)
        con.commit()

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        for student in students:
            print(student)

    except ValueError:
        print("ERROR: Invalid value!")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__=="__main__":
    add_student()