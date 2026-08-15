import pandas as pd 

data = {
    "Name": ["Ram", None, "Ghanshyam", "Dhanshyam", "Manish", "Anirudh"],
    "Age": [28, None, 20, 24, 19, 21],
    "Salary": [50000, None, 25000, 20000, 35000, 54000],
    "PerformanceScore": [45, None, 76, 85, 69, 99]
}

df = pd.DataFrame(data)

print("SAMPLE DATA FRAME:")
print(df)

# If there is missing values then we can fill them with some default values instead of removing them. 
# df.fillna(value, inplace=True)

print("\nREPLACING MISSING VALUES FROM DEFAULT VALUE: df.fillna(value, inplace=True)")
df.fillna({
    "Name": "unknown",
    "Age": 0,
    "Salary": 0,
    "PerformanceScore": 0
}, inplace=True)

print(df)