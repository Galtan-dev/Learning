# # otevírám li soubor pro zápis a ten soubor neexistuje tak se vytvoří
# f = open("file.txt", "r")       # x vytvoří, r čte, w vytvoří a píše
# content = f.read()
# print(content)
#
# # funkce read muže i vypsat jen požadovaný počet znaků
# content2 = f.read(10)
# print(content2)


# f = open("file.txt", "w")
# f.write("content1\n")
# f.write("content2\n")
# f.close()
# # pokud otevřu soubor jako write tak se mi smaže to co tam je, chcili jen pridat musím to otevřít jako append


# # kontext manager - potom co použiju ten soubor tak ho to zavře
# # postará se i o vyjímky, dojdeli k ní tak se soubor automaticky zavře
# # četl bych poškouzený soubor tak se to ošetří
# with open("file.txt", "r") as f:
#     data = f.read()
# # s těmi daty mužu pracovat i  potom co je soubor zavřen
# print(data)
# # nejlépe používat jen ten zápis s with


# # tahle se mi uloží obas jako seznam
# with open("file.txt", "r") as f:
#     data = f.readlines()
# print(data)


# # zapíšu tam něco
# with open("file.txt", "a") as f:
#     f.writelines({"a\n", "b\n"})


# # funkce seek přesouvá kurzor na požadované místo
# with open("file.txt", "r") as f:
#     line = f.readline()
#     print(line)
#     f.seek(2)
#     line = f.readline()
#     print(line)
#     print(f.tell()) # tohle mi řekne kde se kurzor nachazi


# with open("file.txt", "r") as f:
#      line = f.readline()
#      print(f.tell())
#      f.readline()
#      print(f.tell())  # ta funkce mi dá souřadnici ne přímo číslo


# # funkce trunc
# with open("trunc_example.txt", "w") as f:
#     f.write("abcd12345")
# with open("trunc_example.txt", "w") as f:
#     f.truncate(5)  # vezme prvních 5 znaků a zbytek zahodí


# # chcili pracovat s adresáři jinde je dobré používat modul standartní knihovny, bez ohledu na operační systém
# from pathlib import Path
# path = Path(".")
# print(path.resolve())
#
# from pathlib import Path
# path = Path("C:/Users")
# print(path.resolve())
#
# from pathlib import Path
# path = Path("C:/", "Users")   # takhle si zjistim rlativni cestu, na jakymkoliv systému
# print(path.resolve())



# # zjištění obsahu adresáře
# from pathlib import Path
# path = Path(".")
# for item in path.iterdir():
#     print(item)


# # práce s maskou
# from pathlib import Path
# path = Path(".")
# for item in path.glob("o"):
#     print(item)


# from pathlib import Path
# path = Path(".")
# for item in path.glob("**/*"):  # pro všechny itemy v adresáři, proleze to všechno
#     print(item)

# # tvorba nového adresáře
# from pathlib import Path
# path = Path(".", "new_folder", "nested_folder")
# path.mkdir(parents=True, exist_ok=True)


# # přejmenování
# from pathlib import Path
# path = Path("./new_folder")
# path.mkdir(parents=True, exist_ok=True)
# path.rename("new_name")


# from pathlib import Path
# path = Path("./file.txt")
# path.unlink()  # funkce unlink smaže jne soubor ne adresář


# from pathlib import Path
# import shutil
# path = Path("./new_name")
# shutil.rmtree(path)   # smaže všechno včetně podadresáře


# # modul shutil se použáva i pro kopírování souborů
# from pathlib import Path
# import shutil
#
# src = Path(".", "trunc_example.txt")
# dst = Path(".", "venv", "trunc_example.txt")
# shutil.copy2(src,dst)


# # pro přesun souboru
# src.rename(dst) # plus to samé jao předtím


# serializace - chceme uložit třeba seznam ale jako sequenci bitu
# json = jawa script object notation
import json
from pathlib import Path
#
# with("data.dat", "w") as f:
#     json.dump([1, 2, 3, 4, 5], f)
# # deserializace
# with("data.dat", "r") as f:
#     data = json.load(f)
# print(data)

# nebo
# import pickle
#
# with("data.dat", "wb") as f:
#     pickle.dump([1, 2, 3], f)
# # deserializace
# with("data.dat", "r") as f:
#     data = pickle.load(f)
# print(data)
# nefunguje nevim proč