from Classes.transaction_record import TransactionRecord, TransactionType

class BankAccount:
    def __init__(self, account_holder, account_number, pin, starting_balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.pin = pin # 4-Digit PIN
        self.balance = starting_balance
        
        self.transaction_history: list[TransactionRecord] = []
        self.is_locked = False # Account is locked after 3 consecutive incorrect PIN entries 
    
    @classmethod
    def from_dict(cls, data):
        account = cls(
            account_holder = data['account_holder'],
            account_number = data['account_number'],
            pin = data['pin'],
            starting_balance = data['balance']
        )
        account.transaction_history = [TransactionRecord.from_dict(tr) for tr in data['transaction_history']]
        account.is_locked = data['is_locked']
        return account
    
    def to_dict(self):
        return {
            'account_holder': self.account_holder,
            'account_number': self.account_number,
            'pin': self.pin,
            'balance': self.balance,
            'transaction_history': [tr.to_dict() for tr in self.transaction_history],
            'is_locked': self.is_locked
        }

    def _add_transaction_log(self, transaction_type, amount):
        self.transaction_history.append(TransactionRecord(transaction_type, amount))
    
    def get_balance(self):
        return self.balance
    
    def check_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        if amount < 0: return False, "Invalid amount."
        
        self.balance += amount
        self._add_transaction_log(TransactionType.DEPOSIT, amount)
        return True, "Deposit complete."
    
    def withdraw(self, amount):
        if amount < 0: return False, "Invalid amount"
        if self.balance - amount < 0: return False, "Insufficent Funds"

        self.balance -= amount
        self._add_transaction_log(TransactionType.WITHDRAW, -amount)
        return True, "Withdraw complete."
    
    def transfer(self, other, amount):
        if amount < 0: return False, "Invalid amount"

        # V1.1 C3 V2: Validate sender has enough money
        if self.balance - amount < 0: return False, "Insufficient Balance"

        # V1.1 C3 R4
        # Update both accounts
        self.balance -= amount
        other.balance += amount

        # V1.1 C3 R5
        # Logs are made in each account
        self._add_transaction_log(TransactionType.TRANSFER, -amount)
        other._add_transaction_log(TransactionType.TRANSFER, amount)

        return True, "Transfer complete."
    
    def account_information(self):
        return  [
            f"\nAccount Holder: {self.account_holder}",
            f"Account Number: {self.account_number}",
            "",
            f"Balance: ${self.balance:,.2f}"
        ]
    
    def get_transaction_history(self):
        return [str(th) for th in self.transaction_history]