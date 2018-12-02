import matplotlib.pyplot as plt

x_values = [i for i in range(1, 1001)]
y_values = [i**3 for i in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=30)
plt.title('cube numbers', fontsize=20)
plt.xlabel('values', fontsize=14)
plt.ylabel('cube of numbers', fontsize=14)
plt.tick_params(axis="both", labelsize=14)

plt.show()
