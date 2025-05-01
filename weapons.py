import random, time
from main import slow_print

class Weapon:

    def __init__(self, name: str, damage: int, cost: int):
        self.name = name
        self.damage = damage
        self.cost = cost

        def get_wep_dmg(self):
            bonus_damage = random.randint(10, self.damage)
            return bonus_damage
        
        


hatchet = Weapon(name="hatchet", damage=20, cost=120)
iron_sword = Weapon(name="Iron sword", damage=5, cost=10)

short_bow = Weapon(name="Short bow", damage=4, cost=8)

fists = Weapon(name="fists", damage=2, cost=0)
               
               
            