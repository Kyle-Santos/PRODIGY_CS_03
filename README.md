# PRODIGY_CS_03

## Password Complexity Checker | Prodigy InfoTech Internship
This Python script assesses the complexity of a user-provided password based on various criteria such as length, character diversity, and avoidance of common patterns or dictionary words.

### Usage

1. Ensure you have Python installed on your system.
2. Run the script by executing the following command in your terminal: 
    > python PasswordChecker.py
3. Enter your desired password.

### Password Complexity Criteria

- **Minimum Length Requirement**: Password must be at least 8 characters long.
- **Character Diversity**: Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
- **Avoidance of Common Patterns**: Password should not match common patterns or dictionary words to prevent easy guessing.

## Files

- `password_complexity_checker.py`: The main Python script that assesses password complexity.
- `100k-most-used-passwords-NCSC.txt`: A text file containing a list of common password patterns or dictionary words. 
from Danielmiessler. (n.d.). SecLists/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt at master · danielmiessler/SecLists. GitHub. https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt

## Dependencies

- `re` (Regular Expression library): Used for pattern matching in password assessment.

## Note

Make sure to replace the file path in the script (`100k-most-used-passwords-NCSC.txt`) with the appropriate path to the common password patterns file on your system.




