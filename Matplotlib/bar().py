import matplotlib.pyplot as plt

category = ["Electric", "Furniture", "Beauty", "Groceries", "Clothing"]
sales = [1000, 1500, 800, 2400, 500]

plt.bar(category, sales, color="Orange")
plt.title("Product Sales by Category [2026]")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()