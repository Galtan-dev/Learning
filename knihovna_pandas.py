# knihovna pro práci s velkými data, jako ma numpy array tak pandas ma dataframe, umí otevřít skoro vše
# obsahuje i nějaké vyzualizace, umí dělat i s excelem, je to vlastně takový uppgradovaný excel
# projekt jupiter - google colap, nejlepší přístup, ukládá si proměnné jako matlab, po 30 minutach se smaže
import pandas as pd

# knihovna zaměřená na vyzualizaci dat pomocí grafů, založeno na matplotlibu který je univerzálnější
# seaborn počítá s tím že do něj vlkádáme tabulky
import seaborn as sns

import openpyxl

# matplotlib no...
from matplotlib_examples import pyplot as plt

import lxml
import numpy as np




# DataFrame form dictionary
data = {"Name": ["Jakub", "Tomáš", "Milan", "Alois"],
        "Surname": ["Sluka", "Jerman", "Červený", "Koloun"],
        "Age": [20, 34, 18, 55]}
df1 = pd.DataFrame(data)
# print(df1)


#data - row structure
data = [["Jakub", "Novák", 20],
        ["Tommáš","jerman",34]]
column_names = ["Name","Surname","Age"]
df2 = pd.DataFrame(data=data,columns=column_names)
# print("")
# print(df2)


# first n rows
# print(df1.head(3))   # return first 3 rows, default value is 5


# last n rows
# print(df1.tail(3))   # return last 3 rows


# information on the column
# print(df1.info())


## basic statistical information
# print(df1.describe(percentiles=[0.1, 0.9]).T)   # automaticky přeskakuje nečíselné sloupce, nastavení percentilu, automaticky kvartily
# pokud zavoláme .T tak se nám prohodí sloupečky a řádky

# df1.loc[0, "Name"] = "Milan"       # takhle upravíme hodnotu v tabulce
# print(df1.mode())

# print(df1.Age.median())     # median se z nečiselnych hodnot počitat nedá
                            # pokud bych měl víceslovné nazvy sloupce tak to crashne
                            # musím použít df1["Last name]

# print(df1.columns)   # vrátí sloupečky


# print(df2[["Surname", "Name"]])
# nebo
# df2 = df2[["Surname", "Name"]]
# print(df2)
# přejmenování názvů
# df2.columns(proházení sloupců)


# accesing specific part of table
print(df1.loc[0])
print("")
print(df1.loc[:, "Age"])
print("")
print(df1.loc[1:3, "Age"])  # na rozdíl od esznamů tady to vrátí i tu poslední hodnotu
print("")
print(df1.loc[:, ["Name", "Surname"]])
print("")
print(df1.iloc[0, 0], df1.loc[0, "Name"])

# changing indeces of table
df1.index = [20, 21, 22, 23]
print(df1)      # musím ale teďka počítat že když odkazuju na nějaou hodnotu tak má nový index
print("")
df1.reset_index(inplace=True, drop=True)   # vykoná to na tabulce a auloží to pomocí toho impace
                                           # s argumentem drop se nebudou zachovávat indexy
print(df1)
print("")
df3 = pd.concat([df1, df1])

df3 = df3.drop_duplicates()
print("")
print(df3)

# merge two tables
data3 = {"name": ["Karel","Jan", "Pavel", "Tony"],
         "Age": [20, 30, 40, 20]}
data4 = {"Vocation": ["Učitel","pravnik", "podnikatel", "stavebník"]}
ids = ["ID001", "ID002", "ID003", "ID004"]
data3["id"] = ids
data4["id"] = ids
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)
print(df3)
print("")
print(df4)

print(df3.merge(df4, on="id", how="left"))


# saving data
df1.to_csv("data.csv", index=False)    # to excel, to html, to pickle, to jason, to dict
                                        # index = false nám udělá aby se něukládali i indexi

# loading data
df5 = pd.read_csv("data.csv")
print(df5)


