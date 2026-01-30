class Customer:
    Bank_Name = "HFC BANK"
    IFSC = "HFC000567"
    BRANCH = "AMEERPET"
    STATE = "TG"

    # how can we create object attributes?
    """
    Before creating the object attributes we need to initialize
    the object attributes inside the class
    """

    def __init__(self, Name, Balance, account_number, address):
        self.Name = Name
        self.Balance = Balance
        self.account_number = account_number
        self.address = address

    # create a method to welcome a customer into bank
    def welcome_wish(self):
        return f"Hello {self.Name}! Welcome to {self.Bank_Name}, {self.BRANCH}, {self.STATE}"

    # create a method to check the balance
    def check_balance(self):
        return f"Hello {self.Name}! Your current balance is {self.Balance}/-"

    # create a method to deposit the amount
    def deposit(self, amount):
        self.Balance = self.Balance + amount
        return f"""Your transaction is successful
Your account has been credited with {amount}/-
Your updated balance is {self.Balance}/-."""

    # create a method to withdraw the amount
    def withdraw(self, amount):
        if amount <= self.Balance:
            self.Balance = self.Balance - amount
            return f"""Your transaction is successful
Your account has been debited with {amount}/-
Your updated balance is {self.Balance}/-."""
        else:
            return "Insufficient funds, please check your balance"
c1 = Customer("Candy", 15000, 6345736, "Ameerpet, Hyderabad")
c2 = Customer("Rix", 10000, 3476387, "Hyderabad")
print(c1.IFSC)
print(c2.BRANCH)
print(c1.Balance)
print(c2.account_number)
print(c1.welcome_wish())
print(c1.check_balance())
print(c1.deposit(10000))
print(c2.withdraw(25000))
