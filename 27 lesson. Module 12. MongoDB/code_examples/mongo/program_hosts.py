import servises.state as state
import servises.utils as utils


def run():
    show_options()
    while True:
        option = choose_option()
        if option == "c":
            create_account()
        elif option == "l":
            login()
        elif option == "s":
            show_cages()
        elif option == "a":
            add_cage()
        elif option == "v":
            view_bookings()
        elif option == "m":
            change_mode()
        elif option == "e":
            exit_app()


def show_options():
    print("c - create an account")
    print("l - login")
    print("s - show your cages")
    print("a - add a cage")
    print("v - view your bookings")
    print("m - change the mode")
    print("e - exit")


def choose_option():
    option = input()
    return option


def create_account():
    print("REGISTRATION")
    name = input("Name? ")
    email = input("Email? ")
    user = utils.find_by_email(email)
    if user:
        print(f"Choose another email")
        return
    state.active_account = utils.create_account(name, email)
    print(f"Account was created")


def login():
    print("LOGIN")
    email = input("Email? ")
    user = utils.find_by_email(email)
    if not user:
        print(f"Wrong email")
        return
    state.active_account = user
    print(f"You have been logged in")


def show_cages():
    print("LIST OF CAGES")
    if not state.active_account:
        print("You must login")
        return
    cages = utils.show_cages(state.active_account)
    for cage in cages:
        print(cage.name, cage.price, cage.size)


def add_cage():
    print("ADD CAGE")
    if not state.active_account:
        print("You must login")
        return
    name = input("Enter your cage name")
    price = float(input("Enter the price per night"))
    size = float(input("Enter the size in square cm"))
    allow_venomous = input("Can venoumus spyders live? [y], [n]")

    cage = utils.add_cage(state.active_account, name, price, size, allow_venomous)
    print("Your cage has been added")

def view_bookings():
    pass


def change_mode():
    pass


def exit_app():
    pass
