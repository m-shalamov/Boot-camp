from data.bookings import Bookings
from data.cages import Cages
from data.people import People
from data.spyders import Spyders


def find_account_by_email(email):
    user = People.objects(email=email).first()
    return user


def create_account(name, email):
    user = People()
    user.name = name
    user.email = email
    user.save()
    return user

def register_cage(active_account, name, size, price, allow_venomous_spyders):
    cage = Cages()
    cage.name = name
    cage.price = price
    cage.size = size
    cage.allow_venomous_spyders = allow_venomous_spyders
    cage.save()
    account = find_account_by_email(active_account.email)
    account.cage_ids.append(cage.id)
    account.save()
    return cage
    
def find_cages_for_user(active_account):
    cages = list(Cages.objects(id__in = active_account.cage_ids))
    return cages