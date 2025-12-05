import re

def password_strength(password: str) -> dict:
    score = 0
    reasons = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        reasons.append("Password is too short (minimum 8 characters).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        reasons.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        reasons.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        reasons.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        reasons.append("Add special characters.")

    common_patterns = ["123", "password", "aaa", "111", "abc"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        reasons.append("Password contains common weak patterns.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "strength": strength,
        "score": score,
        "suggestions": reasons
    }

if __name__ == "__main__":
    pwd = input("Enter password to analyze: ")
    result = password_strength(pwd)
    print("\nStrength:", result["strength"])
    print("Score:", result["score"])
    print("Suggestions:")
    for s in result["suggestions"]:
        print("-", s)
