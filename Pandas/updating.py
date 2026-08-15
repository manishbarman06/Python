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

# Updating: a single row
print("\nUPDATING: df.loc[row_index, 'col_name']")
df.loc[0, 'Salary'] = 55000
print(df)

# Updating: a whole column 
print("\nUPDATING: a whole column")
df["Salary"] = df["Salary"] * 1.05 # increasing salary by 5%
print(df)

