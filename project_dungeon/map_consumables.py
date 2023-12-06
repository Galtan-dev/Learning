from abstract_classes import Consumable
import random

class Fountain(Consumable):
    object_type = "Item"

    def __str__(self):
        return "Treasure"

    def __init__(self, identifier, position, cost):
        super().__init__(identifier, position, cost)
        self.new_hp = random.randint(1, 5)
        self.new_stamina = random.randint(1, 5)

