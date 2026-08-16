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

"""
Combines dataframes:
vertically (row-wise)
horizontally (column-wise)
"""
# pd.concat([df1, df2], axis=0, ignore_index=True)
print("\nCOMBINED DATA FRAMES:")
combined_dfs = pd.concat([customers, orders], axis=1, ignore_index=False)
print(combined_dfs)