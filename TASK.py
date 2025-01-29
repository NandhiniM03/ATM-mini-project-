class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter a new account number: ")
        if account_number in self.accounts:
            print("Account number already exists. try again.")
            return
        pin = input("Set a 4-digit PIN: ")
        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN format.  enter a 4-digit number.")
            return
        self.accounts[account_number] = Account(account_number, pin)
        print("Account created successfully.")
        self.main_menu()

    def login(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            print("Login successful.")
            self.account_menu(account)
        else:
            print("Invalid account number or PIN.")
            self.main_menu()

    def account_menu(self, account):
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            account.check_balance()
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '4':
            print("Logging out.")
            self.main_menu()
            return
        else:
            print("Invalid choice.  try again.")
        self.account_menu(account)

    def main_menu(self):
        print("\nWelcome to the ATM")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            self.create_account()
        elif choice == '2':
            self.login()
        elif choice == '3':
            print("Thank you for using the ATM.")
        else:
            print("Invalid choice.  try again.")
            self.main_menu()

if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()
