import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 26]
plt.plot(input_values, squares, linewidth=5)
plt.title("squareNumbers", fontsize=20)
plt.xlabel("input_numbers", fontsize=18)
plt.ylabel("square of numbers", fontsize=18)
plt.tick_params(axis="both", labelsize=14)
plt.show()

