import random
import string

while True:

    # Password length
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    # Character type selection
    print("\nChoose character types:")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$...)")

    choices = input("Enter choices (example: 123): ")

    # Remove duplicate choices
    choices = set(choices)

    # Validate choices
    valid_choices = {"1", "2", "3", "4"}

    if not choices.issubset(valid_choices):
        print("Invalid choice. Please choose only 1, 2, 3, or 4.")
        continue

    if len(choices) < 2:
        print("Please select at least 2 character types.")
        continue

    # Character pool
    characters = ""

    if "1" in choices:
        characters += string.ascii_uppercase

    if "2" in choices:
        characters += string.ascii_lowercase

    if "3" in choices:
        characters += string.digits

    if "4" in choices:
        characters += string.punctuation

    # Generate password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    # Display password
    print("\nGenerated Password:", password)

    # Generate another password
    again = input("\nGenerate another password? (y/n): ")

    if again.lower() != "y":
        print("Thank you for using the Password Generator!")
        breakgi