def looper(n):
    # there are three loops that try numbers, every next loop iterate only to last number host from
    # previous loop because this number cannot be bigger if we have limit 1000
    for c in range(1, n+1):
        for b in range(1, c):
            for a in range(1, b):
                # first condition check if sum of a b and c is 1000
                if a + b + c == n:
                    # second loop check if choosen numbers are pythagorean numbers
                    if (pow(a, 2) + pow(b, 2)) == pow(c, 2):
                        # visualization of results
                        print(f"Hledaná číasla jsou {a}, {b}, {c}")
                        print(f"Součin hledaných čísel je: {a*b*c}")
                        return

# inicialization of function
looper(1000)

