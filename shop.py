import os, time

def shop(player):
    from main import slow_print, load_ascii_art, wizard_return, load, save
    from weaponshop import axe_shop
    os.system('clear')
    time.sleep(1)
    loop = True
    while loop:
        os.system('clear')
        load_ascii_art('images/shopkeep.txt')
        slow_print(f'Welcome to the shop {player.name}!\n')
        time.sleep(0.5)
        slow_print('Please have a look around!\n')
        time.sleep(0.5)
        print(f'|\ [W]eapons /\ [I]tems /\ [A]rmor /\ [B]ag /\ [L]eave Shop /\ [Q]uit Game /||\ \033[93mGold\033[0m: {player.gold} /\n')
        value = input('> ')
        if value == 'w' or value == 'W' or value == 'Weapons' or value == 'weapons' or value == 'weapon' or value == 'Weapon':
            time.sleep(0.5)
            slow_print('And what kind of weapons would you like to look at?\n')
            time.sleep(0.5)
            print(f'|\ [S]words /\ [A]xes /\ [B]ows /\ [M]agic-Tombs /||\ \033[93mGold\033[0m: {player.gold}\n')
            choice = input('> ')
            if choice == 'A' or choice == 'Axe' or choice == "axe" or choice == 'a':
                loop = False
                slow_print('Axes coming right up hero!')
                time.sleep(0.5)
                axe_shop(player)
            elif choice == 'gimme gold':
                player.magic_gold()
            elif choice == 'b' or choice == 'B' or choice =='Bows' or choice == 'bows':
                time.sleep(0.5)
                slow_print('I don\'t have any bows in stock at the moment...\n')
            elif choice == 's' or choice == 'S' or choice =='swords' or choice == 'Swords':
                time.sleep(0.5)
                slow_print('I don\'t have any swords in stock at the moment\n')
            elif choice == 'm' or choice == 'M' or choice =='Magic-Tomb' or choice == 'magic-tomb':
                time.sleep(0.5)
                slow_print('I don\'t have any Magic-Tombs in stock at the moment...\n')
            else:
                slow_print('I don\'t have those in stock yet, check back later...\n')
        elif value =='b' or value == 'bag' or value == 'B' or value == 'Bag':
            time.sleep(1)
            for wep in player.weapons:
                slow_print(f'{wep.name}')
        elif value == 'q' or value == 'Q' or value == 'Quit' or value == 'quit':
            quit()
        elif value == 'a' or value == 'A' or value == 'Armor' or value == 'armor':
            slow_print('I don\'t have any armor in stock yet, check back later\n')
        elif value == 'i' or value == 'I' or value == 'Items' or value == 'items':
            slow_print('I don\'t have any items in stock yet, check back later\n')
        elif value == 'l' or value == 'Leave' or value == 'L' or value == 'leave':
            save(player)
            wizard_return(player)
