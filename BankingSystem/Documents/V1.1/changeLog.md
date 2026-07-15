# Change Log V1.1

## Save Accounts
- When User Exits
    - Save account to file

- When Program Starts
    - Load accounts

- Changes
    - Added to_dict and from_dict to Bank Account and Transaction Record
    - Accounts auto load on program startup
    - Auto Save on Program Exit
    - Accounts are no saved in a list in the bank class instead of dictionaries
        - Increases lookup time but is simplier for persistence

## Delete Account
- Add a new menu option to delete an account
- Requirements:
    - R1: Ask for account number
    - R2: Confirm before deletion
    - R3: Remove account

- Changes
    - Added delete account as a menu option
    - Added delete account function to Bank class
    - Added delete account function in bank services

## Transfer Money Between Accounts (C3)
- Add a new menu option to transfer money between accounts
- Requirements:
    - R1: Ask for sender account
    - R2: Ask for receiver account
    - R3: Ask for amount
    - R4: Update both accounts
    - R5: Record transaction in both accounts
- Validate:
    - V1: Both accounts exist
    - V2: Sender has enough money

Changes:
    - Added Transfer menu option
    - Add Transfer value to TransactionType Enum
    - Added transfer method to BankAccount class
    - Added transfer method to Bank class
    - added transfer method to bank services

## Transaction Timestamps
- Feature was included in V1.0

## Better Account Numbers
- Feature was included in V1.0

## Formatting
- Was included in V1.0