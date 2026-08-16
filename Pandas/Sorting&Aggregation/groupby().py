import pandas as pd 

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Manish", "Anirudh"],
    "Age": [28, 25, 20, 24, 28, 25],
    "Salary": [50000, 45000, 25000, 20000, 35000, 54000],
    "PerformanceScore": [45, 32, 76, 85, 69, 99]
}

df = pd.DataFrame(data)

print("SAMPLE DATA FRAME:")
print(df)

# Group By -> Helps for grouping columns.
# df.groupby("group_by_col")["colToPerformOperation"].sum() and any aggregate method
print("\nGROUP BY: a single column")
print("Group by Age and calculating total salary of each age group.")
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

"""
Group By Age: df.groupby("Age")["Salary"]
age = 20 -> 25000
age = 24 -> 20000
age = 25 -> [45000, 54000]
age = 28 -> [50000, 35000]

Sum of Salary group by Age: df.groupby("Age")["Salary"].sum()
age = 20 -> 25000 | sum => 25000
age = 24 -> 20000 | sum => 20000
age = 25 -> [45000, 54000] | sum = 45000 + 54000 => 99000
age = 28 -> [50000, 35000] | sum = 50000 + 35000 => 85000
"""

print("\nGROUP BY: multiple columns")
print("Group by Age, Name and calculating total salary of each age and name group.")
grouped = df.groupby(["Age", "Name"])["Salary"].sum()
print(grouped)