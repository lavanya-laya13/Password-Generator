# password_generator.py
import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password too short! Minimum length is 4."

    # Character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # At least one character from each category
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with random choices from all categories
    all_chars = upper + lower + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable order
    random.shuffle(password)

    return ''.join(password)

# --- Main Execution ---
if __name__ == "__main__":
    print("🔐 Password Generator")
    length = int(input("Enter password length (minimum 4): "))
    print("Generated Password:", generate_password(length))
