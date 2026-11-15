from validations import *
from json_manager import *

def next_booking_id():
    loads = read_books_json()
    if not loads:
        return "R001"
    last_one = loads[-1]
    last_digits = last_one["booking_id"][3:]
    last_digits = int(last_digits)
    next_digit = last_digits + 1
    if next_digit < 10:
        return "B00" + str(next_digit)
    elif 10 < next_digit < 100:
        return "B0" + str(next_digit)
    else:
        return "B" + str(next_digit)


def create_order():
    new_order = {}
    new_order["booking_id"] = next_booking_id()


def show_all_orders():
    pass

def search_order():
    pass

def show_client_order():
    pass

def orders_by_date():
    pass

def change_order():
    pass

def cancel_order():
    pass


def orders_manager():
    pass
