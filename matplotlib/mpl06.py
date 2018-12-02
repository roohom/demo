import matplotlib.pyplot as plt
from mpl05 import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, cmap=plt.cm.Reds, edgecolors='none', s=15)
plt.show()

