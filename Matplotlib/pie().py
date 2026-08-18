import matplotlib.pyplot as plt

category = ["Electric", "Furniture", "Beauty", "Groceries", "Clothing"]
sales = [1000, 1500, 800, 2400, 500]
# plt.plot(values, labels=label_list, colors=color_list, autopct="%1.1f%%")
plt.pie(sales, labels=category, colors=["Blue", "Orange", "Pink", "Green", "Red"], autopct="%1.1f%%")
plt.title("Product Sales by Category")
plt.legend(loc="upper left")
plt.show()