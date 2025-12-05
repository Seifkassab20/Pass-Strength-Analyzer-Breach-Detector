import random
import string

def generate_password(length=16, use_upper=True, use_lower=True,
                      use_numbers=True, use_symbols=True):
    
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    allowed_chars = ""

    if use_upper:
        allowed_chars += upper
    if use_lower:
        allowed_chars += lower
    if use_numbers:
        allowed_chars += numbers
    if use_symbols:
        allowed_chars += symbols

    if not allowed_chars:
        raise ValueError("At least one character set must be enabled.")

    password = "".join(random.choice(allowed_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generated Strong Password:")
    print(generate_password(length=18, use_symbols=True, use_numbers=True))
