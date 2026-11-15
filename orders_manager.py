from validations import *
from json_manager import *
import datetime
from datetime import datetime, timedelta

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



def get_date():
    today = datetime.date.today()
    print("Enter a date to order, not farther than a year --- year/ month/ day: ")

    booking_year = input("Year: ")
    while not check_year(booking_year):
        booking_year = input("Only an acceptable year: ")
    booking_year = int(booking_year)
    while booking_year - today.year > 1 or booking_year - today.year < 0:
        booking_year = input("Year is too far, or past already: ")
        while not check_year(booking_year):
            booking_year = input("Only an acceptable year: ")
        booking_year = int(booking_year)

    booking_month = input("Month: ")
    while not check_month(booking_month):
        booking_month = input("Only an acceptable month: ")
    booking_month = int(booking_month)
    if booking_year - today.year == 0:
        while booking_month < today.month:
            booking_month = input("Month past already:  ")
            while not check_month(booking_month):
                booking_month = input("Only an acceptable month: ")
            booking_month = int(booking_month)
    else:
        while booking_month > today.month:
            booking_month = input("Month is too far:  ")
            while not check_month(booking_month):
                booking_month = input("Only an acceptable month: ")
            booking_month = int(booking_month)


    booking_day = input("Day: ")
    while not check_day(booking_day):
        booking_day = input("only an acceptable day: ")
    booking_day = int(booking_day)
    if booking_year - today.year == 0 and booking_month - today.month == 0:
        while booking_day < today.day:
            booking_day = input("day passed already: ")
            while not check_day(booking_day):
                booking_day = input("only an acceptable day: ")
            booking_day = int(booking_day)
    else:
        while booking_day - today.day > 0:
            booking_day = input("day is too far: ")
            while not check_day(booking_day):
                booking_day = input("only an acceptable day: ")
            booking_day = int(booking_day)


    date = datetime.date(booking_year, booking_month, booking_day)
    return date


def get_time():
    print("Enter an hour between 10:00 and 22:00 (the place closes at 22:00) - hour / minute")
    hour = input("Hour: ")
    while not check_hour(hour):
        hour = input("Hour is outside working hours: ")
    # hour = int(hour)
    minutes = input("Minutes: ")
    while not check_minutes(minutes):
        minutes = input("Minutes aren't in the format: ")
    # minutes = int(minutes)
    time = datetime.strptime(f"{hour}:{minutes}", "%H:%M")
    time = time.time()
    return time


def get_available_hour(room_id, date):
    loads = read_room_json()
    all_books = read_books_json()
    new_time = get_time()
    for place in loads:
        if place["room_id"] == room_id:
            if int(new_time.hour) == 21:
                while new_time.minute + place["duration"] > 60:
                    print("hours chosen are too late for this room: ")
                    new_time = get_time()
    for book in all_books:
        if book["room_id"] == room_id:
            if book["booking_date"] == date:
                booked_time = datetime.strptime(book["start_time"], "%H:%M")
                booked_time = booked_time.time()
                booked_time = timedelta(hours=booked_time.hour, minutes=booked_time.minute)
                new_time = timedelta(hours=new_time.hour, minutes=new_time.minute)
                difference1 = booked_time - new_time
                difference2 = new_time - booked_time
                while difference1 < timedelta(minutes=15) or difference2 < timedelta(minutes=15):
                    new_time = get_time()
print(get_available_hour("R001", "2026-11-18"))





def create_order():
    new_order = {}
    new_order["booking_id"] = next_booking_id()
    customer_name = input("Enter customer name: ")
    while not is_str(customer_name):
        customer_name = input("Only a non empty name: ")
    new_order["customer_name"] = customer_name
    exist = False
    loads = read_room_json()
    if not loads:
        return "Can't create order there's no rooms exist!!!"
    room_id = None
    while not exist:
        room_id = input("Enter room id: ")
        for room in loads:
            if room["room_id"] == room_id:
                exist = True
                if not room["is_active"]:
                    return "is unavailable. please try again later..."
    new_order["room_id"] = room_id
    date = get_date()
    time = get_available_hour(new_order["room_id"], date)














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
