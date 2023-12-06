"""
Script that calculate biggest divider of set number by function biggest_divider
"""


def biggest_divider(momental_num):
    """
    function that find biggest factor of entered number
    """
    # starting variables
    largest_num = -1
    i = 2
    # loop that iterates through all possible dividers of set number
    while i * i <= momental_num:
        # loop that try if residue after division is zero
        while momental_num % i == 0:
            largest_num = i
            # update of set number
            momental_num = momental_num // i
        # time update
        i = i + 1
    # final condition
    if momental_num > 1:
        largest_num = momental_num
    return largest_num


# number which we are analysing
MOMENTAL_NUM = 70616204741131
# message with answer
print(f"číslo je: {biggest_divider(MOMENTAL_NUM)}")
