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
            if not os.path.exists('savefile.json') or os.path.getsize("savefile.json") == 0:
                slow_print('No save file found\n')
                time.sleep(0.5)
                start()
            else:
                 run = False
                 player = load()
                 wizard_talk(player)
        elif menu == 'G' or menu == 'Game rules' or menu == 'g' or menu == 'game rules':
            rules()
        elif menu == 'Q' or menu == 'Quit' or menu == 'q' or menu == 'quit':
            sys.exit()
        else:
            print('Invalid choice, please try again')

def lookup_weapon(name):
    weapon_dict = {
        "Hatchet": hatchet,
        "Battle Axe": battle_axe,
        "Double Axe": double_axe,
        "Great Axe": great_axe,
        "Dragon Bane": dragon_bane,
        # Add more mappings
    }
    return weapon_dict.get(name)

def load():
    if os.path.getsize("savefile.json") == 0:
        raise ValueError("Save file is empty. Cannot load player data.")

    with open("savefile.json", "r") as f:
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
    # add weapons loading if applicable
    return player

    
def get_name():
    os.system('clear')
    time.sleep(0.5)
    load_ascii_art('images/empty.txt')
    slow_print('It\'s been a long time since we\'ve had a traveler.\n')
    time.sleep(0.5)
    slow_print('Yes yes. I can tell you\'re new around these parts.\n')
    time.sleep(0.5)
    loop = True
    while loop:
        load_ascii_art('images/empty.txt')
        slow_print('So, tell me, what is your name traveler?\n')
        name = input('> ')
        if len(name) > 16 - 1:
            slow_print('Too many characters. Please use 15 or less\n')
            time.sleep(0.5)
        else:    
            slow_print(f'Are you sure you sure it\'s {name}?\n')
            print('\033[92m[Y]es\033[0m or \033[91m[N]o\033[0m')
            option = input('> ')
            if option == 'y' or option == 'yes' or option == 'Y' or option == 'Yes':
                loop = False
                player = Player(health=100, max_hit=15, name=name, max_health=100, mana=100, max_mana=100, gold=250)
                save(player)
                intro(player)
            elif option == 'n' or option == 'no' or option == 'No' or option =='N':
                pass
    
        
        os.system('clear')

def intro(player):
    #os.system('clear')
    #time.sleep(1)
    #slow_print('You\'re probably wondering who I am, I would if I were you\n')
    #time.sleep(1)
    #slow_print('My name is Arabast, I\'m one of the elder wizards in the capital.\n')
    #time.sleep(1)
    #slow_print('While normally I reside in the Light Tower, today, I was called to town.\n')
    #time.sleep(1)
    #os.system('clear')
    #slow_print(f'Looking at you there, {player.name}, I know why.\n')
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
    from ch1 import quest_start

    os.system('clear')
    #slow_print('You approach the elder wizard, and your gaze meets his.\n')
    #time.sleep(1)
    load_ascii_art('images/wizard.txt')
    #slow_print(f'Yes. Yes. I can sense great power within you {self.name}\n')
    #time.sleep(1)
    slow_print(f'Tell me, are you ready to begin {player.name}?\n')
    time.sleep(1)
    #os.system('clear')
    loop = True
    while loop:
        os.system('clear')
        load_ascii_art('images/wizard.txt')
        print('')
        print(f'{player.name} | \033[91mHealth\033[0m: {player.health}/{player.max_health} | \033[94mMana\033[0m: {player.mana}/{player.max_mana} | \033[93mgold\033[0m: {player.gold}')
        print('-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-\n')
        print('|\ [S]tart Game /\ [B]ag /\ [M]agic Spells /|\n')
        menu = input('> ')
        if menu == 'c' or menu == 'combat' or menu == 'C' or menu == 'Combat':
            loop = False
            time.sleep(1)
            slow_print('Teleporting you to the first fight now, good luck hero!\n')
            time.sleep(1)
            minotaur_combat(player)
        if menu == 's' or menu == 'S' or menu == 'shop' or menu == 'Shop':
            loop = False
            quest_start(player)
        if menu == 'b' or menu == 'B' or menu == 'bag' or menu == 'Bag':
            pass
        if menu == 'm' or menu == 'M' or menu == 'magic spells' or menu == 'Magic Spells':  
            for spell in player.spells:
                slow_print('Spellbook:\n')
                print(f'{spell.name} (Cost: {spell.mana_cost}, Damage: {spell.damage})\n')
                slow_print('Press any key to contine')


def wizard_return(player, game_state):
        from ch1 import resume_game
        from shop import shop
        os.system('clear')
        wiz_loop = True
        while wiz_loop:
            os.system('clear')
            load_ascii_art('images/wizard.txt')
            time.sleep(1)
            slow_print(f'Ah, Good to see you again {player.name}\n')
            time.sleep(0.5)
            print(f'{player.name} | \033[91mHealth:\033[0m {player.health}/{player.max_health} | \033[94mMana:\033[0m {player.mana}/{player.max_mana} | \033[93mgold\033[0m: {player.gold}')
            print('-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-\n')
            print(f'\ [C]ontinue /\ [H]eal Me /\ [B]ag /\ [A]bilities /\ [S]ave Game /\ [Q]uit Game /| \n')
            menu = input('> ')
            if menu == 'c' or menu == 'combat' or menu == 'C' or menu == 'Combat':
                slow_print('Returning you now hero\n')
                time.sleep(0.5)
                resume_game(game_state)   
            elif menu == 's' or menu == 'S' or menu == 'save' or menu == 'Save':
                slow_print('Saving the game now hero...')
                time.sleep(0.5)
                save(player)
            elif menu == 'h' or menu == 'H' or menu == 'Heal' or menu == 'heal':
                player.heal_me()
            elif menu == 'i' or menu == 'I' or menu == 'Item Shop' or menu == 'item shop':
                time.sleep(0.5)
                shop(player)
            elif menu == 'q' or menu == 'Q' or menu == 'quit' or menu == 'Quit':
                wiz_loop = False
                save(player)
                sys.exit()
            else:
                slow_print(f'Invalid option, try again hero!\n')
                time.sleep(1)




def save(player):
    data = {
        "name": player.name,
        "health": player.health,
        "max_hit": player.max_hit,
        "mana": player.mana,
        "max_health": player.max_health,
        "max_mana": player.max_mana,
        "gold": player.gold,
        "spells": [spell.__dict__ for spell in player.spells],
        "inventory": player.inventory,
        # "weapons": ...
    }
    with open("savefile.json", "w") as f:
        json.dump(data, f, indent=4)

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
