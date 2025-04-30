import os, sys, time
from player import *
from values import max_hit

def start():
    os.system('clear')
    time.sleep(1)
    load_ascii_art('images/intro.txt')
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
            get_name()
        elif menu == 'L' or menu == "Load Game":
            with open('savefile.txt', 'r') as f:
                load_list = f.readlines()
                name = load_list[0]
                health = load_list[1]
                max_hit = load_list[2]
                mana = load_list[3]
                print(name, health, max_hit, mana)
        elif menu == 'G' or menu == 'Game rules' or menu == 'g' or menu == 'game rules':
            rules()
        elif menu == 'Q' or menu == 'Quit' or menu == 'q' or menu == 'quit':
            sys.exit()
        else:
            print('Invalid choice, please try again')

    

    
def get_name():
    os.system('clear')
    time.sleep(0.5)
    slow_print('It\'s been a long time since we\'ve had a traveler.\n')
    time.sleep(0.5)
    slow_print('Yes yes. I can tell you\'re new around these parts.\n')
    time.sleep(0.5)
    loop = True
    while True:
        slow_print('So. What is your name traveler?\n')
        name = input('> ')
        slow_print(f'Are you sure you sure it\'s {name}?\n')
        print('[Y]es or [N]o')
        option = input('> ')
        if option == 'y' or option == 'yes' or option == 'Y' or option == 'Yes':
            loop = False
            intro(name)
        elif option == 'n' or option == 'no' or option == 'No' or option =='N':
            get_name()
    
        
        os.system('clear')

def intro(name):
    self = Player(health=100, max_hit=max_hit, name=name, max_health=100, mana=100, max_mana=100, gold=0)
    os.system('clear')
    time.sleep(1)
    slow_print('You\'re probably wondering who I am, I would if I were you\n')
    time.sleep(1)
    slow_print('My name is Arabast, I\'m one of the elder wizards in the capital.\n')
    time.sleep(1)
    slow_print('While normally I reside in the Black Tower, today, I was called to town.\n')
    time.sleep(1)
    os.system('clear')
    slow_print(f'Looking at you there, {name}, I know why.\n')
    time.sleep(1)
    slow_print('Here in Feldor, the citizens are ruled over by the king-wizards.\n')
    time.sleep(1)
    slow_print('A king-wizard from the Tower of Guilded Light...\n')
    time.sleep(1)
    slow_print('and a king-wizard from the depths of the inverted Tower of Eternal Darkness\n')
    time.sleep(1)
    os.system('clear')
    slow_print('Two towers working to bring balance to Feldor, though not in harmony\n')
    time.sleep(1)
    slow_print(f'Come closer {name}, let met have a look at you.\n')
    time.sleep(2)
    wizard_talk(self)
    
    
def wizard_talk(self):
    from combat import minotaur_combat
    from shop import shop
    target = Player(health=100, max_hit=30, name='Minotaur', max_health=100, mana=None, max_mana=None, gold=180)
    os.system('clear')
    slow_print('You approach the elder wizard, and your gaze meets his.\n')
    time.sleep(1)
    load_ascii_art('images/wizard.txt')
    slow_print(f'Yes. Yes. I can sense great power within you {self.name}\n')
    time.sleep(1)
    slow_print('Tell me, what is it you\'re looking for hero?\n')
    time.sleep(1)
    os.system('clear')
    loop = True
    while loop:
        load_ascii_art('images/wizard.txt')
        print('')
        print('[S]hop [C]ombat_Minotaur [B]ag [A]bilities\n')
        menu = input('> ')
        if menu == 'c' or menu == 'combat' or menu == 'C' or menu == 'Combat':
            loop = False
            time.sleep(1)
            slow_print('Teleporting you now, good luck hero!\n')
            time.sleep(1)
            minotaur_combat(self, target)
        if menu == 's' or menu == 'S' or menu == 'shop' or menu == 'Shop':
            loop = False
            shop(self)

        else:
            slow_print('Function hasn\'t been added yet\n')



    
def menu(self, target):   
    run = True
    while run:
        print('[T]ravel [S]hop [M]enu [B]ag [Q]uit')
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
