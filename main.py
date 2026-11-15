from validations import *
from rooms_manager import rooms_manager

def print_main_menu():
    print("""
    1. Rooms manager
    2. Orders manager
    3. Reports
    4. Exit
    """)
    choose = input()
    while not main_choose_checker(choose):
        choose = input("Only a number from the menu: ")
    choose = int(choose)
    return choose

def active1():
    print(rooms_manager())
def active2():
    pass
def active3():
    pass



def main_menu():
    choose = print_main_menu()
    while choose != 4:
        if choose == 1:
            active1()
        elif choose == 2:
            active2()
        elif choose == 3:
            active3()
        choose = print_main_menu()
    return "progress has finished"

