import random, time
from spells import *
from weapons import *
from items import *
from main import slow_print

class Player():
    def __init__(self, health, max_hit, name, max_health, mana, max_mana, gold):
        self.health = health
        self.max_hit = max_hit
        self.name = name
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.spells = []
        self.gold = gold
        self.weapons = []
        self.inventory = {}
        self.items = {}


    
    def get_gold(self, target):
        gold_loot = random.randint(100, target.gold) * 2
        self.gold += gold_loot
        slow_print(f'{self.name} has been awarded {gold_loot} \033[93mgold!\033[0m\n')
    
    def magic_gold(self):
        self.gold += 30_000

    def get_hit(self, damage):
        self.health -= damage

    def heal_me(self):
        heal_price = self.gold // 5
        if self.gold < heal_price or self.gold == 0:
            ('Sorry hero, these spell components aren\'t cheap!')
        else:
            self.gold -= heal_price
            self.health = self.max_health
            self.mana = self.max_mana

    def buy_scroll(self, spell, item):
        if any(s.name == spell.name for s in self.spells):
            slow_print(f'You already know the {spell.name} spell.\n')
            time.sleep(0.5)
        elif self.gold >= item.cost:
            self.gold -= item.cost
            self.spells.append(spell)
            slow_print(f'{spell.name} has been added to your Spellbook.\n')
        else:
            slow_print(f'You don\'t have enough gold to purchase the {item.name}.\n')
        time.sleep(0.5)

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


    def hit(self, target):
        damage = random.randint(1, self.max_hit)
        target.get_hit(damage)
        slow_print(f'{self.name} damages {target.name} for {damage}\n')

    def heal_status(self):
        time.sleep(0.5)
        slow_print(f'{self.name} has {self.mana} mana remaining\n')
    
    def get_status(self):
        slow_print(f"{self.name} has {self.health} health left\n")
        time.sleep(0.5)


goblin = Player(health=60, max_hit=4, name='Goblin', max_health=60, mana=None, max_mana=None, gold=0)
knight = Player(health=60, max_hit=10, name='Knight', max_health=60, mana=None, max_mana=None, gold=300)
skeleton = Player(health=120, max_hit=8, name='Skeleton', max_health=120, mana=None, max_mana=None, gold=0)
wyvern = Player(health=350, max_hit=18, name='Wyvern', max_health=350, mana=None, max_mana=None, gold=0)
dragon = Player(health=280, max_hit=22, name='Dragon', max_health=280, mana=None, max_mana=None, gold=0)
boss_dragon = Player(health=1200, max_hit=33, name='Grand Dragon', max_health=1200, mana=None, max_mana=None, gold=0)
wizard = Player(health=60, max_hit=5, name='Wizard', max_health=60, mana=None, max_mana=None, gold=0)
d_rider = Player(health=2200, max_hit=45, name='Dragon Rider', max_health=2200, mana=None, max_mana=None, gold=1400)