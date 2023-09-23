"""
Script for calculation of sum of numbers of fibonachi sequence lower than 5 000 000
"""

# definition of initial lists and variables
List_of_fib_nums = [0, 1]
LAST_FIB_NUM = 0
TIME = 2
SUMMARIZATION = 1

# start of cycle which control if fibonacchi number is not greater than 5 000 000
while LAST_FIB_NUM < 5000000:
    # equation defining fibonacchi sequence
    List_of_fib_nums.append(List_of_fib_nums[TIME - 1] + List_of_fib_nums[TIME - 2])
    # time update which move cycle towards
    TIME += 1
    # defining of variable that is used for considering
    # cycle condition as last item in list of fibonacchi sequence
    LAST_FIB_NUM = List_of_fib_nums[len(List_of_fib_nums) - 1]
    # sum of all fibonacchi numbers till the condition allow continue
    SUMMARIZATION += LAST_FIB_NUM

# visualization of list of fibonacchi numbers
print(List_of_fib_nums)
# visualization of sum of fibonacchi numbers and final
# substract of last number that is greater than allowed condition
print(SUMMARIZATION - LAST_FIB_NUM)
