import math
import tqdm
import numpy as np
import matplotlib_examples.pyplot as plt
from scipy import misc

def f(x):
    return x/(math.sin(x)+2)

data_1 = []
data_2 = []

for i in range(-500, 500, 1):
    data_1.append(misc.derivative(f, i/100, dx=1e-2))
    data_2.append(f(i/100))
    if round((misc.derivative(f, i/100, dx=1e-2))*100)/100 == round(f(i/100)*100)/100:
        point = [i*10, misc.derivative(f, i/100, dx=1e-2)]
        print(point)
        print(i)
    else:
        pass

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_title("My beautiful plot")
ax.plot(data_1, color="tab:orange")
ax.plot(data_2, color="tab:blue")
ax.set_xlim(0, 1000)
ax.set_ylim(-2, 5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_yticks(np.arange(-2, 5.5, 0.5))
ax.set_xticks([100, 300, 500, 700, 900])
ax.set_xticklabels(['-4', '2', '0', "2", '4'])
ax.legend(["Function", "Derivative"], loc ="lower right")
ax.plot([0.29252821086104], marker="o", markersize=8, markerfacecolor="red")
ax.grid()
plt.show()