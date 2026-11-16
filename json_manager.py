import json


def read_books_json():
    with open("books.json", "r") as file:
        loads = json.load(file)
    return loads


def add_books_json(dictionary):
    loads = read_books_json()
    loads.append(dictionary)
    with open("books.json", "w") as file:
        json.dump(loads, file, indent=2)
    return "Book was added successfully"

def update_all_books_json(new_json):
    with open("books.json", "w") as file:
        json.dump(new_json, file, indent=2)
    return "File updated new json"

def read_room_json():
    with open("rooms.json", "r") as file:
        loads = json.load(file)
    return loads

def add_room_json(dictionary):
    loads = read_room_json()
    loads.append(dictionary)
    with open("rooms.json", "w") as file:
        json.dump(loads, file, indent=2)
    return "Room was added successfully"


def update_all_rooms_json(new_json):
    with open("rooms.json", "w") as file:
        json.dump(new_json, file, indent=2)
    return "File updated new json"
