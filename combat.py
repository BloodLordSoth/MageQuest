import os
import sys
import time
from main import slow_print, load_ascii_art, save

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

    while player.health > 0 and minotaur.health > 0:
        os.system('clear')
        load_ascii_art('images/minotaur.txt')
        print('')
        print(f'{player.name}: hp: {player.health}/{player.max_health} mana: {player.mana}/{player.max_mana}  |  {minotaur.name}: hp: {minotaur.health}/{minotaur.max_health}             \n')
        print(f' [A]ttack [C]ast [I]tem [S]ave [Q]uit: \n')
        choice = input('> ')
        if choice  == 'attack' or choice == 'A' or choice == 'a':
            player.hit(minotaur)
            if minotaur.health > 0:
                minotaur.hit(player)
            player.get_status()
            minotaur.get_status()
        elif choice == 'cast' or choice == 'C' or choice == 'Cast' or choice == 'c':
            spells(player, minotaur)
        elif choice == 'Save' or choice == 's' or choice == 'S' or choice == 'save':
            slow_print('Saving please wait....\n')
            time.sleep(1)
            save(player)
        elif choice == 'q' or choice == 'quit' or choice == 'Q' or choice == 'quit':
            slow_print(f"Are you sure you want to quit?\n")
            type = input('> ')
            if type =="y" or type =='yes':
                sys.exit()
            elif type =='n' or type =="no":
                pass
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
        minotaur.hit(player)
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
