import random, time
from spells import *
from weapons import *
from main import slow_print

class Player():
    def __init__(self, health, max_hit, name, max_health, mana, max_mana, gold):
        self.health = health
        self.max_hit = max_hit
        self.name = name
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.spells = [fireball, heal, ice_spire]
        self.gold = gold
        self.weapons = []
        self.inventory = {}
    
    def get_gold(self, target):
        gold_loot = random.randint(30, target.gold)
        self.gold += gold_loot
    
    def magic_gold(self):
        self.gold += 30_000

    def get_hit(self, damage):
        self.health -= damage


    def buy_hatchet(self):
        hatchet = Weapon(name="hatchet", damage=20, cost=20)
        if self.gold >= hatchet.cost:
            self.gold -= hatchet.cost
            self.weapons.append(hatchet)
            slow_print('You have purchased the hatchet')
        else:
            slow_print('You don\'nt have enough gold')

    def get_healed(self, healing):
        self.health += healing
        if self.health > self.max_health:
            self.health = self.max_health
            
    
    def heal(self):
        heal = Spells(name="Heal", damage=0, mana_cost=10, healing=20)
        if self.mana >= heal.mana_cost:
            self.mana -= heal.mana_cost
            healing = heal.healing
            self.get_healed(healing)
            slow_print(f'{self.name} heals for {healing}.\n')
            time.sleep(0.5)
            slow_print(f'{self.name} has {self.mana} mana remaining\n')
        else:
            slow_print('You are low on mana\n')
    
    def cast_spell(self, spells, target):
        if self.mana >= spells.mana_cost:
            self.mana -= spells.mana_cost
            damage = random.randint(1, spells.damage)
            target.get_hit(damage)
            time.sleep(0.5)
            slow_print(f"{self.name} casts {spells.name} at {target.name} for {damage} damage!\n")
            time.sleep(0.5)
        else:
            slow_print(f"{self.name} doesn't have enough mana to cast {spells.name}!\n")

        
    def ice_spire(self, target):
        ice_spire = Spells(name="Ice Spire", damage=60, mana_cost=30, healing=0)
        if self.mana >= ice_spire.mana_cost:
            self.mana -= ice_spire.mana_cost
            damage = random.randint(1, ice_spire.damage)
            slow_print(f'{self.name} deals {ice_spire.damage} damage to the {target.name}\n')
            target.get_hit(damage)
        else:
            slow_print('You are low on mana\n')

    def hit(self, target):
        damage = random.randint(1, self.max_hit)
        target.get_hit(damage)
        slow_print(f'{self.name} damages {target.name} for {damage}\n')

    def heal_status(self):
        time.sleep(0.5)
        slow_print(f'{self.name} has {self.mana} mana remaining\n')
    
    def get_status(self):
        slow_print(f"{self.name} has {self.health} health left\n")
        time.sleep(1)


goblin = Player(health=60, max_hit=4, name='Goblin', max_health=60, mana=None, max_mana=None, gold=0)
skeleton = Player(health=120, max_hit=8, name='Skeleton', max_health=120, mana=None, max_mana=None, gold=0)
wyvern = Player(health=350, max_hit=18, name='Wyvern', max_health=350, mana=None, max_mana=None, gold=0)
dragon = Player(health=280, max_hit=22, name='Dragon', max_health=280, mana=None, max_mana=None, gold=0)
boss_dragon = Player(health=1200, max_hit=33, name='Grand Dragon', max_health=1200, mana=None, max_mana=None, gold=0)
wizard = Player(health=60, max_hit=5, name='Wizard', max_health=60, mana=None, max_mana=None, gold=0)