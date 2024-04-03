"""
Script where moust of function and calculation of dungeon are implemented.
Is inicialized from main.script
"""
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
    """
    class constructor
    """
    def __init__(self, size: tuple, tunnel_number: int, hero_name: str):
        super().__init__(size)
        self.hero = Hero("@", hero_name, [1, 1], 5, 5, 1)
        self.tunnel_number = tunnel_number
        self.hero_name = hero_name
        # list of monsters player wants in dungeon
        self.starting_entities = ["goblin", "goblin", "goblin", "fountain", "goblin", "goblin",
                                  "goblin", "goblin", "goblin", "goblin", "goblin",
                                  "goblin", "goblin"]
        # predefining of variables
        self.entities = []
        self.empty_space = []
        # self.cond = 0
        self.manhattan_distance = None
        self.message = ""
        self.status = ""
        self.create_dungeon()



    def __str__(self):
        """
        function for map printing
        """
        printable_map = ""
        # print elements of list of lists, first columns and then rows
        for row in self.current_map:
            for column in row:
                printable_map += column
            printable_map += "\n"
        return printable_map

    def create_dungeon(self):
        """
        function for dungeon design. There is used script seinerj_create_dungeon
        where most calculation occur
        """
        # create maze from set height and width using diferent script
        maze = seinerj_create_dungeon.maze_start(self.size[1], self.size[0])
        # declare create dungeon as self.dungeon_map
        self.dungeon_map = seinerj_create_dungeon.maze_tunels(maze,
                                                              self.size[1],
                                                              self.size[0],
                                                              self.tunnel_number)

        # create list of blank space that is represented by point
        # for placing entities
        for i in range(0, self.size[1]):
            for j in range(0,  self.size[0]):
                if self.dungeon_map[j][i] == ".":
                    self.empty_space.append(tuple([j, i]))
                else:
                    pass

        # run inserting entities to blanks
        self.place_entities(self.starting_entities)
        # save preprepared map to current map which is displayed
        self.current_map = deepcopy(self.dungeon_map)
        # empty space storage
        self.empty_space = list(map(list, set(self.empty_space)))
        # inserting hero identifier to map
        self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier


    def hero_action(self, action):
        """
        function defining action which hero can take.
        Status message is designed here too a some other function are
        inicialized from here.
        """
        # action from script main. By letter is used specified if section
        if action == "R":
            # if condition that prevents going through the walls
            if self.dungeon_map[self.hero.position[0]][self.hero.position[1] + 1] != "▓":
                # position update
                self.hero.position[1] += 1
                # running functions that are related to movement
                self.beholder_fireball()
                self.beholder_move()
                # next 3 if statements are the same except for that they are for different directions

        if action == "D":
            if self.dungeon_map[self.hero.position[0]+1][self.hero.position[1]] != "▓":
                self.hero.position[0] += 1
                self.beholder_fireball()
                self.beholder_move()

        if action == "L":
            if self.dungeon_map[self.hero.position[0]][self.hero.position[1]-1] != "▓":
                self.hero.position[1] -= 1
                self.beholder_fireball()
                self.beholder_move()

        if action == "U":
            if self.dungeon_map[self.hero.position[0]-1][self.hero.position[1]] != "▓":
                self.hero.position[0] -= 1
                self.beholder_fireball()
                self.beholder_move()

        # interaction that define interactions with fountain that is refueling point
        if action == "I":
            for entity in self.entities:
                # next statement interact with fountain
                if tuple(self.hero.position) == entity.position and\
                        entity.map_identifier == "\033[0;34;1mU\033[0;0m":
                    self.interact(entity)
                    self.message = f"You rested well... +HP,+STAMINA"
                    # next statements is for posibility that hero wants to interact with monsters
                    # condition control if there is some diferent entity and which entity it is
                elif tuple(self.hero.position) == entity.position and \
                        entity.map_identifier == "\033[38;5;1mg\033[0;0m":
                    self.message = "you tryed to have chat with monster, monster didn´t " \
                                   "have much sympathy... -HP"
                    self.hero.hp -= 2
                elif tuple(self.hero.position) == entity.position and \
                        entity.map_identifier == "\033[0;34;1mB\033[0;0m":
                    self.message = "You patted Beholder on the head, and a moment " \
                                   "after he recovered," \
                                   " he slammed you into the ground."
                    self.hero.hp -= 1000

        # last action is attack
        elif action == "A":
            fighting = False
            # iterate throught entity list and control if some entity have the same location as hero
            for entity in self.entities:
                if tuple(self.hero.position) == entity.position:
                    if hasattr(entity, "attack"):
                        # run fight function
                        self.fight(entity)
                        # run leveling function
                        self.leveling()
                        fighting = True

            # for posibility when hero attack on blank space
            if not fighting:
                self.message ="Your big sword is hitting air really hard!"

            # run fireabll fucntion
            self.beholder_fireball()

        # after action run map update function that print changes
        self.update_map(self.entities)
        # update of status message informations
        self.status = f"XP:{self.hero.xp} Stamina:{self.hero.stamina} HP:{self.hero.hp} " \
                      f"Trophy:{self.hero.hero_trophy}\nGold:{self.hero.gold} " \
                      f"Damage:{self.hero.base_attack} AC:{self.hero.base_ac}" \
                      f" Level:{self.hero.level}"

        # if some action leads to dead of hero that is solved there
        if self.hero.hp < 1:
            self.message += "\nTHIS IS THE END"

    def leveling(self):
        """
        function for leveling of hero and upgrading basic stats
        """
        # control if hero have enough experince for level up
        if self.hero.xp >= 10:
            # modify stats
            self.hero.level += 1
            self.hero.base_attack += 2
            self.hero.base_ac += 1
            # reset experinces
            self.hero.xp = 0


    def place_entities(self, entities: list):
        """
        function for placing entities to designed dungeon before play
        """
        # choose random position from list of empty space
        position = random.sample(self.empty_space, len(entities))
        # iterate through list of wanted entites and palcing thm into list of entities
        for idx, entity in enumerate(self.starting_entities):
            if position[idx] != (1, 1):
                # condition distinctive to type of entity
                if entity == "goblin":
                    # entities have some stats too, important is identifier and position
                    self.entities.append(Goblin(identifier="\033[38;5;1mg\033[0;0m",
                                                position=position[idx], base_attack=-1,
                                                base_ac=0, damage=1))
                if entity =="fountain":
                    self.entities.append(Fountain(identifier="\033[0;34;1mU\033[0;0m",
                                                  position=position[idx], cost=5))

        # after placing entities to list of acite entities, their indetifiers are placed
        # to dungeon map on specified position that is after that update
        for entity in self.entities:
            self.dungeon_map[entity.position[0]][entity.position[1]] = entity.map_identifier

    def beholder_spawn(self):
        """
        function for spawning boss entity called beholder and adding it to the list of entities
        """
        for entity in self.entities:
            if entity.map_identifier != "\033[0;34;1mB\033[0;0m":
                cond = 0
            else:
                1
        # when parametr is not 1 nothing happen
        try:
            while cond != 1:
                # first choosing of random position for beholder placement
                print("problem 1")
                position = (random.randint(1, self.size[0] - 1), random.randint(1, self.size[1] - 1))
                print("problem 2")
                # then control if that space is blank (it wil be better to choose blank
                # space from empty list, i know)
                if self.dungeon_map[position[0]][position[1]] == ".":
                    # parametr update
                    cond = 1
                    # beholder placing on the map and into the list of active entities
                    self.dungeon_map[position[0]][position[1]] = "\033[0;34;1mB\033[0;0m"
                    self.entities.append(Beholder(identifier="\033[0;34;1mB\033[0;0m",
                                                      position=position, base_attack=-3,
                                                      base_ac=2, damage=3))
        except Exception as ex:
            print(ex)

    def update_map(self, entities: list):
        """
        function for updating changes on map every round
        """
        # transfer map from dungeon map to current map that is shown and change
        # of position of hero identifier
        self.current_map = deepcopy(self.dungeon_map)
        self.current_map[self.hero.position[0]][self.hero.position[1]] = self.hero.map_identifier

    def fight(self, monster):
        """
        function for calculating fight between hero and entities
        """
        # rolls for damage
        hero_roll = self.hero.attack()
        monster_roll = monster.attack()
        # comparation if attack go through
        if hero_roll["attack_roll"] > monster.base_ac:
            monster.hp -= hero_roll["inflicted_damage"]
            # chcek if monster survive
            if monster.hp > 0:
                self.message = f"Hero inflicted {hero_roll['inflicted_damage']}"
            # if not upgrading hero status and removing monster form list and map
            else:
                self.message = f"Hero inflicted {hero_roll['inflicted_damage']}" \
                               f" damage and slain {monster}"
                self.hero.gold += monster.gold
                self.hero.xp += 1
                self.dungeon_map[monster.position[0]][monster.position[1]] = "."
                self.entities.remove(monster)
                # adding trophy by monster
                if monster.trophy == "small_trophy":
                    self.hero.hero_trophy += 1
                elif monster.trophy == "big_trophy":
                    self.hero.rank = "Beholder slayer"
        # block of code that occurs damage dealt to hero
        if monster_roll["attack_roll"] > self.hero.base_ac:
            self.message += f"\nMonster inflicted {monster_roll['inflicted_damage']} damage"
            # removing hero hp
            self.hero.hp -= monster_roll['inflicted_damage']
            # condition for posibility that hero is dead
            if self.hero.hp < 1:
                self.message += f"{self.hero.name} have been slained by {monster}"
        # lasting hp of monster print
        self.message += f"\nMonster HP: {monster.hp}"
        # price for attack for hero
        self.hero.stamina -= 2
        # trophy system that run beholder spawner if hero kill 8 goblins
        if self.hero.hero_trophy == 5:
            self.beholder_spawn()

    def interact(self, fountain):
        """
        function for interacting with fountain consumable
        """
        # if hero have enough money than he can interact with fountain
        if self.hero.gold >= 2:
            self.hero.hp += fountain.new_hp
            self.hero.stamina += fountain.new_stamina
            self.hero.gold -= 2

    def save_dungeon(self):
        """
        function for game saving
        """
        # creating filename for save
        date_time = datetime.strftime(datetime.now(), "%d-%m-%Y_%H-%M-%S")
        s_path = Path(".") / "saved_games" / "{}_{}".format(self.hero.name, date_time)
        Path.mkdir(s_path)

        s_map = "%s_%s_map.dng" % (self.hero.name, date_time)

        # save using pickle
        # its necesary to save dungeon map and list of entities
        with open(s_path / s_map, "wb") as f:
            pickle.dump(self.dungeon_map, f)

        s_entities = "%s_%s_entities.dng" % (self.hero.name, date_time)
        with open(s_path / s_entities, "wb") as f:
            pickle.dump(self.entities, f)

    def load_dungeon(self):
        """
        function for game loading
        """
        # displaying possible games for load
        l_path = Path(".").resolve() / "saved_games"
        print("Saved games available: ")
        number = 0

        # if there are games saved
        for saved_game in l_path.iterdir():
            print(saved_game)
            number = number + 1

        # if there are not saved any gmaes
        if number == 0:
            print("There are no saved games available")
            time.sleep(2)
            exit(0)

        try:
            l_file = input("Which game do you wanna play? insert in format heroname: ")
            l_path = l_path / l_file

            # load of game and declaring variables
            with open(l_path / (l_file + "_map.dng"), "rb") as f:
                self.dungeon_map = pickle.load(f)
            with open(l_path / (l_file + "_entities.dng"), "rb") as f:
                self.entities = pickle.load(f)
        # condition if someone try wrong input
        except Exception as ex:
            print("Wrong input")
            print(ex)
            exit(0)

        # condition that arrange situation if hero and monster have the same position
        for entity in self.entities:
            if entity.map_identifier == self.hero.map_identifier:
                self.hero.position = entity.position

    def beholder_move(self):
        """
        function for move of beholder. Movement is random with one
        exception and that is if hero is 5 units or less of
        manhatan distance far from beholder, beholder stops movement
        and start to shoot fireballs.
        """
        # parametr
        count = 0
        # exception - there is problem that if i start game beholder is
        # not spawned yet and game crash becose of thist
        # function, but thta funtion is necesary later. It will be better to do it diferent
        # than like this but this is faster... and a dont think that there
        # could by any other problem
        try:
            # checkyng distance betwen hero and beholder, manhattan distance is
            # calculated in beholder fireball function
            if self.manhattan_distance > 5:
                # loop that iterate through entities and move only with beholder
                for entity in self.entities:
                    if entity.map_identifier == "\033[0;34;1mB\033[0;0m":
                        # this condition is necesary if we want beholder to move every time.
                        # it is becose direction is choosed random and if there is wall
                        # nothing happen.
                        # So till beholder move without problems condition isnt update to 1
                        while count != 1:
                            pose = entity.position
                            # random direction
                            the_way_of_beholder = random.randint(0, 3)
                            # condition that control if there is not wall or another entity
                            if self.dungeon_map[pose[0]][pose[1] + 1] != "▓" and\
                                    self.dungeon_map[pose[0]][pose[1] + 1] !=\
                                    "\033[38;5;1mg\033[0;0m" and the_way_of_beholder == 0:
                                # repainting place where beholder was on map
                                self.dungeon_map[pose[0]][pose[1]] = "."
                                # position update
                                pose[1] += 1
                                # identifier inserting on the new place
                                self.dungeon_map[pose[0]][pose[1]] = entity.map_identifier
                                # condition update
                                count = 1
                                # other if statements are the same except for different direction

                            if self.dungeon_map[pose[0] + 1][pose[1]] != "▓" and\
                                    self.dungeon_map[pose[0] + 1][pose[1]] != \
                                    "\033[38;5;1mg\033[0;0m" and the_way_of_beholder == 1:
                                self.dungeon_map[pose[0]][pose[1]] = "."
                                pose[0] += 1
                                self.dungeon_map[pose[0]][pose[1]] = entity.map_identifier
                                count = 1

                            if self.dungeon_map[pose[0]][pose[1] - 1] != "▓" and \
                                    self.dungeon_map[pose[0]][pose[1] - 1] != \
                                    "\033[38;5;1mg\033[0;0m" and the_way_of_beholder == 2:
                                self.dungeon_map[pose[0]][pose[1]] = "."
                                pose[1] -= 1
                                self.dungeon_map[pose[0]][pose[1]] = entity.map_identifier
                                count = 1

                            if self.dungeon_map[pose[0] - 1][pose[1]] != "▓" and \
                                    self.dungeon_map[pose[0] - 1][pose[1]] != \
                                    "\033[38;5;1mg\033[0;0m" and the_way_of_beholder == 3:
                                self.dungeon_map[pose[0]][pose[1]] = "."
                                pose[0] -= 1
                                self.dungeon_map[pose[0]][pose[1]] = entity.map_identifier
                                count = 1
        except:
            pass

    def beholder_fireball(self):
        """
        function defining how is fireball shot by beholder.
        Beholder shoot if hero is 5 units or less of manhattan
        distance farr. Fireball have ac penetration becose
        its magic, sou it ignores ac.
        """
        # there is the same problem that is described in the function above on the start of function
        try:
            # iterate through entities position and saving beholder position to fire_pose variable
            for entity in self.entities:
                if entity.map_identifier == "\033[0;34;1mB\033[0;0m":
                    fire_pose = entity.position

            # manhattan distance calculation
            self.manhattan_distance = abs(fire_pose[0] - self.hero.position[0])\
                                      + abs(fire_pose[1] - self.hero.position[1])

            # control if manhattan distance of hero and beholder is less or equal to 5
            if self.manhattan_distance <= 5:
                # if is, this code make list of sum of manhattan distance every point in dungeon related to hero and to beholder.
                hold = []
                for i in range(0, self.size[0]):
                    level = []
                    for j in range(0, self.size[1]):
                        level.append((abs(i - self.hero.position[0]) +
                                      abs(j - self.hero.position[1])) +
                                     (abs(i - fire_pose[0]) +
                                      abs(j - fire_pose[1])))
                    hold.append(level)

                # this find minimum value from list of manhatten distances
                minimums = []
                for i in range(0, 9):
                    minimums.append(min(hold[i]))
                min_value = min(minimums)

                # this insert into list of manhattan distances to the position
                # of hero and beholder their letters
                hold[self.hero.position[0]][self.hero.position[1]] = "@"
                hold[fire_pose[0]][fire_pose[1]] = "B"

                control_list = []
                # his insert coordinates of all places where is menhetten
                # distance minimal and insert into control
                # ist all elements from dungeon map on saved coordinates
                for i, row in enumerate(hold):
                    for j, element in enumerate(row):
                        if isinstance(element, int) and element == min_value:
                            control_list.append(self.dungeon_map[i][j])

                # now it only chcek if in the way betwen beholder and hero is some wall
                cond = 0
                for item in enumerate(control_list):
                    if item[1] == "▓":
                        cond = 1
                # if there is not wall beholder fire fireball
                if cond != 1:
                    self.hero.hp -= random.randint(1, 6)
                    self.message += f"\nYou got hit by fireball -HP"
                else:
                    pass
        except:
            pass
