"""
Původně jsem používal taktiku toho že všechny palindromická čísla jsou dělitelná 11,
to ale není pravda jak bylo v ůkolu upraveno.
Dělitelná jsou jen se sudým počtem číslic. Zde je teda oprava kde jsem raději zvolil jiný přístup,
a to vynechání duplictitních dvojic které by se zkoušeli

"""

def is_palindrome(n):
    # testování jestli číslo je palindromické
    return str(n) == str(n)[::-1]

def find_largest_palindrome():
    largest_palindrome = 0

    # smička hledající největší palindromícké číslo
    for i in range(1000, 10000):
        # Začínáme od i, abychom eliminovali duplikáty (např. 12 * 34 a 34 * 12)
        for j in range(i, 10000):
            # součin teoreticky produkující hledané číslo
            product = i * j
            # kontrola zdali je to opravdu to největší hledané číslo
            if product > largest_palindrome and is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome

def main():
    # vypsání výsledku
    result = find_largest_palindrome()
    print("Nevětší palindromické číslo je:", result)

if __name__ == "__main__":
    main()