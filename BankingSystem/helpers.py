import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    input("\n\nPress <ENTER> to continue..")

def program_title(title):
    clear_screen()
    print(f"===== {title.title()} =====")

def screen_title(title):
    clear_screen()
    print(f"=== {title.title()} ===")

def menu_choice():
    return input("Enter choice: ")

def collect_non_blank(prompt):
    while True:
        value = input(prompt).strip()
        if value: return value
        print("Input cannot be blank.")

def collect_number(prompt, is_float=False):
    value_type = float if is_float else int

    while True:
        try:
            return value_type(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")

def check_empty(object, empty_msg):
    if not object:
        print(empty_msg)
        press_enter()
        return True
    return False

def confirm(prompt):
    while True:
        value = collect_non_blank(prompt).lower()
        if value in ['y', 'n']: return True if value == 'y' else False
        print("Enter 'y' for yes or 'n' for no.")
