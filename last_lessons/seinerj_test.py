import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Dataset():
    # funkce pro generování dat
    def generate_data(self, shape):
        # vytvoří dataframe s daty
        data = pd.DataFrame(np.random.randn(shape[0], shape[1]))
        return(data)

    # funkce pro ukládání dat
    def save_data(self, data, name):
        # převod na list
        data = data.values.tolist()
        data_for_save = json.dumps(data)
        # zapsání dat do souboru
        with open(name, "w") as file:
            print(data_for_save, file=file)

    # funkce pro zobrazování dat
    def plot_column(self, data, column):
        # vyplotování histrogramu
        plt.hist(data[column])

