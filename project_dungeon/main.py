from dungeon import Dungeon
import subprocess
import time

if __name__ == "__main__":

    load_game = input("Do you want continue in a previous game? (Y)ES or (N)O ")
    if load_game == "Y":
        # load previous game
        dungeon = Dungeon((10, 30), tunnel_number=40, hero_name="")
        dungeon.load_dungeon()
        hero_name = dungeon.hero.name  # hero_name taken from the past game
        dungeon.update_map(dungeon.entities)  # update positioning from the past game

    elif load_game == "N":
        hero_name = input("What is your name hero? ")
        dungeon = Dungeon(size=(10, 30), tunnel_number=40, hero_name=hero_name)

    else:
        print("Wrong input")
        time.sleep(5)
        exit(0)


    while True:
        subprocess.Popen("cls", shell=True).communicate()
        print(dungeon)
        print(dungeon.status)
        print(dungeon.message)
        dungeon.message = ""

        action = input(f"Select an action {hero_name}: (L)EFT, (R)IGHT, (D)OWN, (U)P, (A)TTACK, (Q)UIT, (S)AVE, (I)nteract")
        if action == "Q":
            print("You coward!")
            exit(0)
        elif action == "S":
            dungeon.save_dungeon()
            print("The game was saved")
            exit(0)
        else:
            dungeon.hero_action(action)
        if dungeon.hero.hp < 1:
            print(dungeon.message)
            exit(0)


# při psuštění z cmd se to bude chovat hezky, nebude se to pořád dokola
# vypisvat ale bude se přepisovat ten samý výtisk
