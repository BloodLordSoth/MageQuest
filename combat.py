import os, time, sys
from main import slow_print, load_ascii_art, save, wizard_return, save
from spells import *
from player import *

def minotaur_dialogue(player):
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
    minotaur_combat(player)
    
def minotaur_combat(player):
    target = Player(health=100, max_hit=30, name='Minotaur', max_health=100, mana=None, max_mana=None, gold=220)
    game_state = {
    "location": "min_pt1",
    "current_enemy": 'Minotaur',
    "player": player,
}
    loop = True
    while loop:
        os.system('clear')
        load_ascii_art('images/minotaur.txt')
        print('')
        print(f'{player.name} | \033[91mHealth:\033[0m {player.health}/{player.max_health} | \033[94mMana:\033[0m {player.mana}/{player.max_mana} | \033[93mgold\033[0m: {player.gold}')
        print('-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-')
        print(f'{target.name} | \033[91mHealth:\033[0m {target.health}/{target.max_health}\n')
        print(f'|\ [A]ttack /\ [C]ast /\ [I]tem /\ [S]ave /\ [Q]uit: /| \n')
        choice = input('> ')
        if choice  == 'attack' or choice == 'A' or choice == 'a':
            player.hit(target)
            if target.health > 0:
                target.hit(player)
            player.get_status()
            target.get_status()
        elif choice == 'cast' or choice == 'C' or choice == 'Cast' or choice == 'c':
            spell_cast(player, target)
        elif choice == 'i' or choice == 'I' or choice == 'item' or choice == 'Item':
            pass #item(player)
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
    
        if player.health <= 0:
            death(player, game_state)   
        elif target.health <= 80:
            loop = False
            min_part2(player, target)

def min_part2(player, target):
    game_state = {
    "location": "min_pt2",
    "current_enemy": 'Minotaur',
    "player": player,
}
    os.system('clear')
    time.sleep(1)
    slow_print('\033[91mThe minotaur enrages unleashing his fury.\033[0m\n')
    time.sleep(1)
    slow_print('\033[91mthe minotaur lets out a tremendous roar in his rage....\033[0m\n')
    time.sleep(1)

    loop = True
    while loop:
        os.system('clear')
        print('\033[91m')
        load_ascii_art('images/minotaur2.txt')
        print('\033[0m')
        print(f'{player.name} | \033[91mHealth\033[0m: {player.health}/{player.max_health} | \033[94mMana\033[0m: {player.mana}/{player.max_mana} | \033[93mgold\033[0m: {player.gold}')
        print('-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-')
        print(f'{target.name} | \033[91mHealth:\033[0m {target.health}/{target.max_health}\n')
        print(f'|\ [A]ttack /\ [C]ast /\ [I]tem /\ [S]ave /\ [Q]uit: /| \n')
        choice = input('> ')
        if choice  == 'attack' or choice == 'A' or choice == 'a':
            player.hit(target)
            if target.health > 0:
                target.hit(player)
            player.get_status()
            target.get_status()
        elif choice == 'cast' or choice == 'C' or choice == 'Cast' or choice == 'c':
            spell_cast(player, target)
        elif choice == 'i' or choice == 'I' or choice == 'item' or choice == 'Item':
            pass #item(player)
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

        if player.health <= 0:
            death(player, game_state)

        if target.health <= 0:
            loop = False
            os.system('clear')
            time.sleep(1)
            slow_print(f'{target.name} has been slain!\n')
            time.sleep(1)
            slow_print(f'{player.name} has been awarded {target.gold} \033[93mgold!\033[0m\n')
            player.get_gold(target)
            save(player)
            time.sleep(1)
            wizard_return(player)

def item_list(player):
    print('Which item would you like to use?\n')
    print(f'Bag: {player.inventory}')
    value = input('> ')
    if value == '1':
        pass
    elif value == '2':
        pass
    else:
        slow_print('That item isn\'t your inventory.')

def spell_cast(player, target):
    slow_print('What spell would you like to cast?\n')
    for spell in player.spells:
        print(f'{spell.name} (Cost: {spell.mana_cost}, Damage: {spell.damage})')
    cast = input('> ')
    if cast == 'fireball':
        time.sleep(0.5)
        player.cast_spell(fireball, target)
        if target.health > 0:
            target.hit(player)
        player.get_status()
        target.get_status()
        player.reduce_spell_cooldowns()
    elif cast == 'heal' or cast == 'Heal':
        time.sleep(0.5)
        player.heal()
        target.hit(player)
        player.heal_status()
        player.reduce_spell_cooldowns()
    elif cast == 'ice spire' or cast == 'Ice spire' or cast == 'Ice Spire':
        time.sleep(0.5)
        player.cast_spell(ice_spire, target)
        if target.health > 0:
            target.hit(player)
        player.get_status()
        target.get_status()
        player.reduce_spell_cooldowns()
    else:
        ('You do\'nt know that spell')

def death(player, game_state):
    from main import start
    from ch1 import resume_game
    os.system('clear')
    time.sleep(1)
    load_ascii_art('images/death.txt')
    time.sleep(2)
    slow_print(f'Our hero {player.name} has been laid to rest\n')
    time.sleep(1)
    print('Continue? \033[92m[Y]es\033[0m or \033[91m[N]o\033[0m \n')
    choice = input('> ')
    if choice == 'Y' or choice == "Yes" or choice == 'y' or choice == 'yes':
        resume_game(game_state)
    elif choice =='N' or choice == 'No' or choice == 'n' or choice == 'no':
        slow_print('Exiting to menu\n')
        time.sleep(1)
        start()
    else:
        time.sleep(1)
        slow_print('Invalid response mortal.\n')

def drider_combat(player):
    game_state = {
    "location": "d_rider",
    "current_enemy": 'Dragon Rider',
    "player": player,
}
    target = Player(health=200, max_hit=45, name='Dragon Rider', max_health=200, mana=None, max_mana=None, gold=1400)
    os.system('clear')
    slow_print('You\'ve reached the top of the tower, the air hangs thick.\n')
    time.sleep(1)
    slow_print('The putrid smell of decaying carcasses engulf your senses.\n')
    time.sleep(1)
    slow_print('Without having the time to regain your composure.... \n')
    os.system('clear')
    time.sleep(1)
    slow_print('You\'re nearly knocked back from the force of thunderous flapping...\n')
    time.sleep(1)
    slow_print('The \033[91mDragon-rider\033[0m emerges....')
    time.sleep(1)
    os.system('clear')
    
    loop = True
    while loop:
        os.system('clear')
        load_ascii_art('images/dragonrider.txt')
        print('')
        print(f'{player.name} | \033[91mHealth:\033[0m {player.health}/{player.max_health} | \033[94mMana:\033[0m {player.mana}/{player.max_mana} | \033[93mgold\033[0m: {player.gold}')
        print('-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-')
        print(f'{target.name} | \033[91mHealth:\033[0m {target.health}/{target.max_health}\n')
        print(f'|\ [A]ttack /\ [C]ast /\ [I]tem /\ [S]ave /\ [Q]uit: /| \n')
        choice = input('> ')
        if choice  == 'attack' or choice == 'A' or choice == 'a':
            player.hit(target)
            if target.health > 0:
                target.hit(player)
            player.get_status()
            target.get_status()
        elif choice == 'cast' or choice == 'C' or choice == 'Cast' or choice == 'c':
            spell_cast(player, target)
        elif choice == 'i' or choice == 'I' or choice == 'item' or choice == 'Item':
            pass #item(player)
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

        if player.health <= 0:
            death(player, game_state)
        if target.health <= 190:
            loop = False
            drider2_combat(player, target)

def drider2_combat(player, target):
    game_state = {
    "location": "d_rider2",
    "current_enemy": 'Dragon Rider',
    "player": player,
}
    os.system('clear')
    time.sleep(1)
    slow_print('\033[91mThe dragon thrashes about in panic and rage...\033[0m\n')
    time.sleep(1)
    slow_print('\033[91mIn the chaos, the dragon rider falls from the sky...\033[0m\n')
    time.sleep(1)
    slow_print('\033[91mThe enraged dragon now lunges at you!\033[0m \n')
    time.sleep(1)

    loop = True
    while loop:
        print('\033[92m')
        load_ascii_art('images/dragonattack.txt')
        print('\033[0m')
        print(f'{player.name} | \033[91mHealth\033[0m: {player.health}/{player.max_health} | \033[94mMana\033[0m: {player.mana}/{player.max_mana} | \033[93mgold\033[0m: {player.gold}')
        print('-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-')
        print(f'{target.name} | \033[91mHealth\033[0m: {target.health}/{target.max_health}\n')
        print(f'|\ [A]ttack /\ [C]ast /\ [I]tem /\ [S]ave /\ [Q]uit:/| \n')
        choice = input('> ')
        if choice  == 'attack' or choice == 'A' or choice == 'a':
            player.hit(target)
            if target.health > 0:
                target.hit(player)
            player.get_status()
            target.get_status()
        elif choice == 'cast' or choice == 'C' or choice == 'Cast' or choice == 'c':
            spell_cast(player, target)
        elif choice == 'i' or choice == 'I' or choice == 'item' or choice == 'Item':
            pass #item(player)
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

        if player.health <= 0:
            death(player, game_state)

        if target.health <= 0:
            loop = False
            os.system('clear')
            load_ascii_art('images/empty.txt')
            time.sleep(1)
            slow_print(f'{target.name} has been slain!\n')
            time.sleep(1)
            slow_print(f'{player.name} has been awarded {target.gold} \033[93mgold!\033[0m\n')
            player.get_gold(target)
            time.sleep(1)
            wizard_return(player)

    
def knight_combat(player, target):
    game_state = {
    "location": "knight_combat",
    "current_enemy": target,
    "player": player,
}
    loop = True
    while loop:
        os.system('clear')
        load_ascii_art('images/knightcombat.txt')
        print('')
        print(f'{player.name} | \033[91mHealth:\033[0m {player.health}/{player.max_health} | \033[94mMana:\033[0m {player.mana}/{player.max_mana} | \033[93mgold\033[0m: {player.gold}')
        print('-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-')
        print(f'{target.name} | \033[91mHealth:\033[0m {target.health}/{target.max_health}\n')
        print(f'|\ [A]ttack /\ [C]ast /\ [I]tem /\ [W]izard /\ [S]ave /\ [Q]uit: /| \n')
        choice = input('> ')
        if choice  == 'attack' or choice == 'A' or choice == 'a':
            player.hit(target)
            if target.health > 0:
                target.hit(player)
            player.get_status()
            target.get_status()
        elif choice == 'cast' or choice == 'C' or choice == 'Cast' or choice == 'c':
            spell_cast(player, target)
        elif choice == 'i' or choice == 'I' or choice == 'item' or choice == 'Item':
            pass #item(player)
        elif choice == 'Save' or choice == 's' or choice == 'S' or choice == 'save':
            slow_print('Saving please wait....\n')
            time.sleep(1)
            save(player)
        elif choice == 'w' or choice == 'W' or choice == 'Wizard' or choice == "wizard":
            slow_print('You hold the amulet in your hand, and the world shimmers away...')
            time.sleep(1)
            wizard_return(player, game_state)
        elif choice == 'q' or choice == 'quit' or choice == 'Q' or choice == 'quit':
            slow_print(f"Are you sure you want to quit?\n")
            type = input('> ')
            if type =="y" or type =='yes':
                sys.exit()
            elif type =='n' or type =="no":
                pass
        else:
            slow_print("Invalid input, please try again.\n")
    
        if target.health <= 0:
            loop = False
            os.system('clear')
            load_ascii_art('images/empty.txt')
            time.sleep(1)
            slow_print(f'{target.name} has been slain!\n')
            time.sleep(1)
            player.get_gold(target)
            save(player)
            time.sleep(1)
            knight_combat2(player)

def knight_combat2(player):
    from ch1 import prison
    target = Player(health=60, max_hit=10, name='Knight', max_health=60, mana=None, max_mana=None, gold=300)
    game_state = {
    "location": "knight_combat2",
    "current_enemy": 'Knight',
    "player": player,
}
    time.sleep(1)
    load_ascii_art('images/empty.txt')
    slow_print('Another knight rushes in to replace his fallen comrade.\n prepare once more for combat!\n')
    time.sleep(1)
    loop = True
    while loop:
        os.system('clear')
        load_ascii_art('images/knightcombat.txt')
        print('')
        print(f'{player.name} | \033[91mHealth:\033[0m {player.health}/{player.max_health} | \033[94mMana:\033[0m {player.mana}/{player.max_mana} | \033[93mgold\033[0m: {player.gold}')
        print('-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-=*=-')
        print(f'{target.name} | \033[91mHealth:\033[0m {target.health}/{target.max_health}\n')
        print(f'|\ [A]ttack /\ [C]ast /\ [I]tem /\ [W]izard /\ [S]ave /\ [Q]uit: /| \n')
        choice = input('> ')
        if choice  == 'attack' or choice == 'A' or choice == 'a':
            player.hit(target)
            if target.health > 0:
                target.hit(player)
            player.get_status()
            target.get_status()
        elif choice == 'cast' or choice == 'C' or choice == 'Cast' or choice == 'c':
            spell_cast(player, target)
        elif choice == 'i' or choice == 'I' or choice == 'item' or choice == 'Item':
            pass #item(player)
        elif choice == 'Save' or choice == 's' or choice == 'S' or choice == 'save':
            slow_print('Saving please wait....\n')
            time.sleep(1)
            save(player)
        elif choice == 'w' or choice == 'W' or choice == 'Wizard' or choice == "wizard":
            slow_print('You hold the amulet in your hand, and the world shimmers away...')
            time.sleep(1)
            wizard_return(player, game_state)
        elif choice == 'q' or choice == 'quit' or choice == 'Q' or choice == 'quit':
            slow_print(f"Are you sure you want to quit?\n")
            type = input('> ')
            if type =="y" or type =='yes':
                sys.exit()
            elif type =='n' or type =="no":
                pass
        else:
            slow_print("Invalid input, please try again.\n")
    
        if target.health <= 0:
            loop = False
            os.system('clear')
            load_ascii_art('images/empty.txt')
            time.sleep(1)
            slow_print(f'{target.name} has been slain!\n')
            time.sleep(1)
            player.get_gold(target)
            save(player)
            time.sleep(1)
            prison(player)