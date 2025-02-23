import random
import string

def generate_random_password(length=8):
    """Generate a random password of specified length."""
    characters = string.digits + string.ascii_letters + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 12  # Set desired password length here
    password = generate_random_password(password_length)
    print("Your random password is:", password)
