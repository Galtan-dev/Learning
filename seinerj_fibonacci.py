"""
Script for calculation of sum of numbers of fibonachi sequence lower than 5 000 000
"""

# definition of initial lists and variables
List_of_fib_nums = [0, 1]
LAST_FIB_NUM = 0
TIME = 2
SUMMARIZATION = 0

# start of cycle which control if fibonacci number is not greater than 5 000 000
while LAST_FIB_NUM < 5000000:
    # equation defining fibonacci sequence
    List_of_fib_nums.append(List_of_fib_nums[TIME - 1] + List_of_fib_nums[TIME - 2])
    # time update which move cycle towards
    TIME += 1
    # save last fib number from list to variable
    LAST_FIB_NUM = List_of_fib_nums[len(List_of_fib_nums) - 1]
    # considering if last fibonacci number is even
    if (LAST_FIB_NUM % 2) == 0:
        # sum of all fibonacchi numbers till the condition allow continue
        SUMMARIZATION += LAST_FIB_NUM
    else:
        pass

# visualization of sum of even fibonacchi numbers
print(SUMMARIZATION)


# problém je v tom že když na konci kontroluju jestli je to poslední šíslo sudé tak to vždycky nemusí fungovat, lepší
# tam dát podmínku aby právě nebylo větší než to co jsem použil, protože to poslední číslo nemusí nutně být sudé a
# přesto bude větší než podmínka
