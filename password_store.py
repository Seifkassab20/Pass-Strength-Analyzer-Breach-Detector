import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def store_password(hashed_password: str, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(hashed_password + "\n")

def verify_password(password: str, filename="passwords.txt") -> bool:
    hashed_input = hash_password(password)

    try:
        with open(filename, "r") as file:
            stored_hashes = file.read().splitlines()
    except FileNotFoundError:
        return False

    return hashed_input in stored_hashes


# Example usage
if __name__ == "__main__":
    pwd = input("Enter password to store: ")
    hashed = hash_password(pwd)
    store_password(hashed)
    print("Password hashed and stored securely!")
