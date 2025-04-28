import random
import os
import time

class Player():
    def __init__(self, health, max_hit, name, max_health):
        self.health = health
        self.max_hit = max_hit
        self.name = name
        self.max_health = max_health
    
    def get_hit(self, damage):
        self.health -= damage

    def hit(self, target):
        damage = random.randint(1, self.max_hit)
        target.get_hit(damage)
    
    def get_status(self):
        os.system('clear')
        time.sleep(1)
        print(f"{self.name} has {self.health} left")