                                                #   Simple LogIn System
                                            
# Simple File-Based Login System

def load_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass
    return users


def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")


def signup(users):
    print("\n--- SIGN UP ---")
    username = input("Choose username: ").strip()

    if username in users:
        print("Username already exists.")
        return

    password = input("Choose password: ").strip()

    save_user(username, password)
    users[username] = password
    print("Account created successfully!")


def login(users):
    print("\n--- LOGIN ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username] == password:
        print("Login successful! 🎉")
    else:
        print("Invalid username or password.")


# -------- MAIN PROGRAM --------
users = load_users()

while True:
    print("\n1. Sign Up")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        signup(users)
    elif choice == "2":
        login(users)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
