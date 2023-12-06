import this

# vícenásobné přiřazení
#
# a = 5
# b = 10
# a, b = b, a

#######################

# tady tímhle si říkame že vystupem bude string
# def introduce(name: str, surename: str) -> str :
#     """
#     Function that returns your full name
#     """
#     return f"Hi my name is {name} {surename}"
#
# #######################
# # takhle nám to vlastně iteruje pozadu, otočí nám to pořadí prvků
# default_string = "alphabet"
# print(f"reversed string:{default_string[::-1]}")
#
# # iterčaně přes for cyklus by se to dělalo dost složitě, dělali jsme v palindomu


###################
#pro velký počet čísel je tohle strašně pomalé
default_numbers = [1, 2, 3, 4]
even_numbers = []
for value in default_numbers:
    if value % 2 == 0:
        even_numbers.append(value)
print(even_numbers)

# jsou 2 možnosti co použít linak
#list comprehension
even_numbers = [number for number in default_numbers if number % 2 == 0]  # v novém seznamu chci mít čísla která v původním seznamu jsou dělitelná 2
# nebo použiju filtr a lambda funkci
even_numbers = list(filter(lambda x: x % 2 == 0, default_numbers))

###########################################

# sparse i better than dense - asi nejduležitější
# to že něco dokážu napsat na jednu řádnku ještě neznamená že je to dobře, lepší ať to každý pochopí
# golf exchange - soutěž kde se snaží lidi vyřešit šíleně komplexní veci na malém prostoru
# a je takov´ten debilní znat pro a
lambda c: chr(((((ord(c)) a ob11111) + 12) = 26 +1) + (ord(c) a ob11000000))

###########################################

# Special cases aren't special enough to break the rules.
# dodržovat standartní postupy, lepší než mít rychlé ale špatně odladěné řešení
if not bug_condition:
    do_stuff()
# třeba tohle když vím že tam je chyba ale nevím jak vzniká tak ji objedu

#############################################
# Although practicality beats purity.
# někdy je i to špatné řešení lepší než strávit stovky hodin na odstranění nějaké chyb. Vícem=ně to popírá tu předchozí

####################################
# Errors should never pass silently.
try:
    somethink()
except Exception as ex:
    pass
# tohle je tragedie, vím že mi tam vzniká chyba, ale ignoruju ji

############################################
# Unless explicitly silenced.

number_is_ok = False
while not number_is_ok:
    number = input("gimmi number")
    try:
        print(int(number) + 1)
        number_is_ok = True
    except ValueError:
        print("please input the NMUBER")

###############################################
# In the face of ambiguity, refuse the temptation to guess.
# když si nejsme jistí jak vyřešit nějaký problém tak bychom se měli vyvyrovat zkoušet pokusy o řešení
# takové to když někde začnu přičítat jedničku a zkoušet jestli to bude fungovat, z ryzí frustrace
################################################
# There should be one-- and preferably only one --obvious way to do it.
# spoustu problému lze vyřešit vícero způsoby
##############################################
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# když se píše kod tak často zbastlim strašnou prasárnu a někdy to chci předělat ale už to nikdy neudělam protože to funguje
    # špatně je lepší než když neudělam nic
############################################x
# je lepší pomalý program co vrátí správný výsledke než rychlý co vrátí špatny
##########################################
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# mameli nějakou implementaci kterou neumíme snadno vysvětlit je to špatně
#########################################x
# Namespaces are one honking great idea -- let's do more of those!
# než začnu psát program je dobré si rozmyslet nejenom strukturu atd, ale taky jak pojmenuju proměné


# modul radon nebo multimetrik - vypočíta metriky složitosti


