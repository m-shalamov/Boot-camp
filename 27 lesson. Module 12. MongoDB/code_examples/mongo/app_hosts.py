import servises.utils as utils
import data.account as account


def run():
    print("Welcome host!")
    print()
    show_commands()
    while True:
        action = get_action()
        if action == "c":
            create_account()
        elif action == "l":
            login()
        elif action == "s":
            show_cages()
        elif action == "r":
            register_cage()
        elif action == "m":
            mode_change()
        elif action == "e":
            exit_program()
        elif action == "?":
            help_to_user()
        else:
            unknown_command()


def get_action():
    action = input("")
    return action


def show_commands():
    print("c - create an account")
    print("l - login")
    print("s - show your cages")
    print("r - register your cage")
    print("m - mode change")
    print("e - exit")
    print("? - help")
    print()


def create_account():
    print("REGISTRATION")
    name = input("Your name: ")
    email = input("Your email: ")
    old_account = utils.find_account_by_email(email)
    if old_account:
        print(f"Error. Account with {email} already exists")
        return
    user_account = utils.create_account(name, email)
    print(f"Success. Account with {email} was created")


def login():
    print("LOGIN")
    email = input("Your email: ")
    old_account = utils.find_account_by_email(email)
    if not old_account:
        print(f"Error. Could not find an account with {email}")
        return
    account.active_account = old_account
    print(f"Success. Logged in with {email}")


def show_cages():
    print("SHOW CAGES")
    if not account.active_account:
        print(f"Error. You should login")
        return
    cages = utils.find_cages_for_user(account.active_account)

    print(f"You have {len(cages)} cages")

    for cage in cages:
        print(cage)


def register_cage():
    print("REGISTER A CAGE")
    if not account.active_account:
        print(f"Error. You should login")
        return
    size = float(input("enter size of the cage: "))
    name = input("enter name of the cage: ")
    price = float(input("enter price of the cage: "))
    allow_venomous_spyders = input("can venomous spyders live in this cage [y], [n]: ")
    cage = utils.register_cage(
        account.active_account, name, size, price, allow_venomous_spyders
    )
    account.reload_account()
    print("Success. The cage was created")


def mode_change():
    pass


def exit_program():
    print("GOOD BYE!")
    raise KeyboardInterrupt()


def help_to_user():
    show_commands()


def unknown_command():
    print(
        "Error. Unfortunately we do not understand your command. Please try one more time"
    )
