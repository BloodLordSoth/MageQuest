import os
import sys
from player import Player

def combat(player, enemy):
    os.system('clear')
    while player.health > 0 and enemy.health > 0:
        print("Pick an action?\n")
        choice = input('[Attack] [Cast] [Run]: \n')
        if choice  == 'attack' or choice == 'A':
            player.hit(enemy)
            if enemy.health > 0:
                enemy.hit(player)
            player.get_status()
            enemy.get_status()
        elif choice == 'cast':
            spells()
        elif choice == 'run':
            print(f"{player.name} has run away")
            sys.exit()
        else:
            print("Invalid input, please type fight or run")
    
    if player.health < 0:
        print(f'Oh no, {player.name} has been slain')
    elif enemy.health < 0:
        print(f'{enemy.name} has been slain!')

def spells(player, enemy):
    pass