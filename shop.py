import os, time

def shop(self):
    from main import slow_print, load_ascii_art
    from weaponshop import axe_shop
    os.system('clear')
    time.sleep(1)
    loop = True
    while loop:
        os.system('clear')
        load_ascii_art('images/shopkeep.txt')
        slow_print(f'Welcome to the shop {self.name}!\n')
        time.sleep(1)
        slow_print('Please have a look around!\n')
        time.sleep(1)
        print(f'[W]eapons [I]tems [A]rmor | current gold: {self.gold}\n')
        value = input('> ')
        if value == 'w' or value == 'W' or value == 'Weapons' or value == 'weapons' or value == 'weapon' or value == 'Weapon':
            time.sleep(1)
            slow_print('And what kind of weapons would you like to look at?\n')
            time.sleep(1)
            print(f'[S]words [A]xes [B]ows [M]agic staffs | current gold: {self.gold}\n')
            choice = input('> ')
            if choice == 'A' or choice == 'Axe' or choice == "axe" or choice == 'a':
                loop = False
                time.sleep(1)
                slow_print('Axes coming right up!')
                time.sleep(1)
                axe_shop(self)
            elif choice == 'gimme gold':
                self.magic_gold()
            else:
                slow_print('I don\'t have those in stock yet, check back later\n')
        if value =='b' or value == 'bag':
            time.sleep(1)
            for wep in self.weapons:
                slow_print(f'{wep.name}')
        
        if value == 'a' or value == 'A' or value == 'Armor' or value == 'armor':
            slow_print('I don\'t have those in stock yet, check back later\n')
        if value == 'i' or value == 'I' or value == 'Items' or value == 'items':
            slow_print('I don\'t have those in stock yet, check back later\n')

