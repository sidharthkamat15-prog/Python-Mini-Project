import random
import string


# 🔐 Password Generator


def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation 
    password  = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter desired password length: "))
password = generate_password()
print(f"Generated Password:\n -----{password}-----")    
print("Thanks for using the Password Generator!")

