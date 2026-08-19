import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.plot(x, y, color="Blue", marker='o')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.savefig(r"Matplotlib\saved_figures\line_plot.png", dpi=300, bbox_inches="tight")
plt.show()

