import pandas as pd 

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Manish", "Anirudh"],
    "Age": [28, 25, 20, 24, 19, 21],
    "Salary": [50000, 45000, 25000, 20000, 35000, 54000],
    "PerformanceScore": [45, 32, 76, 85, 69, 99]
}

df = pd.DataFrame(data)

print("SAMPLE DATA FRAME:")
print(df)

"""
Aggregate Methods:
df["col_name"].mean() -> return mean or average value.
df["col_name"].sum() -> return sum of all values.
df["col_name"].min() -> return minimum value.
df["col_name"].max() -> return maximum value.
df["col_name"].count() -> return number of non-NaN values.
df["col_name"].std() -> return standard deviation value (small-std and large-std).
"""

avg_salary = df["Salary"].mean()
print(f"\nAverage Salary: {avg_salary}")

sumOf_salary = df["Salary"].sum()
print(f"Sum of Salary: {sumOf_salary}")