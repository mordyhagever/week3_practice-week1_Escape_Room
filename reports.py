from validations import *
from json_manager import *

def print_reports_menu():
    print("""
    ====== REPORTS MENU ======
    1. All active bookings
    2. All cancelled bookings
    3. All revenue from active bookings
    4. all cancellations fee
    5. Most popular room
    6. Orders number in each room
    7. Active percentage in one room
    8. Exit
    """)
    choose = input()
    while not reports_choose_checker(choose):
        choose = input("Only a number from the menu: ")
    choose = int(choose)
    return choose

def all_active_booking():
    all_orders = read_books_json()
    for order in all_orders:
        if order["status"] == "Active":
            print(order)
    return "All active orders are displayed"

def all_cancelled_booking():
    all_orders = read_books_json()
    for order in all_orders:
        if order["status"] == "cancelled":
            print(order)
    return "Cancelled orders are displayed, if there is"

def all_revenue_from_active():
    revenue = 0
    all_orders = read_books_json()
    for order in all_orders:
        if order["status"] == "Active":
            revenue += order["total_price"]
    return f"All revenue from active bookings: {revenue}"

def all_cancellations_fee():
    fee = 0
    all_orders = read_books_json()
    for order in all_orders:
        if order["status"] == "cancelled":
            fee += order["cancellation_fee"]
    return f"All cancellations fee: {fee}"

def most_popular_room():
    all_orders = read_books_json()
    all_rooms = read_room_json()
    rooms_used = {}
    for room in all_rooms:
        rooms_used[room["room_id"]] = 0
    for order in all_orders:
        rooms_used[order["room_id"]] += 1
    popular = max(rooms_used, key=rooms_used.get)
    return f"Most popular room is: {popular}"

def orders_number_each_room():
    all_orders = read_books_json()
    all_rooms = read_room_json()
    rooms_used = {}
    for room in all_rooms:
        rooms_used[room["room_id"]] = 0
    for order in all_orders:
        rooms_used[order["room_id"]] += 1
    return rooms_used

def active_percentage():
    room_id = input("Enter room id: ")
    all_rooms = read_room_json()
    all_orders = read_books_json()
    found = False
    for room in all_rooms:
        if room["room_id"] == room_id:
            found = True
    if not found:
        return "Couldn't find the room"
    total_time = 0
    for order in all_orders:
        if order["room_id"] == room_id:
            for room in all_rooms:
                if room["room_id"] == room_id:
                    total_time += room["duration"]
    total_time /= 60
    percentage = total_time / 12
    percentage = round(percentage * 100, 1)
    return f"active percentage is: {percentage}%"

def reports_manager():
    choose = print_reports_menu()
    while choose != 8:
        if choose == 1:
            print(all_active_booking())
        elif choose == 2:
            print(all_cancelled_booking())
        elif choose == 3:
            print(all_revenue_from_active())
        elif choose == 4:
            print(all_cancellations_fee())
        elif choose == 5:
            print(most_popular_room())
        elif choose == 6:
            print(orders_number_each_room())
        elif choose == 7:
            print(active_percentage())
        choose = print_reports_menu()
    return "Back to main menu"
