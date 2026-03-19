import logging
import os

# ---------------- LOGGING ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)

USER_FILE = "12_users.txt"


# ---------------- FILE UTILITIES ----------------
def load_users():
    users = {}
    if not os.path.exists(USER_FILE):
        return users

    with open(USER_FILE, "r") as file:
        for line in file:
            username, password, balance = line.strip().split("\n")
            users[username] = {
                "password": password,
                "balance": float(balance)
            }
    return users


def save_users(users):
    with open(USER_FILE, "w") as file:
        for username, data in users.items():
            file.write(f"{username},{data['password']},{data['balance']}\n")


# ---------------- ATM CLASS ----------------
class ATM:
    def __init__(self, username, users):
        self.username = username
        self.users = users

    def check_balance(self):
        return self.users[self.username]["balance"]

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.users[self.username]["balance"] += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        if amount > self.users[self.username]["balance"]:
            raise ValueError("Insufficient funds")
        self.users[self.username]["balance"] -= amount


# ---------------- AUTH SYSTEM ----------------
def signup(users):
    print("\n--- SIGN UP ---")
    username = input("Choose username: ")

    if username in users:
        print("Username already exists.")
        return None

    password = input("Choose password: ")
    users[username] = {
        "password": password,
        "balance": 1000.0
    }

    save_users(users)
    print("Account created successfully!")
    return username


def login(users):
    print("\n--- LOGIN ---")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return username

    print("Invalid username or password.")
    return None


# ---------------- MAIN APP ----------------
def main():
    users = load_users()

    while True:
        print("\n1. Sign Up")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            user = signup(users)
        elif choice == "2":
            user = login(users)
        elif choice == "3":
            break
        else:
            print("Invalid choice")
            continue

        if user:
            atm = ATM(user, users)

            while True:
                print("\n--- ATM MENU ---")
                print("1. Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")

                try:
                    opt = int(input("Enter option: "))

                    if opt == 1:
                        print("Balance:", atm.check_balance())

                    elif opt == 2:
                        amt = float(input("Deposit amount: "))
                        atm.deposit(amt)
                        save_users(users)
                        print("Deposit successful")

                    elif opt == 3:
                        amt = float(input("Withdraw amount: "))
                        atm.withdraw(amt)
                        save_users(users)
                        print("Withdrawal successful")

                    elif opt == 4:
                        print("Logged out.")
                        break

                    else:
                        print("Invalid option")

                except ValueError as e:
                    logging.error(e)
                    print("Error:", e)


if __name__ == "__main__":
    main()
