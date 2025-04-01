import os
from chars import Hero, Enemy
from weapons import short_bow, iron_sword

hero = Hero(name="", health = 100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health = 100, weapon=short_bow)
run = True
menu = True
play = False
rules = False

def __str__(self):
    return hero.name, hero.health

string_rep = [hero.name, hero.health]

def save():
    f = open("load.txt", "w")
    for info in string_rep:
        f.writelines(str(info) + "\n")
    f.close()

while run:
    while menu:
        print("1: New Game")
        print("2: Load Game")
        print("3: Game Rules")
        print("4: Quit Game")
        print("5: Combat")

        if rules:
            print(f"Welcome to MageQuest{hero.name}! The rules are simple. Slay monsters and level up!")
            print(f"You can insert commands into the console. The commands are as follows:")
            rules = False
            choice = ""
            input = ("")
        else:
            choice = input("")
        
        if choice == "1":
            hero.name = input("what is your name hero? ")
            menu = False
            play = True
        elif choice == "2":
            f = open("load.txt" "\r")
            load_list = f.readlines()
            name = load_list[0]
            health = load_list[1]
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()
        menu = False
        play = True
    if choice == "5":
        while True:
            os.system("clear")
            print(f"Hello {hero.name}! Welcome to MageQuest!")
            hero.attack(enemy)
            enemy.attack(hero)

            hero.health_bar.draw()
            enemy.health_bar.draw()
            input()

    while play:
        save()

        dest = input("")

        if dest == "0":
            play = False
            menu = True
            save()
