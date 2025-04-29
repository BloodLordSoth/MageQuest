import os
import sys
import time
from main import slow_print, load_ascii_art, save
from spells import *

def minotaur_combat(self, target):
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
    
    loop = True
    while loop:
        os.system('clear')
        load_ascii_art('images/minotaur.txt')
        print('')
        print(f'{self.name} | Health: {self.health}/{self.max_health} | Mana: {self.mana}/{self.max_mana} | gold: {self.gold}')
        print(f'{target.name} | Health: {target.health}/{target.max_health}\n')
        print(f' [A]ttack [C]ast [I]tem [S]ave [Q]uit: \n')
        choice = input('> ')
        if choice  == 'attack' or choice == 'A' or choice == 'a':
            self.hit(target)
            if target.health > 0:
                target.hit(self)
            self.get_status()
            target.get_status()
        elif choice == 'cast' or choice == 'C' or choice == 'Cast' or choice == 'c':
            spell_cast(self, target)
        elif choice == 'i' or choice == 'I' or choice == 'item' or choice == 'Item':
            pass #item(player)
        elif choice == 'Save' or choice == 's' or choice == 'S' or choice == 'save':
            slow_print('Saving please wait....\n')
            time.sleep(1)
            save(self)
        elif choice == 'q' or choice == 'quit' or choice == 'Q' or choice == 'quit':
            slow_print(f"Are you sure you want to quit?\n")
            type = input('> ')
            if type =="y" or type =='yes':
                sys.exit()
            elif type =='n' or type =="no":
                pass
        else:
            slow_print("Invalid input, please type fight or run\n")
    
        if target.health <= 80:
            loop = False
            min_part2(self, target)

def min_part2(self, target):
    os.system('clear')
    time.sleep(1)
    slow_print('The minotaur enrages unleashing his fury.\n')
    time.sleep(1)
    slow_print('the minotaur lets out a tremendous roar in his rage....\n')
    time.sleep(1)

    loop = True
    while loop:
        load_ascii_art('images/minotaur2.txt')
        print('')
        print(f'{self.name} | Health: {self.health}/{self.max_health} | Mana: {self.mana}/{self.max_mana} | gold: {self.gold}')
        print(f'{target.name} | Health: {target.health}/{target.max_health}\n')
        print(f' [A]ttack [C]ast [I]tem [S]ave [Q]uit: \n')
        choice = input('> ')
        if choice  == 'attack' or choice == 'A' or choice == 'a':
            self.hit(target)
            if target.health > 0:
                target.hit(self)
            self.get_status()
            target.get_status()
        elif choice == 'cast' or choice == 'C' or choice == 'Cast' or choice == 'c':
            spell_cast(self, target)
        elif choice == 'i' or choice == 'I' or choice == 'item' or choice == 'Item':
            pass #item(player)
        elif choice == 'Save' or choice == 's' or choice == 'S' or choice == 'save':
            slow_print('Saving please wait....\n')
            time.sleep(1)
            save(self)
        elif choice == 'q' or choice == 'quit' or choice == 'Q' or choice == 'quit':
            slow_print(f"Are you sure you want to quit?\n")
            type = input('> ')
            if type =="y" or type =='yes':
                sys.exit()
            elif type =='n' or type =="no":
                pass
        else:
            slow_print("Invalid input, please type fight or run\n")

    if self.health < 0:
        death(self, target)
    elif target.health < 0:
        slow_print(f'{target.name} has been slain!')

def item_list(self):
    print('Which item would you like to use?\n')
    print(f'Bag: {self.inventory}')
    value = input('> ')
    if value == '1':
        pass
    elif value == '2':
        pass
    else:
        slow_print('That item isn\'t your inventory.')

def spell_cast(self, target):
    slow_print('What spell would you like to cast?\n')
    for spell in self.spells:
        print(f'{spell.name} (Cost: {spell.mana_cost}, Damage: {spell.damage})')
    cast = input('> ')
    if cast == 'fireball':
        time.sleep(0.5)
        self.cast_spell(fireball, target)
        if target.health > 0:
            target.hit(self)
        self.get_status()
        target.get_status()
    elif cast == 'heal' or cast == 'Heal':
        time.sleep(0.5)
        self.heal()
        target.hit(self)
        self.heal_status()
    elif cast == 'ice spire' or cast == 'Ice spire' or cast == 'Ice Spire':
        time.sleep(0.5)
        self.cast_spell(ice_spire, target)
        if target.health > 0:
            target.hit(self)
        self.get_status()
        target.get_status()
    else:
        ('You do\'nt know that spell')

def death(self, target):
    from main import start
    os.system('clear')
    time.sleep(1)
    load_ascii_art('images/death.txt')
    time.sleep(2)
    slow_print(f'Our hero {self.name} has been laid to rest\n')
    time.sleep(1)
    print('Continue? [Y]es or [N]o\n')
    choice = input('> ')
    if choice == 'Y' or choice == "Yes" or choice == 'y' or choice == 'yes':
        minotaur_combat(self, target)
    elif choice =='N' or choice == 'No' or choice == 'n' or choice == 'no':
        slow_print('Exiting to menu')
        time.sleep(1)
        start()
