from chars import Character

hero = Character(name="Hero", health = 100)
enemy = Character(name="Enemy", health = 100)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()
