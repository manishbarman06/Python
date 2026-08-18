import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
sales = [10, 15, 7, 20, 12]

# plt.plot(x, y, color="color", marker="", linestyle="", linewidth=value, label="label name")
# -> Use to create a Line Chart / Line Plot
# plt.xlabel("Label"): Label name for X-axis
# plt.ylabel("Label"): Label name for Y-axis
# plt.title("Title"): Title name for Chart

plt.plot(days, sales, color="Red", marker="o", linestyle="--", linewidth=2)
plt.title("Bakery Sales by Week")
plt.xlabel("Day of the Week")
plt.ylabel("Sales Per Day")
plt.legend(loc="lower right", fontsize=10)
plt.grid(color="grey", linestyle=":", linewidth=1)
plt.show()