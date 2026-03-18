import re

def password_strength_checker(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make your password at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    # Check for symbols
    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        suggestions.append("Add at least one special character (e.g., @$!%*?&).")

    return score, suggestions

# Example usage
password = input("Enter your password: ")
score, suggestions = password_strength_checker(password)

print(f"Password Strength Score: {score}/5")
if suggestions:
    print("Suggestions for improvement:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("Your password is strong!")


