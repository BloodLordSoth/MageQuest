import random, time
from spells import *
from weapons import *
from main import slow_print
from values import max_hit, get_name

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


    def buy_weapon(self, weapon):
        if any(w.name == weapon.name for w in self.weapons):
            slow_print(f'You already own the {weapon.name}.\n')
        elif self.gold >= weapon.cost:
            self.gold -= weapon.cost
            self.weapons.append(weapon)
            slow_print(f'{weapon.name} has been added to your inventory.\n')
        else:
            slow_print(f'You don\'t have enough gold to purchase the {weapon.name}.\n')
        time.sleep(0.5)

    ##for item in self.weapons:
            #if item.name not in self.weapons:
                #slow_print('You already own this item.')
                #time.sleep(0.5)
                #if self.gold >= weapons.cost: 
                    #self.gold -= weapons.cost
                    #self.weapons.append(weapons)
                #else:
                    #slow_print('You don\'t have enough gold\n')
        #time.sleep(1)

    def get_healed(self, healing):
        self.health += healing
        if self.health > self.max_health:
            self.health = self.max_health

    def reduce_spell_cooldowns(self):
        for spell in self.spells:
            spell.reduce_cooldown()
            
    
    def heal(self):
        heal = Spells(name="Heal", damage=0, mana_cost=10, healing=20)
        if self.mana >= heal.mana_cost:
            self.mana -= heal.mana_cost
            healing = heal.healing
            self.get_healed(healing)
            slow_print(f'{self.name} heals for \033[92m{healing}.\033[0m\n')
            time.sleep(0.5)
            slow_print(f'{self.name} has {self.mana} mana remaining\n')
        else:
            slow_print('You are low on mana\n')
    
    def cast_spell(self, spells, target):
        if not spells.is_available():
            slow_print(f"{spells.name} is still on cooldown for {spells.current_cooldown} more turns!\n")
            
        if self.mana >= spells.mana_cost:
            self.mana -= spells.mana_cost
            damage = random.randint(spells.min_dmg, spells.damage)
            target.get_hit(damage)
            time.sleep(0.5)
            slow_print(f"{self.name} casts \033[91m{spells.name}\033[0m at {target.name} for \033[91m{damage} damage!\033[0m\n")
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
d_rider = Player(health=2200, max_hit=45, name='Dragon Rider', max_health=2200, mana=None, max_mana=None, gold=1400)