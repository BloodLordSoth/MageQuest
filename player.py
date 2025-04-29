import random
import time
from spells import *
from values import max_hit
from main import slow_print

class Player():
    def __init__(self, health, max_hit, name, max_health, mana, max_mana):
        self.health = health
        self.max_hit = max_hit
        self.name = name
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.spells = [fireball, heal, ice_spire]
    
    def get_hit(self, damage):
        self.health -= damage

    def get_healed(self, healing):
        self.health += healing
    
    def heal(self, target):
        heal = Spells(name="Heal", damage=0, mana_cost=10, healing=20)
        if self.mana >= heal.mana_cost:
            self.mana -= heal.mana_cost
            healing = heal.healing
            target.get_healed(healing)
            slow_print(f'{self.name} has {self.mana} mana left\n')
        else:
            slow_print('You are low on mana\n')

    def fireball(self, target):
        fireball = Spells(name="Fireball", damage=15, mana_cost=10, healing=0)
        if self.mana >= fireball.mana_cost:
            self.mana -= fireball.mana_cost
            damage = random.randint(1, fireball.damage)
            slow_print(f'{self.name} deals {fireball.damage} damage to the {target.name}\n')
            target.get_hit(damage)
        else:
            slow_print('You are low on mana\n')

    def hit(self, target):
        damage = random.randint(1, self.max_hit)
        target.get_hit(damage)

    def heal_status(self):
        time.sleep(0.5)
        slow_print(f'{self.name} has {self.mana} mana remaining\n')
    
    def get_status(self):
        time.sleep(0.5)
        slow_print(f"{self.name} has {self.health} health left\n")

def player_window(name, player):
        print(f'{name}')
        print('----------')
        print('hp    ')
        print(f'{player.health} / {player.max_health}')
        print('mana   ')
        print(f'{player.mana} / {player.max_mana}')
        print(f'Max hit: {max_hit}')
        print('----------')
        print('')
        print('')
        print('')
        print('')
        


goblin = Player(health=60, max_hit=4, name='Goblin', max_health=60, mana=None, max_mana=None)
skeleton = Player(health=120, max_hit=8, name='Skeleton', max_health=120, mana=None, max_mana=None)
wyvern = Player(health=350, max_hit=18, name='Wyvern', max_health=350, mana=None, max_mana=None)
dragon = Player(health=280, max_hit=22, name='Dragon', max_health=280, mana=None, max_mana=None)
boss_dragon = Player(health=1200, max_hit=33, name='Grand Dragon', max_health=1200, mana=None, max_mana=None)
wizard = Player(health=60, max_hit=5, name='Wizard', max_health=60, mana=None, max_mana=None)