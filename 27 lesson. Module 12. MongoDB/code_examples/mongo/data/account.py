import servises.utils as utils

active_account = None

def reload_account():
    global active_account
    if not active_account:
        return
    active_account = utils.find_account_by_email(active_account.email)