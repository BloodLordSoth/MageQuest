import os
from chars import Hero, Enemy
from weapons import short_bow, iron_sword

hero = Hero(name="Hero", health = 100)
hero.equip(iron_sword)
enemy = Enemy(name="Enemy", health = 100, weapon=short_bow)

while True:
    os.system("clear")
    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()
