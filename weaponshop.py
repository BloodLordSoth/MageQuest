import os, time
from weapons import *

def axe_shop(player):
    from main import load_ascii_art, slow_print, save
    from shop import shop
    value = True
    while value:
        os.system('clear')
        time.sleep(1)
        load_ascii_art('images/axes.txt')
        print(f'|\ [1]Hatchet /\ [2]Double Axe /\ [3]\033[1;32mGreat Axe\033[0m /\ [4]\033[0;34mBattle Axe\033[0m /\ [5]\033[0;35mDragon Bane\033[0m /||\ \033[93mgold:\033[0m {player.gold}\n')
        print(f'Type back to return to the shop\n')
        value = input('> ')
        if value == '1' or value == "hatchet":
            player.buy_weapon(hatchet)
            time.sleep(0.5)
            save(player)
        elif value == 'sword' or value == 'Sword':
            slow_print('I don\'t have any in stock\n')
        elif value == 'back':
            value = False
            shop(player)
        else:
            slow_print('Invalid option, try again\n')


