import numpy as np
import pandas as pd

class Dataclass:
    data = None
    shape = [100, 5]

    # funkce pro generování dat
    def generate_data():
        data = pd.DataFrame(np.random.randn(100, 5))

        return (data)

    # funkce pro ukládání dat
    def save_data():
        print("ok")

    # funkce pro zobrazování dat
    def plot_column():
        print("ok")