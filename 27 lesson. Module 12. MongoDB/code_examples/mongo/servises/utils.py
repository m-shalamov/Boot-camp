from data.bookings import Bookings
from data.cages import Cages
from data.people import People
from data.spyders import Spyders


def create_account(name, email):
    user = People()
    user.name = name
    user.email = email

    user.save()
    return user


def find_by_email(email):
    return People.objects().filter(email=email).first()

def show_cages(active_account):
    cages = list(Cages.objects(id__in = active_account.cages_ids))
    return cages


def add_cage(active_account, name, price, size, allow_venomous):
    cage = Cages()
    cage.name = name
    cage.size = size
    cage.allow_venomous = allow_venomous
    cage.price = price
    
    cage.save()
    
    active_account.cages_ids.append(cage.id)
    active_account.save()
    return cage