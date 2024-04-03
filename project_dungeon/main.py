"""
Script that is running dungeon script and making space for keybod inputs. Game dungeon.
"""

from dungeon import Dungeon
import subprocess
import time

if __name__ == "__main__":
    # input question
    load_game = input("Do you want continue in a previous game? (Y)ES or (N)O ")
    if load_game == "Y":
        # load previous game
        dungeon = Dungeon((10, 30), tunnel_number=40, hero_name="")
        dungeon.load_dungeon()
        hero_name = dungeon.hero.name  # hero_name taken from the past game
        dungeon.update_map(dungeon.entities)  # update positioning from the past game

    # if player dont want to load game
    elif load_game == "N":
        # input for new name of hero
        hero_name = input("What is your name hero? ")
        # dungeon script run
        dungeon = Dungeon(size=(10, 30), tunnel_number=40, hero_name=hero_name)

    else:
        # exception if someone choose wrong input
        print("Wrong input")
        time.sleep(5)
        exit(0)


    while True:
        # printing messages and dungeon
        subprocess.Popen("cls", shell=True).communicate()
        print(dungeon)
        print(hero_name + " " + dungeon.hero.rank)
        print(dungeon.status + "\n")
        print(dungeon.message + "\n")
        dungeon.message = ""

        # action input question
        action = input(f"Select an action {hero_name}: "
                       f"(L)EFT, (R)IGHT, (D)OWN, (U)P, (A)TTACK, "
                       f"(Q)UIT, (S)AVE, (I)nteract")
        # non-play action
        if action == "Q":
            print("You coward!")
            exit(0)
        elif action == "S":
            dungeon.save_dungeon()
            print("The game was saved")
            exit(0)
        else:
            dungeon.hero_action(action)

        # condition for terminating
        if dungeon.hero.hp < 1:
            print(dungeon.message)
            exit(0)
