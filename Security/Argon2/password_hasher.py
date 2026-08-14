from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Create a password hasher instance with secure defaults
ph = PasswordHasher()

""" Function to convert password into hash password """
def hash_password(password: str) -> str:
    """
    Hash a password using Argon2.
    """
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string.")
    else:
        return ph.hash(password)


""" Function to Verify Hashed Password """
def verify_password(hashed_password: str, plained_password: str) -> bool:
    """
    Verify a password against its hash.
    """
    try:
        return ph.verify(hashed_password, plained_password)
    except VerifyMismatchError:
        return False
    except Exception as e:
        print(f"Verification Error: {e}")
        return False


# Main 
if __name__=="__main__":
    password = "Strong@Password123"

    # Hashed Password
    hashed = hash_password(password)
    print(f"Hashed Password: {hashed}")

    # Verify Correct Password
    verify = verify_password(hashed, password)
    print(f"Pasword Match: {verify}")

    # Verify Incorrect Password
    verify = verify_password(hashed, "Wrong@Password123")
    print(f"Pasword Mismatch: {verify}")


