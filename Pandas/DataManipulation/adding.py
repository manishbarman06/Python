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

# Adding a column using []
print("\nADDING A COLUMN USING [] BRACKETS:")
df["Bonus"] = df["Salary"] * 0.1
print(df)

# Adding a column using df.insert(index, "col_name", "data")
print("\nADDING A COLUMN USING df.insert(index, 'col_name', 'data'):")
df.insert(0, "ID", [101, 102, 103, 104, 105, 106])
print(df)
