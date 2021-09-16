import data.mongo_setup as mongo_setup
import app_hosts
import app_guests

def main():
    mongo_setup.global_init()
    try:
        while True:
            if user_choice() == "g":
                app_guests.run()
            else:
                app_hosts.run()
    except KeyboardInterrupt:
        return

def user_choice():
    print("type [g] - for guests")
    print("type [h] - for hosts")
    print()
    choice = input()
    return choice

if __name__ == "__main__":
    main()