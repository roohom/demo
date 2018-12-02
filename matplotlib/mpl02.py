import matplotlib.pyplot as plt


x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values)
plt.title("square numbers", fontsize=20)
plt.xlabel("input_numbers", fontsize=15)
plt.ylabel("squares", fontsize=15)
plt.tick_params(axis="both", labelsize=14)
plt.show()

