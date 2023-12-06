import random

# function for creating template of dungeon by set width and height
def maze_start(width, heigth):
    maze = []
    # cycles for rows and columns
    for i in range(0, heigth):
        level = []
        for j in range(0, width):
            level.append("▓")
        maze.append(level)
    # return matrix of basic symbols
    return maze

# function which randomly choose direction 1-4 and make randomly long tunnel there
def maze_tunels(maze, width, heigth, tunels_number):
    # starting position
    position_x = 1
    position_y = 1
    # counter of tunnels
    m = 0
    while m != tunels_number:
        # 1-right,2-above, 3-left, 4-down
        tunel_direction = random.randint(1, 4)
        # if is choosen 1 and momental position is not on the right edge than this happened
        if tunel_direction == 1 and position_x != (width-1):
            # this condition is there because somethimes input for tunnel length was
            # choosen from 1 to 0 and that is nonsence
            if (width-2-position_x) < 1:
                pass
            else:
                m += 1
                tunel_length = random.randint(1, width-2-position_x)
                # cycle which append point to positions of choosen tunnel
                for n in range(position_x, position_x + tunel_length):
                    maze[position_y][n] = "."
                position_x += tunel_length

        # others cycles of this function are the same principle, only direction is changing
        elif tunel_direction == 2 and position_y != 1:
            if (position_y - 1) < 1:
                pass
            else:
                m += 1
                tunel_length = random.randint(1, position_y - 1)
                for n in range(position_y, position_y - tunel_length, -1):
                    maze[n][position_x] = "."
                position_y -= tunel_length

        elif tunel_direction == 3 and position_x != 1:
            if (position_x - 1) < 1:
                pass
            else:
                m += 1
                tunel_length = random.randint(1, position_x - 1)
                for n in range(position_x, position_x - tunel_length, -1):
                    maze[position_y][n] = "."
                position_x -= tunel_length

        elif tunel_direction == 4 and position_y != (heigth - 1):
            if (heigth - position_y - 2) < 1:
                pass
            else:
                m += 1
                tunel_length = random.randint(1, heigth - position_y - 2)
                for n in range(position_y, position_y + tunel_length):
                    maze[n][position_x] = "."
                position_y += tunel_length

        else:
            pass
    # return matrix of basic symbols with point on the place of tunnels
    return maze

# this function print matrix of maze to console so it looks like maze.
def maze_visual(maze):
    for k in range(0, len(maze)):
        for l in range(0, len(maze[0])):
            # there is important end because of that it looks like maze and not like matrix
            print(f"{maze[k][l]}", end="")
        print("")

# # there is several inputs, first is width, second is height and third is number of columns
# maze = maze_start(30, 10)
# maze = maze_tunels(maze, 30, 10, 40)
# maze_visual(maze)

















# print("▓▓▓▓▓▓▓▓▓▓\n\
# ▓........▓\n\
# ▓........▓\n\
# ▓▓▓▓▓▓▓▓▓▓")
