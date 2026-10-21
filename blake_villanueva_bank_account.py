class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._amount += amount
        else:
            print("Error: Deposit amount ain' t valid! Please enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive. No money?")
        elif amount > self._balance:
            print("Error: insufficient amount! Wala ka enough money!")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

account = BankAccount("Yza", 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())

            
