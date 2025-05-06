import os, sys, time
from main import save, wizard_return, load_ascii_art, slow_print

def quest_start(player):
    os.system('clear')
    load_ascii_art('images/empty.txt')
    time.sleep(0.5)
    slow_print('\033[96mVarengale\033[0m, major city of \033[96mFeldor\033[0m, and nested between the two towers.\n')
    time.sleep(0.5)
    slow_print('As the city comes into view, you marvel and the crafstmanship of the city\n')
    time.sleep(0.5)
    os.system('clear')
    load_ascii_art('images/city.txt')
    slow_print('"This city must have taken many life times to build." You think to yourself.\n')
    time.sleep(1)
    slow_print('')
    first_quest(player)

def first_quest(player):
    from shop import shop
    game_state = {
    "location": "first_quest",
    "current_enemy": None,
    "player": player,
}
    loop = True
    while loop:
        os.system('clear')
        load_ascii_art('images/city.txt')
        print('')
        print(f'{player.name} | \033[91mHealth\033[0m: {player.health}/{player.max_health} | \033[94mMana\033[0m: {player.mana}/{player.max_mana} | \033[93mgold\033[0m: {player.gold}')
        print('-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-')
        print('|\ [M]ove /\ [E]xamine /\ [T]alk /\ [S]hop /\ [W]izard /\ [Q]uit /|  \n')
        choice_one = input('> ')
        if choice_one == 't' or choice_one == 'T' or choice_one == 'Talk' or choice_one == "talk":
            slow_print('There is no one near you to talk to\n')
        if choice_one == 'e' or choice_one == 'E' or choice_one == 'Examine' or choice_one == "examine":
            slow_print('You\'re at the gates of the city of Varengale. There are three...\n')
            time.sleep(0.5)
            slow_print('paths set before you. To the North, The castle.\n')
            time.sleep(0.5)
            slow_print('To the East, a brilliant tower of light.\n')
            time.sleep(0.5)
            slow_print('To the West, A tower as dark as night itself.\n')
            time.sleep(0.5)
        if choice_one == 'm' or choice_one == 'M' or choice_one == 'Move' or choice_one == "move":
            slow_print('Where would you like to go?\n')
            choice_two = input('> ')
            if choice_two == 'N' or choice_two == 'North' or choice_two == 'north' or choice_two == 'n':
                loop = False
                slow_print('You decide to trek North, towards the castle.\n')
                time.sleep(1)
                castle_start(player)
            if choice_two == 'E' or choice_two == 'East' or choice_two == 'east' or choice_two == 'e':
                slow_print('Taken by the sight of the illustrious tower, you begin your trek.\n')
            if choice_two == 'W' or choice_two == 'West' or choice_two == 'west' or choice_two == 'w':
                slow_print('The dark tower stirs something in you. Curiosity, lust for power?\n')
        if choice_one == 's' or choice_one == 'S' or choice_one == 'Shop' or choice_one == "shop":
            loop = False
            time.sleep(0.5)
            shop(player, game_state)
        if choice_one == 'w' or choice_one == 'W' or choice_one == 'Wizard' or choice_one == "wizard":
            loop = False
            slow_print('You hold the amulet in your hand, and the world shimmers away...')
            time.sleep(1)
            wizard_return(player, game_state)
        if choice_one == 'q' or choice_one == 'Q' or choice_one == 'Quit' or choice_one == "quit":
            slow_print('Are you sure you want to quit?\n')
            exit = input('> ')
            if exit == 'Yes' or exit == 'y' or exit == "yes" or exit == 'Y':
                save(player)
                slow_print('Saving and quitting....\n')
                sys.exit()
            else:
                print('')

def castle_start(player):
    from combat import knight_combat
    from player import Player
    target = Player(health=60, max_hit=10, name='Knight', max_health=60, mana=None, max_mana=None, gold=300)
    os.system('clear')
    load_ascii_art('images/empty.txt')
    slow_print('You feel the trail crunch beneath your feet as you progress the path.\n')
    time.sleep(0.5)
    slow_print('The deafening noise of the city fades off into the distance.\n')
    time.sleep(0.5)
    slow_print('At last, a moment to collect your thoughts, today has been....interesting.\n')
    time.sleep(1.5)
    os.system('clear')
    load_ascii_art('images/empty.txt')
    slow_print('"\033[91mHALT!\033[0m You there!"\n')
    time.sleep(1.5)
    slow_print('The words freeze you in your tracks. Before you can take stock of your situation...\n')
    slow_print('You are descended upon by a kingdom knight.\n')
    time.sleep(1.5)
    os.system('clear')
    time.sleep(1)
    load_ascii_art('images/knightcombat.txt')
    slow_print(f'"Yeah, that\'s him alright, that\'s {player.name}"\n')
    slow_print('An elderly man\'s finger points in your direction.\n')
    time.sleep(1)
    slow_print(f'You. {player.name}. You\'re under arrest!\n')
    time.sleep(1)
    os.system('clear')
    knight_combat(player, target)

def prison(player):
    os.system('clear')
    load_ascii_art('images/knightstand.txt')
    time.sleep(1)
    slow_print('Enough of this! Cease this at once!\n')
    time.sleep(1)
    slow_print(f'You {player.name}, are under arrest! Guards sieze him!\n')
    time.sleep(1)
    os.system('clear')
    load_ascii_art('images/swordpoint.txt')
    time.sleep(1)
    slow_print('The blade held up against your throat, you throw your arms up in the air.\n')
    time.sleep(1)
    slow_print('You resolve that it\'s better to live, and find your way out of this mess...\n')
    time.sleep(1)
    os.system('clear')
    time.sleep(0.3)
    load_ascii_art('images/flail.txt')
    slow_print('\033[91mWHACK!!\033[0m\n')
    time.sleep(1)
    os.system('clear')
    load_ascii_art('images/empty.txt')
    slow_print('Everything goes black, as your body hits the ground with a thud.\n')
    time.sleep(1)
    slow_print('....\n')
    time.sleep(1)
    slow_print('........\n')
    time.sleep(1)
    slow_print('..............\n')
    time.sleep(0.5)
    os.system('clear')
    load_ascii_art('images/empty.txt')
    slow_print('You haven\'t a clue how long you\'ve been unconcious...\n')
    time.sleep(1)
    slow_print('Feeling like your head is being pounded on like an anvil\n you rise up to your feet.\n')
    time.sleep(1)
    slow_print('Taking in your surroundings, you wonder what could be in store for you.\n')
    time.sleep(1)
    os.system('clear')
    load_ascii_art('images/dungeon.txt')
    time.sleep(1.5)
    slow_print('You find yourself in a very dreary situation.\n')
    time.sleep(1)
    dungeon(player)

def dungeon(player):
    from shop import shop
    game_state = {
    "location": "dungeon",
    "current_enemy": None,
    "player": player,
}
    loop = True
    while loop:
        os.system('clear')
        load_ascii_art('images/dungeon.txt')
        print('')
        print(f'{player.name} | \033[91mHealth\033[0m: {player.health}/{player.max_health} | \033[94mMana\033[0m: {player.mana}/{player.max_mana} | \033[93mgold\033[0m: {player.gold}')
        print('-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-')
        print('|\ [M]ove /\ [E]xamine /\ [T]alk /\ [S]hop /\ [W]izard /\ [Q]uit /|  \n')
        choice_one = input('> ')
        if choice_one == 't' or choice_one == 'T' or choice_one == 'Talk' or choice_one == "talk":
            slow_print('Oh hey a newcomer! Welcome!\n')
            time.sleep(1)
            slow_print('My name is Conan, I was once the bravest knight in the land.\n')
            time.sleep(1)
            slow_print('I\'ve allowed the guards to capture me, to spare their lives\n')
            time.sleep(1)
            slow_print('')
        elif choice_one == 'e' or choice_one == 'E' or choice_one == 'Examine' or choice_one == "examine":
            slow_print('As you look around the castle dungeon, you look for any means of escape.\n')
            time.sleep(1)
            slow_print('Standing next to you, you see an old man, chained up to the wall.\n')
            time.sleep(1)
            slow_print('To the East, you see the faint glowing of torch light \n that vanishes beyond the corridor.\n')
            time.sleep(2)
        elif choice_one == 'm' or choice_one == 'M' or choice_one == 'Move' or choice_one == "move":
            slow_print('Where would you like to go?\n')
            choice_two = input('> ')
            if choice_two == 'E' or choice_two == 'East' or choice_two == 'east' or choice_two == 'e':
                slow_print('Taken by the sight of the illustrious tower, you begin your trek.\n')
            elif choice_two == 'W' or choice_two == 'West' or choice_two == 'west' or choice_two == 'w':
                slow_print('The dark tower stirs something in you. Curiosity, lust for power?\n')
        elif choice_one == 's' or choice_one == 'S' or choice_one == 'Shop' or choice_one == "shop":
            loop = False
            time.sleep(0.5)
            shop(player, game_state)
        elif choice_one == 'w' or choice_one == 'W' or choice_one == 'Wizard' or choice_one == "wizard":
            loop = False
            slow_print('You hold the amulet in your hand, and the world shimmers away...')
            time.sleep(1)
            wizard_return(player, game_state)
        elif choice_one == 'q' or choice_one == 'Q' or choice_one == 'Quit' or choice_one == "quit":
            slow_print('Are you sure you want to quit?\n')
            exit = input('> ')
            if exit == 'Yes' or exit == 'y' or exit == "yes" or exit == 'Y':
                save(player)
                slow_print('Saving and quitting....\n')
                sys.exit()
            else:
                pass



def resume_game(game_state):
    from combat import minotaur_combat, drider_combat, knight_combat, knight_combat2, min_part2
    from main import wizard_return
    if game_state["location"] == "min_pt1":
        minotaur_combat(game_state["player"], game_state["current_enemy"])
    elif game_state["location"] == "min_pt2":
        min_part2(game_state["player"], game_state["current_enemy"])
    elif game_state["location"] == "first_quest":
        first_quest(game_state["player"])
    elif game_state["location"] == "knight_combat":
        knight_combat(game_state["player"], game_state["current_enemy"])
    elif game_state["location"] == "knight_combat2":
        knight_combat2(game_state["player"], game_state["current_enemy"])
    elif game_state["location"] == "d_rider":
        drider_combat(game_state["player"], game_state["current_enemy"])
    elif game_state["location"] == "wiz_menu":
        wizard_return(game_state["player"])
    elif game_state["location"] == "dungeon":
        dungeon(game_state["player"])