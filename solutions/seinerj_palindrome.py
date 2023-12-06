# function that control if given parameter k is palindomical number
def Pal_test(k):
    num = str(k)
    result = True
    i = 0
    j = len(num) - 1  # -1 because desired number isn´t even
    # cycle which compare numbers from beginning and end of number
    while i < j and result:
        result = num[i] == num[j]
        i += 1  # beginning update
        j -= 1  # end update
    return result

res = 0

# all palindomical numbers above 1000 are divisible by 11, there is cycle which find only multiples of 11.
for first_num in range(9999, 1000, -11):
    # if division by 11 is zero cycle while end and update parameter first_num
    while first_num % 11 != 0:
        first_num -= 1
    # last cycle which search for second number which we multiply by parameter first_num and get desired number
    for sec_num in range(9999, 1000, -1):
        cond = first_num * sec_num
        # last condition which control if it really is our number and if yes it rewrite variable for print
        if cond > res and Pal_test(cond):
            res = cond
            break

print(res)

