# datové typy
    # list,tuple - uspořádaná neměnná ntice, množina (set),slovník (disctionary)

my_list = [1, "value", [1, 1]]     #do listu mužu uložit i další list
print(my_list[2])

my_list[0] = 10                 # mužu přepisovat členy listu
print(my_list)
print(my_list[2][1])            # přístup do vnořeného listu
print(my_list[0:2])             # výběr více hodnot
my_list[0:2] = [10, "updated value", [1,2,3]]    #přepsat více promených
print(len(my_list))             # velikost listu
print(my_list[-2:])             # lze brát prvky listu od konce
my_list.append(100)             # na posledni misto prida do seznamu hodnot
print(my_list)
my_list.insert(1, "item")       # vložení na konkrétní místo
print(my_list)
my_list.pop(1)                  # takto mužem vymazat konkrétní hodnoty z listu, argument je index
print(my_list)
my_list.remove(10)              # vyhodí ze seznamu každý prvek nabývající hodnotu v argumentu
print(my_list)
# my_list.sort(reverse=True)      # třízení od nejvetšíko k nejmenšímu a opačně, mam li tam strinka číslo tak to crashne

# sčítání seznamů
my_list = [3, 3, 2]
print(my_list + [4, 5])          # tomuhle se říká přetížení operátoru, chová se jinak pro různé datové typy
print(my_list.extend([4, 5]))    # další způsob jak ho rozšířit

# funkce reverse obrátí pořadí prvků listu
my_list.reverse()
print(my_list)

print(my_list.count(3))          # spočítá počet zvolených hodnot
print(my_list.index(3))          # řekne mi kde je daná hodnota
my_list.clear()                  # vymaže list
print(my_list)


my_tuple = ("fake", "fire", "alarm")
val1, val2, val3 = my_tuple       # unpacking, elementy eznamu se mi uloží do proměnych
print(my_tuple + ("huh",))        # zase přidání elementu, na konci musí být čárka, nebo to musí být zavřeno v tuple()
print(my_tuple.count("fake"))
print(my_tuple.index("alarm"))    # ukaže kde je vybrany prvek

# hereze
print(my_tuple * 3)               # násobí jak tuple tak list
print([1] * 3)
# nahrazovat prvky u tuplu nelze

my_set = {1, 2, 3, 4, 4}            # v množině muže být stejná hodnota mac´x jednou, takže se nevytiskne kdyz je tam dvakrát
print(my_set)
print(set({1, 2, 3, 4, 4, 4}))       # tohle je vhodné když chci zjistit jaké unikátní hodnoty se tam nacházejí

# množiny jsou dobré pro zjišťování jestli tam nějaký prvek je
print(3 in my_set)
print(7854 in my_set)

my_set.add(5)
print(my_set)       # takto přidám hodnotu
my_set.remove(1)    # odstraní hodnotu na míste argumentu
print(my_set)

print(my_set.union({2, 6}))  # zjistím jak vypadá sjednocení s jinou množinou

# rošíření množiny o sjendocení
my_set.update({2,6})

# stejne ltze řešit i průnik množin
print(my_set.intersection({2, 5}))
# vyhodí všechny prvky z puvodní množiny co nejsou prvkama sjednocení
my_set.intersection_update({2, 5})
print(my_set)

# do množiny nemužu indexem přistupovat ke konkrétním hodnotám, musel bych ji převést na seznam
print(list(my_set)[0])

# akira
my_dict = {"name": "Akira", "age": 8, "occupation": "test subject", "ID":28}
print(my_dict)
print(my_dict["name"])
# zjisteni vsech klicovych slov ve slovniku
print(my_dict.keys())
print(my_dict.values())
# změna hodnot ve slovníku
my_dict["age"] = 9
print(my_dict)
my_dict.update({"age": 10, "occupation": "Tokyo destroyer"})
print(my_dict)
my_dict["Nationality"] = "Japanese"     # přidání parametru do slovníku
print(my_dict)
my_dict.pop("Nationality")              # vymazání ze slovníku
del my_dict["age"]
print(my_dict)


# # uživatelský vstup - uloži si co napisu
# obtained_input = input("Type somethink and press enter")
# print(f"You typed {obtained_input}")
# print("Give me more")
# more_data = input()
# print(f"You gave me {more_data}")


# smyčky
iteration_number = 0
while_early_stop = False
while iteration_number < 10:
    iteration_number += 1
    if iteration_number == 4:
        while_early_stop = True
        continue
    print(f"This is iteration number: {iteration_number}")
    # vytisknu si to do čtyřky a když přijde čtyřka tak ji přeskočí a jde dál
if while_early_stop == False:
    print(f"Itteration number is {iteration_number}")
    # tohle se často použivá jako kontrola jestli jsem proiteroval všechny iterace, jestli se někde smyčka nepřerušila

# smyčka for
for item in [1, 2, 3, 4, 5, 6]:
    print(item)

# iterování přes slovník
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

for key, value in my_dict.items():  # tyhle dve jsou ekvivalentní
    if value == "Tokyo destroyer":
        continue
    print(f"{key}: {value}")    # nebo zase podmínky

for i in range(2, 5):  # zastaví se to o jednu dřív než napisu
    print(i)

for i in range(5, 15, 3):  # různý krok
    print(i)
else:
    print(f"Finished successfully")



# tímhle ve hře vygeneruju všechny možné kombinace hráčů
for player_a in ["Carles", "Liren", "Carue"]:
    for player_b in ["Aronian", "Giri", "Grischuk"]:
        print(f"{player_a}-{player_b}")

# # spešl funkce
# abs()
# bin()
# chr()
# dir()   # vrátí seznam všech fcí které mužu použít v kontexktu k danému objektu
# eval("print('eval')") # spíš nepoužívat je to bezpečnostní hrozba
# help()  # vrátí nápovědu
# len()
# max()   # vrátí maximální hodnotu
# min()   #...
# sum()   # součet
# ord()   # převede znak na hodnotu
# round() # zaokrouhlení
# type()  # vrátí typ objektu

# definování funkcí

def hello_world():
    print("Hello wrold!")
hello_world()

for i in range(10):
    hello_world()

# ve funkci si mužu definovat promenné které jsou k dispozici ale jen v té funkci
# mužu udělat globální ale nemělo by se to dělat

def introduce_yourself(name, planet):
    print(f"I an {name} from planet {planet}")
introduce_yourself("Jack", "Mars")

def discriminant(a, b, c):
    return b ** 2-4 * a * c, "somethin else"
x, y = discriminant(1, 4, 1)
print(x, y)             # unpacking z funkce


