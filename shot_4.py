# pomocí ctrl + c ukončím skript
counter = 0
while counter < 9:
    print(f"The value of conter is: {counter}")     #napíšuli f pred zavorky je to formatovany řetězec
    counter += 1    # korektněji napsane counter = counter + 1
    if counter == 4:
        break   # tim uzu ukoncit smicku pokud neco treba hledam
print("Finished")