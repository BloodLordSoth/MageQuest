import os, time
from weapons import *

def axe_shop(self):
    from main import load_ascii_art, slow_print
    from shop import shop
    value = True
    while value:
        os.system('clear')
        time.sleep(1)
        load_ascii_art('images/axes.txt')
        print(f'Type the number to purchase the item | current gold: {self.gold}\n')
        print(f'Type back to return to the shop\n')
        value = input('> ')
        if value == '1' or value == "hatchet":
            self.buy_hatchet()
            time.sleep(1)
            for wep in self.weapons:
                slow_print(f'{wep.name} has been added to the inventory\n')
                time.sleep(0.5)
                slow_print(f'{self.name} has {self.gold} left\n')
        elif value == 'sword' or value == 'Sword':
            slow_print('I don\'t have any in stock\n')
        elif value == 'back':
            shop(self)
        else:
            slow_print('Invalid option, try again\n')


