import os
import time
from weapons import *
from main import load_ascii_art, slow_print

def weapon_shop(self):
    shop = True
    while shop:
        os.system('clear')
        load_ascii_art('images/weaponshop.txt')
        print('What item would you like to purchase?\n')
        choice = input('> ')
        if choice == 'axe' or choice == "Axe":
            pass
        elif choice == 'sword' or choice == 'Sword':
            pass
        else:
            slow_print('Invalid option, try again')


