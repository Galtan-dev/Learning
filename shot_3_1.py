# funkce ve velkém
def test_return(a, b):
    return 3 * a, 5 * b
result = test_return(1, 2)
print(result)
print(type(result))
result_1, result_2 = test_return(1, 2)      # pokud víme kolik výstupu bude, mužem je rozdelit
result_1, _ = test_return(1, 2)             # takhle by to ten jeden výsledek zapomělo, pouziju kdyz ho nechci
print(result_1)
print(result_2)


# jedno co se pouziva je ze vracim rovnou seznam
def test_return(a, b):
    return [3 * a, 5 * b]
result = test_return(1, 2)
print(result)
# nevýhodou je ze musím vedet na jaké pozici je jaká hodnota


# nebo pouziju slovník
def test_return(a, b):
    return {"a": 3 * a,"b": 5 * b}
result = test_return(1, 2)
print(result)


# dalsi moznosti v pythonu na predavani parametru
def my_multiply(*args):     # *args pouziju kdyz nevim kolik argumentu tam chci poslat, volitelny pocet argumentu
    total = 1
    for arg in args:
        total *= arg
    return total
print(my_multiply(1, 2, 3))
print(my_multiply(1, 2, 3, 4, 5))
# v programovacích jazycích je to neozvyklé


# mužu udelat i nejaké nutné a pak volitelné
def some_args(first_arg, *args):
    print(first_arg)
    for arg in args:
        print(f"args:{arg}")

some_args("first", "second", "third")
print(some_args)


# další věc jsou pojmenované argumenty
def print_name(first_name, last_name):
    print(f"{first_name} {last_name}")
print(print_name(last_name="Seiner", first_name="Jakub"))


# předpřiřazený argument
def print_favourite_color(color="red"):
    print(f"my favourite color is: {color}")
print_favourite_color()
print_favourite_color("blue")


# když použiju dvouhvězdičkovou notaci tak přidávám pojmenované paramtery, zase libovolný počet
def print_name(**names):
    print(type(names))
    print(names)
    print(f"{names['first_name']}")
print(print_name(first_name="Alan", last_name="Turing"))
# obecne se tomu rika *kwags

# tohle nefunguje nevim proč
# def print_name(first_name, last_name, **kwargs):
#     middle_name = ""
#     for item in kwargs.values():
#         middle_name += f"{item}"
#     print(f"{first_name} {middle_name} {last_name}")
# print_name("john","Veles", "Aron")


# rekurzivní programování
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)
        # tohle se vlastne dosazuje samo za sebe až se to dostane do jedničky
print(factorial_recursive(3))
# tomuhle se říká rekurzivní programování, problém je že to celkem rychle zaplní celou pamět, lze to většinou převést na iterativně


# anonymní funkce, beze jména, často se pouziva s pandasem
def identity(x):
    return x
# je to ekvivalnetní tomuhle:
lambda x: x
# lambda definuje amnonymní funkci, pak proměná a za dvoutečkou to co vrací

a = lambda x: x ** 2
print(a(4))

# nebo
x = (lambda x: x ** 2)(4)
print(x)
# i s více parametry
print((lambda x, y: x * y)(3, 4))
# občas se používá i neanonimně, fce vyššího řádu
ho_func = lambda x, func: x + func(x)
print(ho_func(3, lambda x: x * 2))


numbers = [1, 2, 3]
map_results = (map(lambda x: x * 2, numbers))
print(list(map_results))
# ta map funkce aplikauje tu funkci na každý prvek listu
# dobrý třeba když chci každé číslo v seznamu zaokrouhlit, nebo tak něco, funkce se prostě aplikuje na každé číslo seznamu
# funkce map je strašně rychlá


# funkce filter, vyfiltruje z listu ty chodnoty pro které má funkce hodnotu true
numbers = [1, 2, 3, 4, 5]
odd = filter(lambda x: x % 2 != 0, numbers)
even = filter(lambda x: x % 2 == 0, numbers)
print(type(odd))
print(list(odd))
print(list(even))
# vhodne pro odfiltrovani cisel ze seznamu


# funkce zip, uděla vsechny mozne dvojice
a = ["x", "y", "z"]
b = [1, 2, 3]
c = ["dog", "cat", "car"]
zipped = list(zip(a, b, c))
print(zipped)
# dobre je to k otmu že přes to mužu iterovat
for val1, val2, val3 in zipped:
    print(val1, val2, val3)
    # takhle jde jednoduše generovat slovníky


a = ["x", "y", "z"]
b = [1, 2, 3]
zipped = list(zip(a, b))
dictionary = dict(zipped)
print(dictionary)
cords, values = zip(*zipped)
print(cords)
# dají se tkhle dělat třeba souřadnice


name ="spock"
age = 55
print(f"My name {name}, i am {age:b}")  # napisu li tam b tak to udela binarni cislo
print(f"hot is: {500.5261651:.2f} kelvins")      # takhle pomoci 2f udelam jen 2 desetine cisla
# print(f"hot is: {500.5261651:.d} kelvins")

for x in range(1, 11):
    print(f"{x:2d} {x ** 2} {x ** 31}")

# práce s řeteřzci
to_join = {"name", "surename"}
print(" ".join(to_join))   # řiká abych všechny prvky propojil mezerou nebo tím co tam napíšu
# ltźe iterovat funkcí join i přes slovník

# rozdělování řetezců
to_split = "along came a man carrying a large python"
print(to_split.split(" "))
print(to_split.split("a"))
# dobry to je pro rozdeleni sloupecku s cislama oddelene carkama ci tak neco


# fce replace
cat_string = "cat is cute, cat does meouv"
wut_string = cat_string.replace("cat", "dog")
print(wut_string)
dog_string = cat_string.replace("cat", "dog", 1)  # nahradím pouze pro první výskyt toho slova cat
print(dog_string)

print("text".zfill(10))  # tahle funkce doplmi řetezec nulama aby celkova delka byla to zvolene cislo
print("+text".zfill(10)) # specifičnost pythonu, nuly se přidaji az za plus, dobry pro srovnani delky cisel v řetezci

some_string = "AlpHAb3t"
print(some_string.lower())
print(some_string.upper()) #sjednocení velikosti písmen

# funkce strip - odstrani konkretni znaky
some_text = "               no space               "
print(some_text.strip(" ")) # odstraní z leva i z prava ty znaky
# proparsování textu
another_text = "aaaaaaaaaaabbbbbbbaaaaa"
print(another_text.strip("a"))
print(another_text.lstrip("a")) # zleva
print(another_text.rstrip("a")) # zprava

some_text = "alphabet alphabet"
print(some_text.find("ab"))      # najde první výskyt znaku co hledam a vrátí jeho pozici
print(some_text.find("a", 7, 10))

# funkce count
test_string = "dskfnakggwefwefgwgwegwevwerg"
print(test_string.count("we"))      # vrati počet zvoleneho znaku, zase lze zvolit interval hledání

