import random
import string

def generate_password(length, use_digits=True, use_special=True):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter password length: "))
digits = input("Include digits? (yes/no): ").lower() == "yes"
special = input("Include special characters? (yes/no): ").lower() == "yes"

password = generate_password(length, digits, special)

print("\nGenerated Password:", password)