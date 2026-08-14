import hashlib
from database import con, cursor

# Function to convert password into hash password 
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function for Registration
def register():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    hashed_password = hash_password(password)

    query = """
    INSERT INTO users (username, email, password)
    VALUES (%s, %s, %s)
    """

    values = (username, email, hashed_password)

    try:
        cursor.execute(query, values)
        con.commit()

        print("\nRegistration Successful!")

    except Exception as e:
        print(f"\nRegistration Failed: {e}")

    finally:
        cursor.close()
        con.close()


# Function for Login 
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed_password = hash_password(password)

    query = """
    SELECT id, username FROM users
    WHERE username = %s AND password = %s
    """

    values = (username, hashed_password)

    cursor.execute(query, values)
    
    user = cursor.fetchone()

    if user:
        print(f"\nLogin Successful! WELCOME, {user[1]}")
    else:
        print("\nInvalid username or password!")

    cursor.close()
    con.close()

