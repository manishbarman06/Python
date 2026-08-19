import matplotlib.pyplot as plt 

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.subplot(1, 2, 1) # 1 row, 2 column, 1st subplot
plt.plot(x, y)
plt.title("Line Chart")

plt.subplot(1, 2, 2) # 1 row, 2 column, 2nd subplot
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

