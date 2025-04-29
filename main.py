import os
import sys
import time
from player import *
from values import max_hit

def start():
    os.system('clear')
    time.sleep(2)
    load_ascii_art('images/intro.txt')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('[N]ew Game')
    print('[L]oad game')
    print('[G]ame rules')
    print('[Q]uit')
    print('---------------')
    run = True
    
    while run:
        menu = input('> ')
        if menu == "N" or menu == 'New Game':
            run = False
            start_story()
        elif menu == 'L' or menu == "Load Game":
            with open('savefile.txt', 'r') as f:
                load_list = f.readlines()
                name = load_list[0]
                health = load_list[1]
                max_hit = load_list[2]
                print(name, health, max_hit)
        elif menu == 'G' or menu == 'Game rules':
            rules()
        elif menu == 'Q' or menu == 'Quit':
            sys.exit()
        elif menu == '77':
            grand_dragon()
        else:
            print('Invalid choice, please try again')

    

    
def start_story():
    from combat import enter_combat
    
    os.system('clear')
    slow_print('What is your name hero?\n')
    name = input('> ')
    
    player = Player(health=100, max_hit=max_hit, name=name, max_health=100, mana=100, max_mana=100)
    minotaur = Player(health=200, max_hit=14, name='Minotaur', max_health=200, mana=None, max_mana=None)
    os.system('clear')
    player_window(name, player)
    print('[T]ravel')
    print('[S]hop')
    print('[M]enu')
    print('[B]ag')
    print('[Q]uit')
    save(name, player.health, player.max_hit)
    run = True
    while run:
        value = input(f'> ')
        if value == "T" or value == "Travel":
            pass #Then we travel
        elif value == "S" or value == "Shop":
            pass #Goes to shop
        elif value == 'M' or value == 'Menu':
            run = False
            start()
        elif value == "B" or value == 'Bag':
            pass #Enter inventory
        elif value == 'Q' or value == 'Quit':
            time.sleep(1)
            save(name, player.health, player.max_hit)
            slow_print("Saving and quitting...")
            sys.exit()
        elif value == 'minotaur':
            run = False
            enter_combat(player, minotaur)
        else:
            print('Invalid option.')

def save(name, health, max_hit):
    list = [
        name,
        str(health),
        str(max_hit),
    ]
    with open('savefile.txt', 'w') as f:
        for item in list:
            f.write(item + '\n')


def grand_dragon():
    os.system('clear')
    time.sleep(1)
    load_ascii_art('images/granddragon.txt')

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay) 


def rules():
    os.system('clear')
    time.sleep(1)
    with open('rules.txt', 'r') as f:
        print(f.read())
    choice = input()
    if choice == "":
        start()

def load_ascii_art(filepath):
    try:
        with open(filepath, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        return "Art not found."

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def slow_print_dragon(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        print()
    

if __name__ == '__main__':
    start()
