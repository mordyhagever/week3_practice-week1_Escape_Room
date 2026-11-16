from typing import final

from validations import *
from json_manager import *
import datetime
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

def get_previous_date():
    year = input("Enter year: ")
    while not check_year(year):
        year = input("Only an acceptable year: ")
    month = input("enter month: ")
    while not check_month(month):
        month = input("Only an acceptable month: ")
    day = input("Enter day: ")
    while not check_day(day):
        day = input("Only an acceptable day: ")
    try:
        return datetime.date(int(year), int(month), int(day))
    except ValueError:
        return "Something went wrong with the date"

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
    time = datetime.datetime.strptime(f"{hour}:{minutes}", "%H:%M")
    time = time.time()
    return time

def check_date_time(room_id):
    all_orders = read_books_json()
    all_rooms = read_room_json()
    room_duration = 0
    now = datetime.datetime.now()
    date = get_date()
    time = get_time()
    date_and_time = datetime.datetime.combine(date, time)
    for room in all_rooms:
        if room["room_id"] == room_id:
            room_duration = room["duration"]
    for order in all_orders:
        if order["room_id"] == room_id:
            if datetime.datetime.strptime(order["booking_date"], "%Y-%m-%d").date() == date_and_time.date():
                room_duration += 15
                current_room_start = date_and_time
                current_room_duration = datetime.timedelta(minutes=room_duration)
                current_room_finish = current_room_start + current_room_duration
                other_room = datetime.time.strptime(order["start_time"], "%H:%M")
                other_room = datetime.datetime.combine(current_room_start.date(), other_room)
                other_room_finish = other_room + current_room_duration

                while current_room_finish > other_room and current_room_start < other_room_finish:
                    print("Time is too close to other game!")
                    time = get_time()
                    date_and_time = datetime.datetime.combine(date, time)
                    current_room_start = date_and_time
                    current_room_duration = datetime.timedelta(minutes=room_duration)
                    current_room_finish = current_room_start + current_room_duration
                    other_room = datetime.time.strptime(order["start_time"], "%H:%M")
                    other_room = datetime.datetime.combine(current_room_start.date(), other_room)
                    other_room_finish = other_room + current_room_duration
    print("time approved")
    return date_and_time





def create_order():
    new_order = {}
    price = 0.0
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
                price = room["price_per_player"]
                exist = True
                if not room["is_active"]:
                    return "is unavailable. please try again later..."
    new_order["room_id"] = room_id
    date_and_time = check_date_time(room_id)
    week_day = date_and_time.date().weekday()
    new_order["booking_date"] = date_and_time.strftime("%Y-%m-%d")
    new_order["start_time"] = date_and_time.strftime("%H:%M")
    players = input("Enter amount of players: ")
    while not is_int(players):
        players = input("only a positive number")
    players = int(players)
    while not check_room_capacity(room_id, players):
        players = input("Too much or too little players: ")
        while not is_int(players):
            players = input("only a positive number")
        players = int(players)
    new_order["players"] = players
    discount = 0
    if players > 4 and players <= 6:
        discount = 10
    elif players > 7:
        discount = 15
    final_price = (price * players) - (price * (discount / 100))
    if week_day == 4 or week_day == 5:
        more_discount = final_price * 0.15
        final_price -= more_discount
    new_order["total_price"] = round(final_price, 2)
    new_order["status"] = "Active"
    add_books_json(new_order)
    return "Order has been updated successfully"



def cancellation_price(booking_time, price):
    cancel_price = 0.0
    now = datetime.datetime.now()
    if booking_time - now < datetime.timedelta(hours=24):
        if booking_time - now < datetime.timedelta(hours=6):
            if booking_time - now <= datetime.timedelta(minutes=1):
                return "can't cancel"
            cancel_price = price * 0.5
            return cancel_price
        cancel_price = price * 0.0
        return cancel_price
    cancel_price = 0.0
    return cancel_price

def cancel_order():
    order_id = input("Enter order id to cancel: ")
    all_orders = read_books_json()
    found = False
    for order in all_orders:
        if order["booking_id"] == order_id:
            found = True
            order_date = order["booking_date"]
            order_time = order["start_time"]
            final_price = order["total_price"]
    if not found:
        return "Couldn't find ID"
    date = datetime.datetime.strptime(order_date, "%Y-%m-%d")
    time = datetime.datetime.strptime(order_time, "%H:%M")
    date_and_time = datetime.datetime.combine(date.date(), time.time())
    cancellation_fee = cancellation_price(date_and_time, final_price)
    if cancellation_fee == "can't cancel":
        return "Can't cancel"
    print(f"cancellation fee is {cancellation_fee}")
    for order in all_orders:
        if order["booking_id"] == order_id:
            order["cancellation_fee"] = cancellation_fee
            order["status"] = "cancelled"
    update_all_books_json(all_orders)
    return "Order has been cancelled and updated"

def print_orders_menu():
    print("""
    ======== ORDERS MENU ========
    1. Create a new order
    2. Show all bookings
    3. Search booking by ID
    4. Show a client's booking
    5. Search booking by date
    6. Change booking details
    7. Cancel order
    8. Exit
    """)
    choose = input()
    while not orders_manager_choose_checker(choose):
        choose = input("Only a positive number from the menu: ")
    choose = int(choose)
    return choose

def show_all_orders():
    all_orders = read_books_json()
    return all_orders

def search_order_by_id():
    all_orders = read_books_json()
    order_id = input("Enter booking id: ")
    for order in all_orders:
        if order["order_id"] == order_id:
            return order
    return "Couldn't find order"


def show_client_order():
    all_orders = read_books_json()
    client_name = input("Enter client's name: ")
    found = False
    while not is_str(client_name):
        client_name = input("Only a non empty name: ")
    for order in all_orders:
        if order["customer_name"] == client_name:
            found = True
            print(order)
    if found:
        return "All ordered of this client are displayed"
    return "Customer has not found"

def search_order_by_date():
    print("Enter date to search: ")
    order_date = get_previous_date()
    all_orders = read_books_json()
    found = False
    for order in all_orders:
        day = datetime.datetime.strptime(order["booking_date"], "%Y-%m-%d")
        if order_date == day.date():
            found = True
            print(order)
    if found:
        return "All orders displayed"
    return "Couldn't find order"

def print_change_booking_manu():
    print("""
    WHAT DO YOU WANT TO CHANGE?
    1. Customer's name
    2. Room ID
    3. Booking date
    4. Start time
    5. Number of players
    6. At the end, i don't wanna change anything
    """)
    choose = input()
    while not change_booking_choose_checker(choose):
        choose = input("Only a number from the menu: ")
    choose = int(choose)
    return choose

def change_booking():
    all_orders = read_books_json()
    order_id = input("Enter booking id to change order: ")
    found = False
    for order in all_orders:
        if order["booking_id"] == order_id:
            found = True
    if not found:
        return "Couldn't find booking"
    choose = print_change_booking_manu()
    for order in all_orders:
        if order["booking_id"] == order_id:
            if choose == 1:
                client_name = input("Enter new customer's name: ")
                while not is_str(client_name):
                    client_name = input("Only a non empty name: ")
                order["customer_name"] = client_name
            elif choose == 2:
                room_id = input("Enter a new room id: ")
                while not is_room_exist(room_id):
                    room_id = input("Room, doesn't exist: ")
                order["room_id"] = room_id
            # elif choose == 3:
            #     order_date = get_date()
            #     order_time = order["booking_time"]
            #     date_and_time = datetime.datetime.combine(order_date, order_time)
            #     order["booking_date"] = date_and_time.strftime("%Y-%m-%d")
            # elif choose == 4:
            #     order_time = get_time()
            #     order_date = order["booking_date"]
            #     date_and_time = datetime.datetime.combine(order_date, order_time)
            #     order["booking_time"] = date_and_time.strftime("%H:%M")
            elif choose == 5:
                players = input("Enter number of players: ")
                while not is_int(players):
                    players = input("only a positive number")
                players = int(players)
                while not check_room_capacity(order["room_id"], players):
                    players = input("Too much or too little players: ")
                    while not is_int(players):
                        players = input("only a positive number")
                    players = int(players)
                order["players"] = players
            elif choose == 6:
                return "Nothing changed"

    if choose == 3 or choose == 4:
        for order in all_orders:
            if order["booking_id"] == order_id:
                is_possible = check_date_time(order["room_id"])
                order["booking_date"] = is_possible.strftime("%Y-%m-%d")
                order["start_time"] = is_possible.strftime("%H:%M")
    update_all_books_json(all_orders)
    return "Booking has been updated"






def orders_manager():
    choose = print_orders_menu()
    while choose != 8:
        if choose == 1:
            print(create_order())
        elif choose == 2:
            orders = show_all_orders()
            for order in orders:
                print(order)
        elif choose == 3:
            print(search_order_by_id())
        elif choose == 4:
            print(show_client_order())
        elif choose == 5:
            print(search_order_by_date())
        elif choose == 6:
            print(change_booking())
        elif choose == 7:
            print(cancel_order())

        choose = print_orders_menu()

    return "Progress has finished, back to main menu"



