class Items():
    def __init__(self, name, cost, healing, mana_regen):
        self.name = name
        self.cost = cost
        self.healing = healing
        self.mana_regen = mana_regen


mana_pot = Items('Mana Potion', 50, 0, 20)
fb_scroll = Items('Scroll of Fireball', 200, 0, 0)