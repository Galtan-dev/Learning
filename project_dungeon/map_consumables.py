"""
Static entities with non-monster character, like things and places
"""

from abstract_classes import Consumable
import random

# fountain definition class
class Fountain(Consumable):
    object_type = "Item"

    def __str__(self):
        return "fountain"

    # fountain main features are healing and stamina recover
    def __init__(self, identifier, position, cost):
        super().__init__(identifier, position, cost)
        # choosing of random values for refuel
        self.new_hp = random.randint(1, 5)
        self.new_stamina = random.randint(1, 5)





