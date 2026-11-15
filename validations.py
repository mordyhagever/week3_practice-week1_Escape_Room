from json_manager import *


def is_room_exist(room_number):
    loads = read_room_json()
    for room in loads:
        if room_number == room["room_id"]:
            return True
    return False

def is_str(word):
    if not word:
        return False
    return True

def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def is_positive(number):
    if not is_int(number):
        return False
    number = int(number)
    if number < 1:
        return False
    return True

def update_room_choose_checker(number):
    if not is_int(number):
        return False
    number = int(number)
    if number < 1 or number > 6:
        return False
    return True

def rooms_manager_choose_checker(number):
    if not is_int(number):
        return False
    number = int(number)
    if number < 1 or number > 6:
        return False
    return True
