# Create account class with 2 attribute -balance and account no
# Create method for debit credit and printing the balance


class Bank:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.account_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("Amount debited")
        self.print_balance()

    def credit(self, amount):
        self.balance += amount
        print("Amount credited")
        self.print_balance()

    def print_balance(self):
        print(f"Total Balance is {self.balance}")


b1 = Bank(10000, 88300)
b1.debit(1000)
b1.credit(4000)
