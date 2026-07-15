from enum import Enum
from datetime import datetime

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"

class TransactionRecord:
    def __init__(self, transaction_type: TransactionType, amount: float):
        self.transaction_type = transaction_type
        self.amount = amount

        self.timestamp = datetime.now().strftime("%Y-%m-%d")
    
    def __str__(self):
        return f"[{self.transaction_type.value.upper()}] ${self.amount:,.2f} on {self.timestamp}"
    
    @classmethod
    def from_dict(cls, data):
        record = cls(
            transaction_type = TransactionType(data['transaction_type']),
            amount = data['amount']
        )
        record.timestamp = data['timestamp']
        return record
    
    def to_dict(self):
        return {
            'transaction_type': self.transaction_type.value,
            'amount': self.amount,
            'timestamp': self.timestamp
        }