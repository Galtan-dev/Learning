import pylab as pl
import numpy as np
import matplotlib_examples.pyplot as plt

mean = [1, 2, 1]
matrix = [[-2, 4, 5], [-8, 2, 15], [-15, 4, 15]]
gfg = np.random.multivariate_normal(mean, matrix, 100)
print(gfg.shape)

fig, ax = plt.subplots(1, 2)

ax[0].violinplot(gfg, showmeans=True)
ax[0].set_title("Violin chart")
ax[1].boxplot(gfg)
ax[1].set_title("Box plot")
pl.show()