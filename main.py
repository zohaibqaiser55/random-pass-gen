import random
import string

def generate_password():
    # Define the number of each type of character
    num_digits = 3
    num_special_chars = 2
    total_length = 14
    num_letters = total_length - num_digits - num_special_chars

    # Generate the required characters
    digits = ''.join(random.choice(string.digits) for _ in range(num_digits))
    special_chars = ''.join(random.choice(string.punctuation) for _ in range(num_special_chars))
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(num_letters))

    # Combine all characters
    password = digits + special_chars + letters

    # Convert the password to a list and shuffle it to ensure randomness
    password_list = list(password)
    random.shuffle(password_list)

    # Convert the list back to a string
    final_password = ''.join(password_list)
    
    return final_password

# Generate and print a random password
print(generate_password())