import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    input("\n\nPress <ENTER> to continue...")

def collect_non_blank(prompt):
    while True:
        value = input(prompt).strip()
        if value: return value
        print("Input cannot be blank.")

def collect_number(prompt, is_float=False):
    value_type = float if is_float else int

    while True:
        try:
            return value_type(collect_non_blank(prompt))
        except ValueError:
            print("Please enter a valid number.")

def menu_choice():
    return input("\nEnter choice: ").strip()

def prep_screen(title):
    clear_screen()
    print(f"=== {title} ===")