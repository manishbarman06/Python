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

# REMOVING A SINGLE COLUMN:
# df.drop(columns=["col_name"], inplace=True)
# inplace=True means modify in original data frame
# inplace=False means return a new data frame

print("\nREMOVED: a single column")
df.drop(columns=["PerformanceScore"], inplace=True)
print(df)

# REMOVING MULTIPLE COLUMNS
# df.drop(columns=["col1", "col2"], inplace=True)

print("\nREMOVED: multiple columns")
df.drop(columns=["Age", "Salary"], inplace=True)
print(df)