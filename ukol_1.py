"""
Script for calculation multiples of three and five lower than 1024
"""

END_OF_INTERVAL = 1024
END_CONDITION = 0

# cycle that control if calculation is in range
while END_OF_INTERVAL != 0:
    # first condition that collect numbers dividable only by 3 and lower that biggest number
    if (END_OF_INTERVAL % 3) == 0 and (END_OF_INTERVAL % 5) != 0 and (END_OF_INTERVAL < 1024):
        # variable to which are collected numbers saved
        END_CONDITION += END_OF_INTERVAL
        # counter
        END_OF_INTERVAL -= 1
    # second condition that collect numbers dividable only by 5 and lower that biggest number
    elif (END_OF_INTERVAL % 5) == 0 and (END_OF_INTERVAL % 3) != 0 and (END_OF_INTERVAL < 1024):
        # variable to which are collected numbers saved
        END_CONDITION += END_OF_INTERVAL
        # counter
        END_OF_INTERVAL -= 1
    else:
        # counter
        END_OF_INTERVAL -= 1

print(END_CONDITION)
