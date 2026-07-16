from Classes import Bank, BankAccount

from helpers import *

def _find_account(bank: Bank, prompt = "\nAccount Number: "):
    account_number = collect_number(prompt)
    return bank.find_account_by_number(account_number)

def _account_not_found(account):
    return check_empty(account, "No account with matching account number found.")

def _collect_amount(prompt, invalid_msg):
    while True:
        value = collect_number(prompt, is_float=True)
        if value >= 0: return value
        print(invalid_msg)

def _generate_account_number(bank: Bank):
    if not bank.accounts:
        return 1001
    return bank.accounts[-1].account_number + 1

def _new_balance(account: BankAccount):
    print(f"New Balance: ${account.get_balance():,.2f}")

def _pin_entry(account: BankAccount):
    if account.is_locked:
        print("Account is locked. Please contact adminastrator to unlock.")
        return
    
    incorrect_count = 0

    while True:
        pin = collect_non_blank("PIN: ")
        if account.check_pin(pin):
            break
        print("Incorrect PIN.")
        incorrect_count += 1

        if incorrect_count == 3:
            account.is_locked = True
            print("Account has been locked due to incorrect PIN attempts.")
            break

def create_account(bank: Bank):
    screen_title("Create Account")

    account_holder = collect_non_blank("\nName: ").title()

    while True:
        # Using collect number ensures only numeric values will be used in the PIN
        pin = collect_number("4-Digit PIN: ")
        if len(str(pin)) == 4: break
        print("PIN must be 4 digits.")

    starting_balance = _collect_amount("Starting Balance: ", "Initial balance cannot be below zero.")
    account_number = _generate_account_number(bank)
    
    bank.create_account(BankAccount(account_holder, account_number, str(pin), starting_balance))

    print("\nAccount created!")
    print("Account Number:", account_number)

    press_enter()

# V1.1
def delete_account(bank: Bank):
    screen_title("Delete Account")

    # V1.1 Delete Account R1
    account = _find_account(bank)
    if _account_not_found(account):
        return
    
    # V1.2 Require PIN for Account Deletion
    _pin_entry(account)
    if account.is_locked:
        return
    
    # V1.1 Delete Account R2
    if confirm(f"Are you sure you wish to delete account {account.account_number}: "):
        # V1.1 Delete Account R3
        bank.delete_account(account)
        print(f"Account {account.account_number} was removed.")
    else:
        print("No changes made.")
    
    press_enter()

def deposit(bank: Bank):
    screen_title("Deposit")
    
    account = _find_account(bank)
    if _account_not_found(account):
        return
    
    # V1.2 Require PIN for Deposit
    _pin_entry(account)
    if account.is_locked:
        return
    
    amount = _collect_amount("Amount: ", "Deposit amount cannot be less than zero.")
    result, msg = account.deposit(amount)
    if check_empty(result, msg):
        return

    print(msg)
    _new_balance(account)

    press_enter()


def withdraw(bank: Bank):
    screen_title("Withdraw")

    account = _find_account(bank)
    if _account_not_found(account):
        return
    
    # V1.2 Require PIN for Withdraw
    _pin_entry(account)
    if account.is_locked:
        return
    
    amount = _collect_amount("Amount: ", "Withdraw amount cannot be less than zero.")
    result, msg = account.withdraw(amount)
    if check_empty(result, msg):
        return

    print(msg)     
    _new_balance(account)
    
    press_enter()

def transfer(bank: Bank):
    screen_title("Transfer Between Accounts")
    
    # V1.1 C3 R1: Ask for sender account
    sender = _find_account(bank, prompt="\nEnter Sender's Account Number: ")

    # V1.1 C3 R2: Ask for receiver account
    receiver = _find_account(bank, prompt="\nEnter Destination Account Number: ")
    
    # V1.1 C3 V1: Validate both accounts exist
    if _account_not_found(sender) or _account_not_found(receiver):
        return
    
    # V1.2 Require PIN for Transfer
    _pin_entry(sender)
    if sender.is_locked:
        return
    
    # V1.1 C3 R4: Ask for amount
    amount = _collect_amount("Transfer Amount: ", "Transfer amount cannot be less than zero.")

    result, msg = bank.transfer(sender, receiver, amount)
    if check_empty(result, msg):
        return
    
    print(msg)
    _new_balance(sender)
    
    press_enter()


def account_information(bank: Bank):
    screen_title("Account Information")

    account = _find_account(bank)
    if _account_not_found(account):
        return
    
    # V1.2 Require PIN for viewing account Information
    _pin_entry(account)
    if account.is_locked:
        return
    
    print("\n".join(account.account_information()))
    press_enter()

def transaction_history(bank):
    screen_title("Transaction History")

    account = _find_account(bank)
    if _account_not_found(account): 
        return
    
    # V1.2 Require PIN for view account history
    history = account.get_transaction_history()
    if check_empty(history, "No transaction history."):
        return
    
    print("\n".join(history))
    press_enter()