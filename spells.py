import random

class Spells():
    def __init__(self, name, damage, min_dmg, mana_cost, healing, cooldown_time=0):
        self.name = name
        self.damage = damage
        self.min_dmg = min_dmg
        self.mana_cost = mana_cost
        self.healing = healing
        self.cooldown_time = cooldown_time
        self.current_cooldown = 0

    def to_dict(self):
        return {
            "name": self.name,
            "damage": self.damage,
            "min_dmg": self.min_dmg,
            "mana_cost": self.mana_cost,
            "healing": self.healing
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            damage=data["damage"],
            min_dmg=data["min_dmg"],
            mana_cost=data["mana_cost"],
            healing=data.get("healing", 0)
        )

    def get_damage(self):
        bonus_damage = random.randint(self.min_dmg, self.damage)
        return bonus_damage
    
    def heal_bonus(self):
        bonus_healing = random.randint(self.min_dmg, self.healing)
        return self.healing + bonus_healing
    
    def is_available(self):
        return self.current_cooldown == 0
    
    def start_cooldown(self):
        self.current_cooldown = self.cooldown_time

    def reduce_cooldown(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1


#Fire
fireball = Spells(name="Fireball", damage=20, min_dmg=10, mana_cost=20, healing=0, cooldown_time=3)
fire_strike = Spells(name="Fire Strike", damage=30, min_dmg=2, mana_cost=20, healing=0, cooldown_time=1)
fire_storm = Spells(name="Fire Storm", damage=120, min_dmg=2, mana_cost=35, healing=0, cooldown_time=2)

#Ice
freeze = Spells(name="Freeze", damage=15, min_dmg=2, mana_cost=10, healing=0, cooldown_time=1)
blizzard = Spells(name="Blizzard", damage=30, min_dmg=2, mana_cost=15, healing=0, cooldown_time=1)
ice_spire = Spells(name="Ice Spire", damage=120, min_dmg=60, mana_cost=30, healing=0, cooldown_time=3)


#Necromancy
corrosion = Spells(name="Corrosion", damage=10, min_dmg=2, mana_cost=10, healing=0, cooldown_time=2)
plague = Spells(name="Plague", damage=10, min_dmg=2, mana_cost=10, healing=0, cooldown_time=2)
greater_corrosion = Spells(name="Greater Corruption", damage=10, min_dmg=2, mana_cost=10, healing=0, cooldown_time=2)

#Utility
teleport = Spells(name="Teleport", damage=0, min_dmg=2, mana_cost=20, healing=0, cooldown_time=2)
heal = Spells(name="Heal", damage=0, min_dmg=15, mana_cost=10, healing=30, cooldown_time=2)
greater_heal = Spells(name="Greater Heal", damage=0, min_dmg=2, mana_cost=20, healing=40, cooldown_time=2)
divine_prot = Spells(name="Divine Protection", damage=0, min_dmg=2, mana_cost=40, healing=0, cooldown_time=2)