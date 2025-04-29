class Weapon:

    def __init__(self, name: str, damage: int, cost: int) -> None:
        self.name = name
        self.damage = damage
        self.cost = cost

iron_sword = Weapon(name="Iron sword",
                    damage=5,
                    cost=10)


short_bow = Weapon(name="Short bow",
                   damage=4,
                   cost=8)

fists = Weapon(name="fists",
               damage=2,
               cost=0)
               
               
            