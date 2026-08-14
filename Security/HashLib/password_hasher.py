import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

if __name__=="__main__":
    password = "Strong@Password!123"

    hashed_password = hash_password(password)

    print(f"Hashed Password: {hashed_password}")
