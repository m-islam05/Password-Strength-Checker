# Password Checker v3
# Evaluates password strength based on length, character types, and content

def check_password_strength(password):
    """Check password strength and print a score and rating."""
    score = 0

    # Check if password length is at least 8 characters
    if len(password) >= 8:
        score += 1

    # Check for lowercase letters
    has_lowercase = any(char.islower() for char in password)
    if has_lowercase:
        score += 1

    # Check for uppercase letters
    has_uppercase = any(char.isupper() for char in password)
    if has_uppercase:
        score += 1

    # Check for digits
    has_digit = any(char.isdigit() for char in password)
    if has_digit:
        score += 1

    # Check for special characters
    special_characters = "!@#$%^&*()_+={}[]|:;'<>,.?/~`"
    has_special = any(char in special_characters for char in password)
    if has_special:
        score += 1

    # Check that 'password' is not in the password (case-insensitive)
    if 'password' not in password.lower():
        score += 1

    # Print the score and strength
    print("Password Strength Score:", score, "/6")
    
    if score <= 2:
        print("Weak password")
    elif score <= 4:
        print("Moderate password")
    else:
        print("Strong password")

# ---------------- MAIN ---------------- #

password_input = input("Enter a password: ").strip()
check_password_strength(password_input)
