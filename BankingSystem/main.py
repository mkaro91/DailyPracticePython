from Classes import Bank, BankAccount
from Services import *

from helpers import *

def main():
    bank = Bank()

    while True:
        program_title("Seerious Banking")

        print("\n1. Create Account")
        print("2. Delete Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. View Account")
        print("7. Transaction History")
        print("0. Exit")

        choice = menu_choice()
        match choice:
            case "0": 
                bank.save_accounts()
                break

            case "1": create_account(bank)
            case "2": delete_account(bank)
            case "3": deposit(bank)
            case "4": withdraw(bank)
            case "5": transfer(bank)
            case "6": account_information(bank)
            case "7": transaction_history(bank)

            case _:
                print("Invalid choice.")
                press_enter()



if __name__ == "__main__":
    main()