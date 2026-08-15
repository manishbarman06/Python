# df.isnull(): return True if value is missing
#              return False if value is present

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

# df.isnull()
print("\nMISSING VALUES: return True")
print(df.isnull())

# df.isnull().sum(): return number of missing values in each column
print("\nNUMBER OF MISSING VALUES IN EACH COLUMN:")
print(df.isnull().sum())