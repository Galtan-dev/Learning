from abstract_classes import AbstractDungeon
from copy import deepcopy
from map_entities import Hero, Goblin, Beholder
from map_consumables import Fountain
import random
import seinerj_create_dungeon
from datetime import datetime
from pathlib import Path
import pickle
import time

class Dungeon(AbstractDungeon):
    def __init__(self, size: tuple, tunnel_number: int, hero_name: str):
        super().__init__(size)
        self.hero = Hero("@", hero_name, [1, 1], 5, 5, 1)
        self.tunnel_number = tunnel_number
        self.hero_name = hero_name
        self.starting_entities = ["goblin", "goblin", "goblin", "fountain", "goblin", "goblin", "goblin", "goblin", "goblin",\
                                      "goblin", "goblin", "goblin", "goblin", "beholder", "fountain"]
        self.entities = []      # self.hero
        self.empty_space = []
        self.message = ""
        self.status = ""
        self.create_dungeon()


    def __str__(self):
        printable_map = ""
        for row in self.current_map:
            for column in row:
                printable_map += column
            printable_map += "\n"
        return printable_map

    def create_dungeon(self):
        maze = seinerj_create_dungeon.maze_start(self.size[1], self.size[0])
        self.dungeon_map = seinerj_create_dungeon.maze_tunels(maze, self.size[1], self.size[0], self.tunnel_number)

        for i in range(0, self.size[1]):
            for j in range(0,  self.size[0]):
                if self.dungeon_map[j][i] == ".":
                    self.empty_space.append(tuple([j, i]))
                else:
                    pass

        self.place_entities(self.starting_entities)
        self.current_map = deepcopy(self.dungeon_map)
        self.empty_space = list(map(list, set(self.empty_space)))
        self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier


    def hero_action(self, action):
        if action == "R":
            # if self.hero.position[1] + 1 < self.size[1] - 1:
            if self.dungeon_map[self.hero.position[0]][self.hero.position[1] + 1] != "▓":
                self.hero.position[1] += 1

        if action == "D":
            # if self.hero.position[1] + 1 < self.size[1] - 1:
            if self.dungeon_map[self.hero.position[0]+1][self.hero.position[1]] != "▓":
                self.hero.position[0] += 1

        if action == "L":
            # if self.hero.position[1] + 1 < self.size[1] - 1:
            if self.dungeon_map[self.hero.position[0]][self.hero.position[1]-1] != "▓":
                self.hero.position[1] -= 1

        if action == "U":
            # if self.hero.position[1] + 1 < self.size[1] - 1:
            if self.dungeon_map[self.hero.position[0]-1][self.hero.position[1]] != "▓":
                self.hero.position[0] -= 1

        if action == "I":
            for entity in self.entities:
                if tuple(self.hero.position) == entity.position and entity == "fountain":
                        self.interact(entity)
                else:
                    self.message = "you tryed to have chat with monster, monster didn´t have much sympathy... "
                    # self.hero.hp -= 2    #  z nějakého důvodu se hra vypne

        elif action == "A":
            fighting = False
            for entity in self.entities:
                if tuple(self.hero.position) == entity.position:
                    if hasattr(entity, "attack"):
                        self.fight(entity)
                        fighting = True
            if not fighting:
                self.message ="Your big sword is hitting air really hard!"
        self.update_map(self.entities)
        self.status = f"Gold:{self.hero.gold}, XP:{self.hero.xp}, Stamina:{self.hero.stamina}, HP:{self.hero.hp}"

        if self.hero.hp < 1:
            self.message += "\nTHIS IS THE END"

    def place_entities(self, entities: list):
        position = random.sample(self.empty_space, len(entities))
        for idx, entity in enumerate(self.starting_entities):
            if position[idx] != (1, 1):
                if entity == "goblin":
                    self.entities.append(Goblin(identifier="\033[38;5;1mg\033[0;0m",
                                                position=position[idx], base_attack=-1,
                                                base_ac=0, damage=1))
                if entity == "beholder":
                    self.entities.append(Beholder(identifier="\033[0;34;1mB\033[0;0m",
                                                  position=position[idx], base_attack=-3,
                                                  base_ac=2, damage=3))
                if entity =="fountain":
                    self.entities.append(Fountain(identifier="\033[0;34;1mU\033[0;0m",
                                                  position=position[idx], cost=5))


        for entity in self.entities:
            self.dungeon_map[entity.position[0]][entity.position[1]] = entity.map_identifier

    def update_map(self, entities: list):
        # TODO implement entities
        self.current_map = deepcopy(self.dungeon_map)
        self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier

    def fight(self, monster):
        hero_roll = self.hero.attack()
        monster_roll = monster.attack()
        if hero_roll["attack_roll"] > monster.base_ac:
            monster.hp -= hero_roll["inflicted_damage"]
            if monster.hp > 0:
                self.message = f"Hero inflicted {hero_roll['inflicted_damage']}"
            else:
                self.message = f"Hero inflicted {hero_roll['inflicted_damage']} damage and slain {monster}"
                self.hero.gold += monster.gold
                self.hero.xp += 1
                self.dungeon_map[monster.position[0]][monster.position[1]] = "."
                self.entities.remove(monster)
        if monster_roll["attack_roll"] > self.hero.base_ac:
            self.message += f"\nMonster inflicted {monster_roll['inflicted_damage']} damage"
            self.hero.hp -= monster_roll['inflicted_damage']
            if self.hero.hp < 1:
                self.message += f"{self.hero.name} have been slained by {monster}"
        self.message += f"\nMonster HP: {monster.hp}"
        self.hero.stamina -= 2

    def interact(self, Fountain):
        self.hero.hp += Fountain.new_hp
        self.hero.stamina += Fountain.new_stamina

    def save_dungeon(self):
        date_time = datetime.strftime(datetime.now(), "%d-%m-%Y_%H-%M-%S")
        s_path = Path(".") / "saved_games" / "{}_{}".format(self.hero.name, date_time)
        Path.mkdir(s_path)

        s_map = "%s_%s_map.dng" % (self.hero.name, date_time)
        with open(s_path / s_map, "wb") as f:
            pickle.dump(self.dungeon_map, f)

        s_entities = "%s_%s_entities.dng" % (self.hero.name, date_time)
        with open(s_path / s_entities, "wb") as f:
            pickle.dump(self.entities, f)

    def load_dungeon(self):
        l_path = Path(".").resolve() / "saved_games"
        print("Saved games available: ")
        number = 0

        for saved_game in l_path.iterdir():
            print(saved_game)
            number = number + 1

        if number == 0:
            print("There are no saved games available")
            time.sleep(2)
            exit(0)

        l_file = input("Which game do you wanna play? insert in format heroname: ")
        l_path = l_path / l_file

        with open(l_path / (l_file + "_map.dng"), "rb") as f:
            self.dungeon_map = pickle.load(f)
        with open(l_path / (l_file + "_entities.dng"), "rb") as f:
            self.entities = pickle.load(f)
        for entity in self.entities:
            if entity.map_identifier == self.hero.map_identifier:
                self.hero.position = entity.position







# backupp
#
#
#
# from abstract_classes import AbstractDungeon
# from copy import deepcopy
# from map_entities import Hero, Goblin
# import random
# import seinerj_create_dungeon
# import datetime
#
# class Dungeon(AbstractDungeon):
#     def __init__(self, size: tuple, tunnel_number: int, hero_name: str):
#         super().__init__(size)
#         self.hero = Hero("@", hero_name, [1, 1], 5, 5, 1)
#         self.tunnel_number = tunnel_number
#         self.hero_name = hero_name
#         self.starting_entities = ["goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin", "goblin",\
#                                       "goblin", "goblin", "goblin", "goblin"]
#         self.entities = []
#         self.empty_space = []
#         self.message = ""
#         self.create_dungeon()
#
#
#     def __str__(self):
#         printable_map = ""
#         for row in self.current_map:
#             for column in row:
#                 printable_map += column
#             printable_map += "\n"
#         return printable_map
#
#     def create_dungeon(self):
#         maze = seinerj_create_dungeon.maze_start(self.size[1], self.size[0])
#         self.dungeon_map = seinerj_create_dungeon.maze_tunels(maze, self.size[1], self.size[0], self.tunnel_number)
#
#         for i in range(0, self.size[1]):
#             for j in range(0,  self.size[0]):
#                 if self.dungeon_map[j][i] == ".":
#                     self.empty_space.append(tuple([j, i]))
#                 else:
#                     pass
#
#         self.place_entities(self.starting_entities)
#         self.current_map = deepcopy(self.dungeon_map)
#         self.empty_space = list(map(list, set(self.empty_space)))
#         self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier
#
#
#     def hero_action(self, action):
#         if action == "R":
#             # if self.hero.position[1] + 1 < self.size[1] - 1:
#             if self.dungeon_map[self.hero.position[0]][self.hero.position[1] + 1] != "▓":
#                 self.hero.position[1] += 1
#
#         if action == "D":
#             # if self.hero.position[1] + 1 < self.size[1] - 1:
#             if self.dungeon_map[self.hero.position[0]+1][self.hero.position[1]] != "▓":
#                 self.hero.position[0] += 1
#
#         if action == "L":
#             # if self.hero.position[1] + 1 < self.size[1] - 1:
#             if self.dungeon_map[self.hero.position[0]][self.hero.position[1]-1] != "▓":
#                 self.hero.position[1] -= 1
#
#         if action == "U":
#             # if self.hero.position[1] + 1 < self.size[1] - 1:
#             if self.dungeon_map[self.hero.position[0]-1][self.hero.position[1]] != "▓":
#                 self.hero.position[0] -= 1
#
#         elif action == "A":
#             fighting = False
#             for entity in self.entities:
#                 print(self.hero.position)
#                 print(entity.position)
#                 print("break")
#                 if tuple(self.hero.position) == entity.position:
#                     if hasattr(entity, "attack"):
#                         self.fight(entity)
#                         fighting = True
#             if not fighting:
#                 self.message ="Your big sword is hitting air really hard!"
#         self.update_map(self.entities)
#
#         if self.hero.hp < 1:
#             self.message += "\nTHIS IS THE END"
#
#     def place_entities(self, entities: list):
#         position = random.sample(self.empty_space, len(entities))
#         for idx, entity in enumerate(self.starting_entities):
#             if entity == "goblin":
#                 self.entities.append(Goblin(identifier="\033[38;5;1mg\033[0;0m",
#                                             position=position[idx], base_attack=-1,
#                                             base_ac=0, damage=1))
#         for entity in self.entities:
#             self.dungeon_map[entity.position[0]][entity.position[1]] = entity.map_identifier
#
#     def update_map(self, entities: list):
#         # TODO implement entities
#         self.current_map = deepcopy(self.dungeon_map)
#         self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier
#
#     def fight(self, monster):
#         hero_roll = self.hero.attack()
#         monster_roll = monster.attack()
#         if hero_roll["attack_roll"] > monster.base_ac:
#             monster.hp -= hero_roll["inflicted_damage"]
#             if monster.hp > 0:
#                 self.message = f"Hero inflicted {hero_roll['inflicted_damage']}"
#             else:
#                 self.message = f"Hero Hero inflicted {hero_roll['inflicted_damage']} damage and slain {monster}"
#                 self.hero.gold += monster.gold
#                 self.hero.xp += 1
#                 self.dungeon_map[monster.position[0]][monster.position[1]] = "."
#                 self.entities.remove(monster)
#         if monster_roll["attack_roll"] > self.hero.base_ac:
#             self.message += f"\nMonster inflicted {monster_roll['inflicted_damage']} damage"
#             self.hero.hp -= monster_roll['inflicted_damage']
#             if self.hero.hp < 1:
#                 self.message += f"{self.hero.name} have been slained by {monster}"
#         self.message += f"\nHero HP: {self.hero.hp}  Monster HP: {monster.hp}"
#

