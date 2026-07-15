from Classes.bank_account import BankAccount

import json
import os

class Bank:
    def __init__(self):
        self.accounts = self.load_accounts() # {Account Number: Account}
    
    def find_account_by_number(self, account_number) -> BankAccount:
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    
    def create_account(self, account: BankAccount):
        if self.find_account_by_number(account.account_number) is not None: return

        self.accounts.append(account)
    
    def delete_account(self, account: BankAccount):
        if self.find_account_by_number(account) is None: return

        self.accounts.remove(account)
    
    def transfer(self, sender: BankAccount, receiver: BankAccount, amount: float):
        if sender not in self.accounts: return False, "Invalid Sender account."
        if receiver not in self.accounts: return False, "Invalid receiver account."

        return sender.transfer(receiver, amount)
    
    def load_accounts(self):
        try:
            with open("Data/accounts.json", 'r') as f:
                return [BankAccount.from_dict(account) for account in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_accounts(self):
        os.makedirs('Data', exist_ok=True)
        data = [account.to_dict() for account in self.accounts]

        with open('Data/accounts.json', 'w') as f:
            json.dump(data, f, indent=2)

    
