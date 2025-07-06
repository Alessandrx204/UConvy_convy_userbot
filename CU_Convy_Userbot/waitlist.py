# waitlist.py
import json
import os

WAITLIST_FILE = 'local_Uconvy_waitlist.json'
# Lista di tuple (chat_id, user_id, message_id) per serializzazione semplice
waitlist = []

def load_waitlist():
    global waitlist
    if os.path.exists(WAITLIST_FILE):
        with open(WAITLIST_FILE, 'r') as wl:
            waitlist = json.load(wl)
    else:
        waitlist = []

def save_waitlist():
    with open(WAITLIST_FILE, 'w') as wl:
        json.dump(waitlist, wl)

def add_user(chat_id, user_id, message_id):
    waitlist.append((chat_id, user_id, message_id))
    save_waitlist()

def remove_user(chat_id, user_id):
    for index, (cid, uid, _) in enumerate(waitlist):
        if cid == chat_id and uid == user_id:
            del waitlist[index]
            save_waitlist()
            break

def is_waiting(chat_id, user_id):
    return any(cid == chat_id and uid == user_id for cid, uid, _ in waitlist)

def get_all():
    return waitlist

def pop_da_next():
    if waitlist: # checks if not empty
        entry = waitlist.pop(0)
        save_waitlist()
        return entry  # (chat_id, user_id, message_id)
    return None

load_waitlist()