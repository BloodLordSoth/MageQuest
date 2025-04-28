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
    print('Main menu: [1]New Game [2]Load Game [3]Game rules [4]Quit:\n')
    run = True
    
    while run:
        menu = input(': ')
        if menu == '1' or menu == "N" or menu == 'New Game':
            start_story()
        elif menu == '3' or menu == 'G' or menu == 'Game rules':
            rules()
        elif menu == '4' or menu == 'Q' or menu == 'Quit':
            sys.exit()
        else:
            print('Invalid choice, please try again')

def start_story():
    os.system('clear')
    print('What is your name hero?\n')
    name = input('').lower()
    player = Player(health=100, max_hit=max_hit, name=name)
    enemy = Player(health=100, max_hit=8, name="Goblin")
    print(f"Stranger: This is a dangerous world you have travelled to {name}")
    time.sleep(1)
    print(f"Stranger: There are many dangerous enemies in this land.")
    time.sleep(1)
    print("Stranger: I urge you to speak to Thelemos, in the guild hall.")
    time.sleep(1)
    print('Stranger: Thelemos is our bravest adventurer. You\'ll need his advice')
    time.sleep(1)
    print('[T]ravel [S]hop [M]enu [B]ag [Q]uit')
    value = input(f'{name}: ').lower()
    if value == "T" or value == "Travel":
        pass #Then we travel
    elif value == "S" or value == "Shop":
        pass #Enter the shop
    elif value == "B" or value == 'Bag':
        pass #Enter inventory
    elif value == 'Q' or value == 'Quit':
        time.sleep(1)
        print(f"Saving and quitting...")
        sys.exit()
    else:
        print('Invalid option.')

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        print('It has been many ages before a hero ventured here.....')
        time.sleep(1)
        print('My name is Aeromax, I was one like you... ')  


def rules():
    os.system('clear')
    time.sleep(1)
    print("---------Welcome to MageQuest---------")
    print('|                                     |')
    print('|    This is a simple text rpg        |') 
    print('|    Type the command or letter       |')
    print('|    contained in brackets [] to      |')
    print('|    play the game. Good luck hero!   |')
    print('|                                     |')
    print('|-------------------------------------|')
    print('Press any key to return to the menu')
    choice = input()
    if choice == "":
        start()

if __name__ == '__main__':
    start()
