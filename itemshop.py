import os, time
from items import *
from spells import *

def scroll_shop(player):
    from main import load_ascii_art, slow_print, save
    from shop import shop
    value = True
    while value:
        os.system('clear')
        time.sleep(1)
        load_ascii_art('images/scroll.txt')
        print(f'|\ [1]Scroll of Fireball /\ [2]Scroll of Heal /\ [3] /\ [4]Scroll of Thunder /\ [N]ext /|\ \033[93mgold:\033[0m {player.gold}\n')
        print(f'Type back to return to the shop\n')
        value = input('> ')
        if value == '1' or value == "scroll of fireball":
            player.buy_scroll(fireball, fb_scroll)
            time.sleep(0.5)
        elif value == 'n' or value == 'N' or value == 'next' or value == 'Next':
            os.system('clear')
            load_ascii_art('images/scroll2.txt')
            print(f'/\ [4]Corrosion /\ [5]Fire Storm /\ [6]Ice Lance /|\ \033[93mgold:\033[0m {player.gold}\n')
            scroll_2 = input('> ')
            if scroll_2 == '4' or scroll_2 == 'corrosion' or scroll_2 == 'Corrosion':
                slow_print('I dont have any of those in stock yet.')
        elif value == 'back':
            value = False
            save(game_state)
            shop(player, game_state)
        else:
            slow_print('Invalid option, try again\n')


