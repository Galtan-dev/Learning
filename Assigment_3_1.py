import tqdm
import numpy as np
import matplotlib_examples.pyplot as plt

data = []
print("Generating data...")
from tqdm import tqdm
for i in tqdm(range(100)):
    data.append(0.1*np.random.randint(-30, 30))

action = input()

if action == "":
    plt.plot(data)
    plt.show()