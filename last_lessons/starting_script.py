import seinerj_test as st
import matplotlib.pyplot as plt

# zde zadat jméno ve formátu "jmeno.csv" nebo "jmeno.json"
name = "data.json"
# zde zadat číslo sloupce pro vykreslení
column = 4
# zde zadat rozměr náhodných dat
shape = (100, 5)

if column <= 5:
    # vytvoření hodnot a vypsání prvních 6 řádků
    values = st.Dataset.generate_data(None, shape)
    print(values.head(6))

    # uložení dat do souboru cls, nebo json
    st.Dataset.save_data(None, values, name)


    # zobrazí jednotlivé histogrami do okna
    fig, axs = plt.subplots(2, 3)
    for i in values:
        graph = st.Dataset.plot_column(None, values, i)
    plt.show()
        # nestihl jsem dodělat ty grafy

else:
    print("Přesažena hodnota indexu sloupce")


