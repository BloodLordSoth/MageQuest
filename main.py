import os, sys, time, json
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
        elif menu == 'L' or menu == "Load Game" or menu == 'l':
            if os.path.exists("savefile.json"):
                player = load()
                wizard_return(player)
        elif menu == 'G' or menu == 'Game rules' or menu == 'g' or menu == 'game rules':
            rules()
        elif menu == 'Q' or menu == 'Quit' or menu == 'q' or menu == 'quit':
            sys.exit()
        else:
            print('Invalid choice, please try again')

    
def load():
    with open('savefile.json', 'r') as f:
        data = json.load(f)

    player = Player(
        health=data["health"],
        max_hit=data["max_hit"],
        name=data["name"],
        max_health=data["max_health"],
        mana=data["mana"],
        max_mana=data["max_mana"],
        gold=data["gold"]
    )

    player.spells = [Spells.from_dict(s) for s in data["spells"]]
    player.inventory = data["inventory"]
    # You would also reconstruct weapons here if you store weapon attributes
    return player

    
def get_name():
    os.system('clear')
    time.sleep(0.5)
    slow_print('It\'s been a long time since we\'ve had a traveler.\n')
    time.sleep(0.5)
    slow_print('Yes yes. I can tell you\'re new around these parts.\n')
    time.sleep(0.5)
    loop = True
    while True:
        slow_print('So, tell me, what is your name traveler?\n')
        name = input('> ')
        if len(name) > 16 - 1:
            slow_print('Too many characters. Please use 15 or less')
            get_name()
        player = Player(
            health=100,
            max_hit=10,
            name=name,
            max_health=100,
            mana=100,
            max_mana=100,
            gold=0
        )
        slow_print(f'Are you sure you sure it\'s {name}?\n')
        print('\033[92m[Y]es\033[0m or \033[91m[N]o\033[0m')
        option = input('> ')
        if option == 'y' or option == 'yes' or option == 'Y' or option == 'Yes':
            loop = False
            save(player)
            intro(player)
        elif option == 'n' or option == 'no' or option == 'No' or option =='N':
            get_name()
    
        
        os.system('clear')

def intro(player):
    #os.system('clear')
    #time.sleep(1)
    #slow_print('You\'re probably wondering who I am, I would if I were you\n')
    #time.sleep(1)
    #slow_print('My name is Arabast, I\'m one of the elder wizards in the capital.\n')
    #time.sleep(1)
    #slow_print('While normally I reside in the Black Tower, today, I was called to town.\n')
    #time.sleep(1)
    #os.system('clear')
    #slow_print(f'Looking at you there, {name}, I know why.\n')
    #time.sleep(1)
    #slow_print('Here in \033[96mFeldor\033[0m, the citizens are ruled over by the \033[96mking-wizards\033[0m.\n')
    #time.sleep(1)
    #slow_print('A \033[96mking-wizard\033[0m from the Tower of Guilded Light...\n')
    #time.sleep(1)
    #slow_print('and a \033[96mking-wizard\033[0m from the depths of the inverted Tower of Eternal Darkness\n')
    #time.sleep(1)
    #os.system('clear')
    #slow_print('Two towers working to bring balance to \033[96mFeldor\033[0m, though not in harmony\n')
    #time.sleep(1)
    slow_print(f'Come closer {player.name}, let met have a look at you.\n')
    time.sleep(1)
    save(player)
    wizard_talk(player)
    
    
def wizard_talk(player):
    from combat import minotaur_combat
    from shop import shop

    os.system('clear')
    #slow_print('You approach the elder wizard, and your gaze meets his.\n')
    #time.sleep(1)
    #load_ascii_art('images/wizard.txt')
    #slow_print(f'Yes. Yes. I can sense great power within you {self.name}\n')
    #time.sleep(1)
    slow_print('Tell me, what is it you\'re looking for hero?\n')
    #time.sleep(1)
    #os.system('clear')
    loop = True
    while loop:
        load_ascii_art('images/wizard.txt')
        print('')
        print('|\ [S]hop /\ [C]ombat Minotaur /\ [B]ag /\ [A]bilities /|\n')
        menu = input('> ')
        if menu == 'c' or menu == 'combat' or menu == 'C' or menu == 'Combat':
            loop = False
            time.sleep(1)
            slow_print('Teleporting you now, good luck hero!\n')
            time.sleep(1)
            minotaur_combat(player)
        if menu == 's' or menu == 'S' or menu == 'shop' or menu == 'Shop':
            loop = False
            shop(player)

def wizard_return(player):
        from combat import drider_combat
        from shop import shop
        os.system('clear')
        wiz_loop = True
        while wiz_loop:
            load_ascii_art('images/wizard.txt')
            time.sleep(1)
            slow_print(f'Ah, Good to have you back {player.name}\n')
            time.sleep(0.5)
            print('')
            print(f'\ [S]hop /\ [C]ombat Dragon-Rider /\ [B]ag /\ [A]bilities /\ [Q]uit Game /||\ \033[93mGold\033[0m: {player.gold} /\n')
            menu = input('> ')
            if menu == 'c' or menu == 'combat' or menu == 'C' or menu == 'Combat':
                wiz_loop = False
                time.sleep(1)
                slow_print('The wizard smirks....')
                time.sleep(1)
                slow_print(f'Teleporting you now hero, good luck. you\'ll need it this time {player.name}\n')
                time.sleep(1)
                drider_combat(player)
            elif menu == 's' or menu == 'S' or menu == 'shop' or menu == 'Shop':
                wiz_loop = False
                shop(player)
            elif menu == 'q' or menu == 'Q' or menu == 'quit' or menu == 'Quit':
                wiz_loop = False
                quit()

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

def save(player):
    save_data = {
        "name": player.name,
        "health": player.health,
        "max_hit": player.max_hit,
        "mana": player.mana,
        "max_health": player.max_health,
        "max_mana": player.max_mana,
        "gold": player.gold,
        "spells": [spell.to_dict() for spell in player.spells],
        "inventory": player.inventory,
        "weapons": [weapon.name for weapon in player.weapons]  # assuming weapon is an object
    }

    with open('savefile.json', 'w') as f:
        json.dump(save_data, f, indent=2)

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
   
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

if __name__ == '__main__':
    start()
