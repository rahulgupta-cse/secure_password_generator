#Simple Program to Generate Password According to user choice

import random # Importing random module to generate random characters
import string # Importing string module to access character sets

def generate_password(length, use_digits=True, use_special=True):
    characters = string.ascii_letters # Start with all uppercase and lowercase letters

    if use_digits:
        characters += string.digits # Add digits (0-9) if user wants digits
    if use_special:
        characters += string.punctuation  # Add special characters if user wants them


    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter password length: "))
digits = input("Include digits? (yes/no): ").lower() == "yes"
special = input("Include special characters? (yes/no): ").lower() == "yes"

password = generate_password(length, digits, special)

print("\nGenerated Password:", password)