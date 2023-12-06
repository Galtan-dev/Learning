"""
Script that calculate smallest number that is divisible by numbers from 1 to 30 without residue.
I know that we are baned from using non strandart modules and libraries to this
homeworks, but on this page: https://docs.python.org/3/library/index.html i read that math
library is part of python standard library, so can i use it? Its written on page from url in
the second paragraph.
"""

# importing python standart library for mathematics
import math

# starting varible
NUM = 1
# loop which is searching for smallest number divisible by numbers from 1 to 30
for i in range(1, 31):
    # lcm is function that return last common multiple. Last common multiple is the number which is
    # divisible by numbers before this one from some group
    NUM = math.lcm(NUM, i)
# end message with answer
print(NUM)
