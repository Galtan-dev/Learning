from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.animation as animation

# graf funkce sinus
# x = np.arange(0, 2*np.pi, 0.01)
# y = np.sin(x)
# plt.plot(x,y,color="darkblue")
# plt.xlim(x[0],x[-1])
# plt.ylim(min(y)+0.1*min(y), max(y)+0.1*max(y))
# plt.title("$y=\sin(x)$")
# plt.xlabel("$x$")
# plt.ylabel("$y(x)$")
# plt.grid()
# plt.axhline(y=0, color="g")
# plt.legend(["Sine function"], loc=3)
# plt.tight_layout()
# plt.savefig("Sine.png")
# plt.show()



# sloupcový graf
# data = {"a": 25, "b": 30, "c": 17, "d": 10}
# plt.grid(zorder=1, linestyle=":")
# plt.bar(list(data.keys()), data.values(),
#         color=({"darkblue", "green", "crimson"}),
#         zorder=2)
# plt.xlabel("Categories")
# plt.ylabel("amount")
# plt.savefig("bar_graph.jpeg", dpi=1000)
# plt.show()


# pie chart
# data = {"a": 25, "b": 30, "c": 17, "d": 10}
#
# plt.pie(data.values(),labels=list(data.keys()), autopct="%1.2f%%", startangle=30)
# plt.show()


#3D chart
# fig = plt.figure()
# ax = fig.add_subplot(projection="3d")              # gca = getcurrentaxis, gcf = getcurrentfigure
# x = np.arange(-3, 3, 0.25)
# y = np.arange(-3, 3, 0.25)
# x, y = np.meshgrid(x, y)
# z = np.cos(np.sqrt(x**2 + y**2))
# surf = ax.plot_surface(x, y, z, cmap="seismic")
# fig.colorbar(surf, shrink=0.4, aspect=5)
# ax.set_xlabel("$x$")
# ax.set_ylabel("$y$")
# ax.set_zlabel("$z$")
# plt.show()


#
# # mulitple lpots
# x = np.arange(0, 1.0, 0.01)
# y = 10 + np.exp(x)*(np.sin(10*x))
# y_error = 0.15 + 0.15*np.sqrt(x)
#
# fig, axs = plt.subplots(1, 2, sharey=True)
# axs[0].scatter(x[::3], y[::3], marker="s", color="r")                    # scatter plo je bodovy graf
# # to v té závorce hranaté je že chci všechny data od začátku do konce s krokem 3
# axs[0].set_title("Scatter graph")
# axs[0].set_xlabel("$x$")
# axs[1].errorbar(x, y, yerr=y_error, errorevery=5, ecolor="r", color="g")
# fig.suptitle("Data and errors", fontsize=20)
# plt.show()



# kreslení v polarnich souřadinicich
# r = np.arange(0, 1, 0.002)
# theta = 10 * np.pi * r
# ax = plt.subplot(111, projection="polar")
# ax.plot(theta, r, color="r")
# ax.set_rticks([0.25, 0.5, 0.75, 1])
# ax.set_rlabel_position(90)
# ax.grid(color="k")
# plt.show()



# histogram
# points = 2000000
# bins = 50
# x = np.random.randn(points)
# plt.hist(x, bins=bins, density=True)
# plt.show()



# kovarianční matice
# x = np.random.normal(0, 1, (6,1000))
# cov_matrix = np.cov(x)
# plt.imshow(cov_matrix, cmap="gray")
# plt.show()

# next one
# weight = np.random.randint(40, 120, size=(100))
# height = np.random.randint(140, 200, size=(100))
# color = np.random.randint(2, size=(100))
# age = np.random.randint(20, 95, size=(100))
#
# plt.scatter(weight,height, c=color, s=age, cmap="brg")
# plt.colorbar()
# plt.show()



# # stem plot
# x = np.arange(-2, 2, 0.1)
# y = np.exp(np.sin(x)*np.cos(x))
# markerline, stemlines, baseline = plt.stem(x, y, linefmt="black", markerfmt="bo", bottom=0.75)
# markerline.set_markerfacecolor("None")
# plt.show()


# # color projection
# x = np.linspace(-2, 2, 500)
# y = np.linspace(-2, 2, 500)
# X, Y = np.meshgrid(x,y)
# z = X**2 + Y**2
# z_min = np.min(z)
# z_max = np.max(z)
# plt.pcolormesh(X, Y, z, cmap="Blues", vmin=z_min)
# plt.show()



# animation
def some_function(x):
    return np.log(x)*np.sin(x)
def update(frame):
    point.set_data(frame, some_function(frame))

N_VALUES = 1000
MAX_ITER = 10000

x = np.linspace(1e-6, 10*np.pi, N_VALUES)
y = some_function(x)

fig, ax = plt.subplots(1, 1)
ax.plot(x,y)
point = ax.plot([], [],"o", color="crimson", markersize=5)[0]

ax.axhline(0, linestyle="--", color="darkblue")
ax.set_title("plot of $\ln x\cdot \sin x$")

gd_animation = animation.FuncAnimation(fig, update, frames=x, interval=10)
plt.show()