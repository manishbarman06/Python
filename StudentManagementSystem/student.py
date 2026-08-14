from database import conn, cursor

# Function to Add Student
def add_student():
    try:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ").strip()
        age = int(input("Enter age: "))
        course = input("Enter course: ").strip()
        phone = input("Enter phone number: ").strip()
        gender = input("Enter gender: ").strip()

        sql = """
        INSERT INTO students (roll, name, age, course, phone, gender)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (roll, name, age, course, phone, gender)

        cursor.execute(sql, values)
        conn.commit()
        print("\n✅ Student Added Successfully!")

    except ValueError:
        print("⚠️ ERROR: Roll number and age must be numbers.")
    except Exception as err:
        print(f"❌ Database Error: {err}")


# Function to View Students
def view_students():
    sql = "SELECT id, roll, name, age, course, phone, gender FROM students"
    cursor.execute(sql)
    students = cursor.fetchall()

    if not students:
        print("⚠️ No records found.")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<5} {'Roll':<8} {'Name':<18} {'Age':<5} {'Course':<10} {'Phone':<12} {'Gender':<8}")
    print("-" * 70)

    for student in students:
        id_val, roll, name, age, course, phone, gender = student
        print(f"{id_val:<5} {roll:<8} {name:<18} {age:<5} {course:<10} {phone:<12} {gender:<8}")
    print("=" * 70)


# Function to Search Student
def search_student():
    try:
        roll = int(input("Enter roll number to search: "))

        sql = "SELECT id, roll, name, age, course, phone, gender FROM students WHERE roll = %s"
        cursor.execute(sql, (roll,))
        student = cursor.fetchone()

        if student:
            print("\n--- Student Details ---")
            print(f"ID     : {student[0]}")
            print(f"Roll   : {student[1]}")
            print(f"Name   : {student[2]}")
            print(f"Age    : {student[3]}")
            print(f"Course : {student[4]}")
            print(f"Phone  : {student[5]}")
            print(f"Gender : {student[6]}")
        else:
            print("❌ Student Not Found!")

    except ValueError:
        print("⚠️ ERROR: Roll number must be a number.")


# Function to Update Student
def update_student():
    try:
        roll = int(input("Enter roll number to update: "))

        sql = "SELECT * FROM students WHERE roll = %s"
        cursor.execute(sql, (roll,))
        student = cursor.fetchone()

        if not student:
            print("❌ Student Not Found!")
            return

        name = input("New Name: ").strip()
        age = int(input("New Age: "))
        course = input("New Course: ").strip()
        phone = input("New Phone: ").strip()
        gender = input("New Gender: ").strip()

        sql_update = """
        UPDATE students
        SET name = %s, age = %s, course = %s, phone = %s, gender = %s
        WHERE roll = %s
        """
        values = (name, age, course, phone, gender, roll)

        cursor.execute(sql_update, values)
        conn.commit()
        print("✅ Student Updated Successfully!")

    except ValueError:
        print("⚠️ ERROR: Invalid value! Age and Roll must be integers.")


# Function to Delete Student
def delete_student():
    try:
        roll = int(input("Enter roll number to delete: "))

        sql = "DELETE FROM students WHERE roll = %s"
        cursor.execute(sql, (roll,))
        conn.commit()

        if cursor.rowcount > 0:
            print("✅ Student Deleted Successfully!")
        else:
            print("❌ Student Not Found!")

    except ValueError:
        print("⚠️ ERROR: Roll number must be a number.")