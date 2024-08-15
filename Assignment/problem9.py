'''
Write a Python class BankAccount with attributes like accountNumber, openingBalance, currentBalance dateOfOpening and customerName. Add methods like deposit, withdraw, and checkBalance.

'''

from datetime import datetime

class BankAccount:
    def __init__(self, account_number: str, customer_name: str, opening_balance: float):
        self.account_number = account_number
        self.customer_name = customer_name
        self.opening_balance = opening_balance
        self.current_balance = opening_balance
        self.date_of_opening = datetime.now()  # Store the datetime object

    def deposit(self, amount: float):
        if amount > 0:
            self.current_balance += amount
            print(f'Deposited: ${amount:.2f}')
        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount: float):
        if amount > 0:
            if amount <= self.current_balance:
                self.current_balance -= amount
                print(f'Withdrawn: ${amount:.2f}')
            else:
                print('Insufficient funds.')
        else:
            print('Withdrawal amount must be positive.')

    def check_balance(self) -> float:
        print(f'Current balance: ${self.current_balance:.2f}')
        return self.current_balance

    def get_formatted_opening_date(self) -> str:
        # Format the date when needed
        return self.date_of_opening

    def __str__(self):
        return (f'Account Number: {self.account_number}\n'
                f'Customer Name: {self.customer_name}\n'
                f'Opening Balance: ${self.opening_balance:.2f}\n'
                f'Current Balance: ${self.current_balance:.2f}\n'
                f'Date of Opening: {self.get_formatted_opening_date()}')

# Example usage
account = BankAccount("37634934", "Zul the Great", 2345.0)
print(account)

account.deposit(600.0)
account.withdraw(100.0)
account.check_balance()

print(account)
