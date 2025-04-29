import os
import sys
import time
from main import slow_print, load_ascii_art
from player import player_window

def enter_combat(player, minotaur):
    os.system('clear')
    slow_print('The door opens with a creak, sending chills down your spine.\n')
    time.sleep(1)
    slow_print('You hear an unreal bellow from across the chamber, and your stance tightens.\n')
    time.sleep(1)
    slow_print('As the figure emerges from the shadows, you lose your breath.\n')
    time.sleep(1)
    slow_print('Oh fuck. A minotaur...\n')
    time.sleep(1)
    os.system('clear')
    player_window(player.name, player)
    load_ascii_art('images/minotaur.txt')
    print(f'                         Minotaur health: {minotaur.health}')

    while player.health > 0 and minotaur.health > 0:
        print("[Attack] [Cast] [Run]: \n")
        choice = input('> ')
        if choice  == 'attack' or choice == 'A' or choice == 'a':
            player.hit(minotaur)
            if minotaur.health > 0:
                minotaur.hit(player)
            player.get_status()
            minotaur.get_status()
        elif choice == 'cast' or choice == 'C' or choice == 'Cast':
            spells(player, minotaur)
        elif choice == 'run':
            slow_print(f"{player.name} has run away")
            sys.exit()
        else:
            slow_print("Invalid input, please type fight or run\n")
    
    if player.health < 0:
        death(player, minotaur)
    elif minotaur.health < 0:
        slow_print(f'{minotaur.name} has been slain!')

def spells(player, minotaur):
    slow_print('What spell would you like to cast?\n')
    cast = input('> ')
    if cast == "spellbook":
        pass
    elif cast == 'fireball':
        time.sleep(0.5)
        slow_print(f'{player.name} casts Fireball at the {minotaur.name}...\n')
        player.fireball(minotaur)
        if minotaur.health > 0:
            minotaur.hit(player)
        player.get_status()
        minotaur.get_status()
    elif cast == 'heal':
        time.sleep(0.5)
        slow_print(f'{player.name} recites the words to Healing Touch..\n')
        player.heal(player)
        player.get_status()

def death(player, minotaur):
    from main import start
    os.system('clear')
    time.sleep(1)
    load_ascii_art('images/death.txt')
    time.sleep(2)
    slow_print(f'Our hero {player.name} has been laid to rest\n')
    time.sleep(1)
    print('Continue? [Y]es or [N]o\n')
    choice = input('> ')
    if choice == 'Y' or choice == "Yes" or choice == 'y' or choice == 'yes':
        enter_combat(player, minotaur)
    elif choice =='N' or choice == 'No' or choice == 'n' or choice == 'no':
        slow_print('Exiting to menu')
        time.sleep(1)
        start()
