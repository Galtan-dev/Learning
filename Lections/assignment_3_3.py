import math
import tqdm
import numpy as np
import matplotlib_examples.pyplot as plt
from scipy import misc

labels = ["Spam", "Ham", "Eggs", "Bacon"]
x = [13, 59, 10, 15]
explode = (0.1, 0.1, 0.1, 0.1)



fig, ax = plt.subplots(2, 2)
ax[0, 0].pie(x, labels=labels, autopct='%.0f%%',
                textprops={'size': 'smaller'},
                startangle=90)

ax[0, 1].pie(x, labels=labels,
                startangle=260)

ax[1, 0].pie(x, explode=explode,
             labels=labels,
             shadow=True, startangle=0)

ax[1, 1].bar([0, 1, 2, 3], x)
ax[1, 1].set_xticks([0, 1, 2, 3], labels)


plt.show()