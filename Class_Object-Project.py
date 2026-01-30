class Customer:
    Bank_Name = "RIX BANK"
    IFSC = "RIX69"
    BRANCH = "RIXOREA"
    STATE = "TG"

    def __init__(self, name, balance, account_number, address):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.address = address

    def welcome_wish(self):
        return f"Hello {self.name}! Welcome to {self.Bank_Name}, {self.BRANCH}, {self.STATE}"

    def check_balance(self):
        return f"Hello {self.name}! Your current balance is {self.balance}/-"

    def deposit(self, amount):
        self.balance += amount
        return f"""
Transaction Successful!
Amount Credited : {amount}/-
Updated Balance : {self.balance}/-
"""

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"""
Transaction Successful!
Amount Debited  : {amount}/-
Updated Balance : {self.balance}/-
"""
        else:
            return "❌ Insufficient funds. Please check your balance."
# Creating customers
c1 = Customer("Candy", 15000, 6345736, "Ameerpet, Hyderabad")
c2 = Customer("Rix", 10000, 3476387, "Hyderabad")

print(c1.welcome_wish())

while True:
    print("\n----- BANK MENU -----")
    print("1. Check Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(c1.check_balance())

    elif choice == 2:
        amt = int(input("Enter amount to deposit: "))
        print(c1.deposit(amt))

    elif choice == 3:
        amt = int(input("Enter amount to withdraw: "))
        print(c1.withdraw(amt))

    elif choice == 4:
        print("Thank you for banking with us ")
        break

    else:
        print("Invalid choice! Please try again.")

1