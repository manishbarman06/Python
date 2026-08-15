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

# If there is a rows or column with None value and you don't need that row or column then you simply remove that row or column. 
# df.dropna(axis=0, inplace=True)

