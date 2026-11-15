from operator import truediv

from json_manager import *
from validations import *

def room_next_id():
    loads = read_room_json()
    if not loads:
        return "R001"
    last_one = loads[-1]
    last_digits = last_one["room_id"][3:]
    last_digits = int(last_digits)
    next_digit = last_digits + 1
    if next_digit < 10:
        return "R00" + str(next_digit)
    elif 10 < next_digit < 100:
        return "R0" + str(next_digit)
    else:
        return "R" + str(next_digit)



def show_all_rooms():
    loads = read_room_json()
    for room in loads:
        print(room)
    return "All rooms are displayed"

def show_room_detail():
    room_number = input("Enter room ID: ")
    while not is_room_exist(room_number):
        room_number = input("Couldn't find room, Enter a valid room id: ")
    loads = read_room_json()
    for room in loads:
        if room["room_id"] == room_number:
            print(room)
    return "Room is now displayed"

def add_new_room():
    difficulties = ["hard", "medium", "easy"]
    new_room = {}
    new_room["room_id"] = room_next_id()
    name = input("Enter room name: ")
    while not is_str(name):
        name = input("Only a non empty name: ")
    new_room["name"] = name
    difficulty = input("Enter room difficulty: ")
    while not is_str(difficulty):
        difficulty = input("Only a non empty word: ")
    while difficulty not in difficulties:
        difficulty = input("Room difficulty doesn't exist: ")
    new_room["difficulty"] = difficulty
    duration = input("Enter room playing duration: ")
    while not is_positive(duration):
        duration = input("Only a positive number: ")
    duration = int(duration)
    new_room["duration"] = duration
    min_players = input("Enter minimum player for this room: ")
    while not is_positive(min_players):
        min_players = input("Only a positive number of player: ")
    min_players = int(min_players)
    new_room["min_players"] = min_players
    max_players = input("Enter maximum players for this room: ")
    while not is_positive(max_players):
        max_players = input("Only a positive number: ")
    max_players = int(max_players)
    new_room["max_players"] = max_players
    price_per_player = input("Enter price per player for this room: ")
    while not is_positive(price_per_player):
        price_per_player = input("Only a positive number: ")
    price_per_player = int(price_per_player)
    new_room["price_per_player"] = price_per_player
    new_room["is_active"] = True
    return new_room


def update_room_details():
    difficulties = ["hard", "medium", "easy"]
    loads = read_room_json()
    room_id = input("Enter room id to change details: ")
    room_to_update = None
    for room in loads:
        if room["room_id"] == room_id:


            print("""
            What do you want to update?
            1. Room name
            2. Room difficulty
            3. Room duration
            4. Min_players
            5. Max_players
            6. Price per player
            """)
            choose = input()
            while not update_room_choose_checker(choose):
                choose = input("Only a number from  the menu: ")
            choose = int(choose)
            if choose == 1:
                name = input("Enter room new name: ")
                while not is_str(name):
                    name = input("Only a non empty name: ")
                room["name"] = name
            elif choose == 2:
                difficulty = input("Enter room new difficulty: ")
                while not is_str(difficulty):
                    difficulty = input("Only a non empty word: ")
                while difficulty not in difficulties:
                    difficulty = input("Room difficulty doesn't exist: ")
                room["difficulty"] = difficulty
            elif choose == 3:
                duration = input("Enter room playing new duration: ")
                while not is_positive(duration):
                    duration = input("Only a positive number: ")
                duration = int(duration)
                room["duration"] = duration
            elif choose == 4:
                min_players = input("Enter new minimum player for this room: ")
                while not is_positive(min_players):
                    min_players = input("Only a positive number of player: ")
                min_players = int(min_players)
                room["min_players"] = min_players
            elif choose == 5:
                max_players = input("Enter new maximum players for this room: ")
                while not is_positive(max_players):
                    max_players = input("Only a positive number: ")
                max_players = int(max_players)
                room["max_players"] = max_players
            elif choose == 6:
                price_per_player = input("Enter new price per player for this room: ")
                while not is_positive(price_per_player):
                    price_per_player = input("Only a positive number: ")
                price_per_player = int(price_per_player)
                room["price_per_player"] = price_per_player
            update_all_rooms_json(loads)
            return "Updated successfully"

    return "Couldn't find the room, 404"


def change_room_status():
    loads = read_room_json()
    room_id = input("Enter room id to change details: ")
    for room in loads:
        if room["room_id"] == room_id:
            choice = input(f"status is now {room["is_active"]}, are you sure you want to change it? [Y/N]")
            while choice != "Y" and choice != "N":
                choice = input("Only Y or N : ")
            if choice == "Y":
                room["is_active"] = not room["is_active"]
                update_all_rooms_json(loads)
                return "updates successfully"
            else:
                return "Didn't update"
    return "couldn't find the room"


def print_rooms_menu():
    print("""
    ======= ROOMS MANAGER =======
    
    1. Show all rooms
    2. show one room details
    3. add new room
    4. update room details
    5. change room's status
    6. Exit
    """)
    choose = input()
    while not rooms_manager_choose_checker(choose):
        choose = input("Only a number from the menu: ")
    choose = int(choose)
    return choose

def rooms_manager():
    choose = print_rooms_menu()
    while choose != 6:
        if choose == 1:
            print(show_all_rooms())
        elif choose == 2:
            print(show_room_detail())
        elif choose == 3:
            new_room = add_new_room()
            add_room_json(new_room)
            print("Added successfully")
        elif choose == 4:
            room_to_update = update_room_details()
            print(room_to_update)
        elif choose == 5:
            print(change_room_status())
        choose = print_rooms_menu()

    return "Progress has finished"







