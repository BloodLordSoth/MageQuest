import random

class Spells():
    def __init__(self, name, damage, mana_cost, healing):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.healing = healing

    def get_damage(self):
        bonus_damage = random.randint(0, 20)
        return self.damage + bonus_damage
    
    def heal_bonus(self):
        bonus_healing = random.randint(0, 20)
        return self.healing + bonus_healing


#Fire
fireball = Spells(name="Fireball", damage=5, mana_cost=15, healing=0)
fire_strike = Spells(name="Fire Strike", damage=30, mana_cost=20, healing=0)
fire_storm = Spells(name="Fire Storm", damage=120, mana_cost=35, healing=0)

#Ice
freeze = Spells(name="Freeze", damage=15, mana_cost=10, healing=0)
blizzard = Spells(name="Blizzard", damage=30, mana_cost=15, healing=0)
ice_spire = Spells(name="Ice Spire", damage=120, mana_cost=30, healing=0)


#Necromancy
corrosion = Spells(name="Corrosion", damage=10, mana_cost=10, healing=0)
plague = Spells(name="Plague", damage=10, mana_cost=10, healing=0)
greater_corrosion = Spells(name="Greater Corruption", damage=10, mana_cost=10, healing=0)

#Utility
teleport = Spells(name="Teleport", damage=0, mana_cost=20, healing=0)
heal = Spells(name="Heal", damage=0, mana_cost=10, healing=20)
greater_heal = Spells(name="Greater Heal", damage=0, mana_cost=20, healing=40)
divine_prot = Spells(name="Divine Protection", damage=0, mana_cost=40, healing=0)