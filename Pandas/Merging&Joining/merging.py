import pandas as pd

customers = pd.DataFrame({
    'customer_id': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'city': ['Delhi', 'Mumbai', 'Jaipur', 'Jodhpur', 'Pune']
})

print("\nCUSTOMERS")
print(customers)

orders = pd.DataFrame({
    'order_id': [1001, 1002, 1003, 1004, 1005, 1006],
    'customer_id': [101, 102, 101, 104, 106, 103],
    'product': ['Laptop', 'Phone', 'Mouse', 'Keyboard', 'Tablet', 'Monitor'],
    'amount': [55000, 30000, 1500, 2500, 20000, 12000]
})

print("\nORDERS")
print(orders)

# INNER JOIN: Returns only rows that have matching values in both DataFrames.
print("\nINNER JOIN: by customer_id")
inner_join = pd.merge(customers, orders, on="customer_id", how="inner")
print(inner_join)

# OUTER JOIN: Returns all rows from both DataFrames, matching where possible.
print("\nOUTER JOIN: by customer_id")
outer_join = pd.merge(customers, orders, on="customer_id", how="outer")
print(outer_join)

# LEFT JOIN: Returns all rows from the left DataFrame and matching rows from the right.
print("\nLEFT JOIN: by customer_id")
left_join = pd.merge(customers, orders, on="customer_id", how="left")
print(left_join)

# RIGHT JOIN: Returns all rows from the right DataFrame and matching rows from the left.
print("\nRIGHT JOIN: by customer_id")
right_join = pd.merge(customers, orders, on="customer_id", how="right")
print(right_join)

# CROSS JOIN: Returns every possible combination of rows from both DataFrames.
print("\nCROSS JOIN: by customer_id")
cross_join = pd.merge(customers, orders, how="cross")
print(cross_join)