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
    print('[N]ew Game')
    print('[L]oad game')
    print('[G]ame rules')
    print('[Q]uit')
    print('---------------')
    run = True
    
    while run:
        menu = input('> ')
        if menu == "N" or menu == 'New Game' or menu == 'n':
            run = False
            start_story()
        elif menu == 'L' or menu == "Load Game":
            with open('savefile.txt', 'r') as f:
                load_list = f.readlines()
                name = load_list[0]
                health = load_list[1]
                max_hit = load_list[2]
                mana = load_list[3]
                print(name, health, max_hit, mana)
        elif menu == 'G' or menu == 'Game rules':
            rules()
        elif menu == 'Q' or menu == 'Quit':
            sys.exit()
        else:
            print('Invalid choice, please try again')

    

    
def start_story():
    from combat import minotaur_combat
    
    os.system('clear')
    slow_print('What is your name hero?\n')
    name = input('> ')
    
    self = Player(health=100, max_hit=max_hit, name=name, max_health=100, mana=100, max_mana=100, gold=0)
    target = Player(health=200, max_hit=14, name='Minotaur', max_health=200, mana=None, max_mana=None, gold=300)
    os.system('clear')
    print('[T]ravel')
    print('[S]hop')
    print('[M]enu')
    print('[B]ag')
    print('[Q]uit')
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
            slow_print("Saving and quitting...")
            sys.exit()
        elif value == 'minotaur' or value == 'min':
            run = False
            minotaur_combat(self, target)
        else:
            print('Invalid option.')

def save(self):
    list = [
        self.name,
        str(self.health),
        str(self.max_hit),
        str(self.mana),
    ]
    with open('savefile.txt', 'w') as f:
        for item in list:
            f.write(item + '\n')

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
   

if __name__ == '__main__':
    start()
