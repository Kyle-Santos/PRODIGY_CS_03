import re

def main():
    password = input("Enter your password: ")
    result = assess_password_complexity(password.strip())
    print("\n" + result)

def assess_password_complexity(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Character diversity check
    if not re.search(r'[a-z]', password) or \
       not re.search(r'[A-Z]', password) or \
       not re.search(r'\d', password) or \
       not re.search(r'[^a-zA-Z0-9]', password):
        return "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."

    # Open the common password patterns txt file for reading
    with open('100k-most-used-passwords-NCSC.txt', 'r') as file:
        # Read all lines from the file and store them in a list
        common_patterns = file.readlines()

    # Avoid common patterns or dictionary words
    if password.lower() in common_patterns:
        return "Password is too common or easily guessable."

    # Password meets complexity requirements
    return "Password complexity is sufficient."


if __name__ == "__main__":
    main()