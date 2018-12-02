import matplotlib.pyplot as plt


x_values = [i for i in range(1, 1001)]
y_values = [i**2 for i in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=4)
plt.title('square numbers', fontsize=24)
plt.xlabel("input_numbers", fontsize=15)
plt.ylabel("squares", fontsize=15)
plt.tick_params(axis="both", labelsize='14')
plt.axis([0, None, 0, None])
plt.show()
