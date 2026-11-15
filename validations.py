from json_manager import *
import datetime

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

def check_year(year):
    if not year:
        return False
    if len(year) < 4 or len(year) > 4:
        return False
    if not is_int(year):
        return False
    year = int(year)
    if year < 2025:
        return False
    return True

def check_month(month):
    if not month:
        return False
    if len(month) < 2 or len(month) > 2:
        return False
    if not is_int(month):
        return False
    month = int(month)
    if month > 12 or month < 1:
        return False
    return True

def check_day(day):
    if not day:
        return False
    if len(day) < 1 or len(day) > 2:
        return False
    if not is_int(day):
        return False
    day = int(day)
    if day > 31 or day < 1:
        return False
    return True


def check_hour(hour):
    if not is_int(hour):
        return False
    hour = int(hour)
    if hour >= 22 or hour < 10:
        return False
    return True

def check_minutes(minutes):
    if not is_int(minutes):
        return False
    minutes = int(minutes)
    if minutes > 59 or minutes < 00:
        return False
    return True

def main_choose_checker(number):
    if not is_int(number):
        return False
    number = int(number)
    if number < 1 or number > 4:
        return False
    return True
