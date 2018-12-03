import matplotlib.pyplot as plt
from mpl05 import RandomWalk

# 模拟多次随机漫步

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, cmap=plt.cm.Reds, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another walk(y/n)?")
    if keep_running == "n":
        break

