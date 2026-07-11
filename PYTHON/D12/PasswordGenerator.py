import random
import string

def generate_password(length=12):
    # Combine all characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the combined pool
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Generate a password
if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print(f"Your password is: {generate_password(length)}")