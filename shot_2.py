ingredient = "nic"

if ingredient == "Potato":  # korektně by to bylo bez toho == true, python to testuje okamžite aniž bych mu to řekl,
                            # pokud vyhodnocuju false true tohle už je přepsané
    print("add potatoes")
elif ingredient == "Tomato":
    print("add tomatoes")
else:
    print("add onion")

# zapisování na jeden řádek
key_ingredient = "Potato" if ingredient == "potato" else "something else"
print(key_ingredient)

# mužu mít vnořeno max 20 bloků, obecně, mamli vice než 5 je to špatně