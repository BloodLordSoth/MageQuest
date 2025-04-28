import os
import sys
import time
import combat
from player import Player
from values import max_hit

def start():
    os.system('clear')
    time.sleep(1)
    print('##########################################################################################################')
    print('#               ███╗   ███╗ █████╗  ██████╗ ███████╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗          #')
    print('#               ████╗ ████║██╔══██╗██╔════╝ ██╔════╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝          #')
    print('#               ██╔████╔██║███████║██║  ███╗█████╗  ██║   ██║██║   ██║█████╗  ███████╗   ██║             #')  
    print('#               ██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║             #')  
    print('#               ██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗╚██████╔╝╚██████╔╝███████╗███████║   ██║             #')  
    print('#               ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝             #')
    print('#                                                                       BloodLordSoth production         #')
    print('##########################################################################################################')
    time.sleep(3)
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
        menu = input('Command: ')
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
    os.system('clear')
    print(slow_print('What is your name hero?\n'))
    name = input('')
    player = Player(health=100, max_hit=max_hit, name=name, max_health=100)
    os.system('clear')
    print(f'{name}')
    print('--------')
    print(f'{player.health} / {player.max_health}')
    print(f'Max hit: {max_hit}')
    print('')
    print('')
    print('')
    print('')
    print('[T]ravel')
    print('[S]hop')
    print('[M]enu')
    print('[B]ag')
    print('[Q]uit')
    save(name, player.health, player.max_hit)
    run = True
    while run:
        value = input(f'Command: ')
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
            save()
            print(slow_print("Saving and quitting..."))
            sys.exit()
        else:
            print(slow_print('Invalid option.'))

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
    print(load_ascii_art('images/granddragon.txt'))

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
            return file.read()
    except FileNotFoundError:
        return "Art not found."

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    

if __name__ == '__main__':
    start()
