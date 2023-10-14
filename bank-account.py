from enum import Enum, auto

class TransactionTypes(Enum):
    DEPOSIT = auto()
    WITHDRAWAL = auto()
    TRANSFER = auto()

Transactions = tuple[TransactionTypes, int]

class BankAccount:
    def __init__(self, initial_balance: int = 0) -> None:
        self._balance: int = initial_balance
        self._transaction_history: list[Transactions] = []
    
    def deposit(self, amount: int) -> None:
        self._balance += amount
        self._transaction_history.append((TransactionTypes.DEPOSIT, amount))
        pass
    
    def withdraw(self, amount: int) -> None:
        if not self._sufficient_balance(amount):
            raise {"Error": "Not enough funds"}
        self._balance -= amount
        self._transaction_history.append((TransactionTypes.WITHDRAWAL, amount))

    def transfer(self, other, amount: int) -> None:
        if not self._sufficient_balance(amount):
            raise {"Error": "Not enough funds"}
        
        self._balance -= amount
        other._balance += amount
        self._transaction_history.append((TransactionTypes.TRANSFER, amount))
    
    def _sufficient_balance(self, amount: int):
        return amount <= self._balance
    
    @property
    def balance(self) -> int:
        return self._balance

    @property
    def transaction_history(self) -> list[Transactions]:
        return self._transaction_history


account1 = BankAccount(200)
account2 = BankAccount(500)
account1.deposit(300)
print(account1._balance)
account1.withdraw(125)
account1.transfer(account2, 20)
print(account2._balance)
print(account1.transaction_history)