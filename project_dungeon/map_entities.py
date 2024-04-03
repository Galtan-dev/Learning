"""
Script for prepreparation of living creature character entities
"""
from abstract_classes import Creature
import random

# class defining hero stats
class Hero(Creature):
    object_type = "hero"

    def __init__(self, identifier, name, position, base_attack, base_ac, damage):
        super().__init__(identifier, position, base_attack, base_ac, damage)
        self.name = name
        self.max_hp = 20
        self.hp = 20
        self.max_stamina = 20
        self.stamina = 20
        self.xp = 0
        self.level = 0
        self.gold = 10
        self.hero_trophy = 0
        self.rank = "No one"


# class defining goblin monster and basic stats and trophies
class Goblin(Creature):
    object_type = "monster"

    def __str__(self):
        return "Goblin"

    def __init__(self, identifier, position, base_attack, base_ac, damage):
        super().__init__(identifier, position, base_attack, base_ac, damage)
        self.hp = random.randint(1, 5)
        self.xp = 10
        self.gold = random.randint(1, 6)
        self.trophy = "small_trophy"

# class defining first boss
class Beholder(Creature):
    object_type = "monster"

    def __str__(self):
        return "Beholder"

    def __init__(self, identifier, position, base_attack, base_ac, damage):
        super().__init__(identifier, position, base_attack, base_ac, damage)
        self.hp = random.randint(7, 12)
        self.position = list(position)
        self.xp = 50
        self.gold = random.randint(8, 15)
        self.trophy = "big_trophy"
