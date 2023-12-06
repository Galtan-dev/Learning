n = 20
pascal_rows = []
for i in range(n):
    if i == 0:
        pascal_rows.append([1])
    else:
        previous_row = [0] + pascal_rows[-1] + [0]
        new_row = []
        for idx in range(len(previous_row)-1):  # nepojedu až na konec, jen k předposlednimu
            new_row.append(previous_row[idx] + previous_row[idx + 1])
        pascal_rows.append(new_row)
    print(pascal_rows[-1])

maximum_length = len(pascal_rows[-1])   # length of the longest row
for row in pascal_rows:
    row_str = " " * int((maximum_length - len(row))/2)
    for number in row:
        row_str = f"{row_str} {number}"
    print(row_str)
