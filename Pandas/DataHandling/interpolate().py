import pandas as pd 

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Manish", "Anirudh"],
    "Age": [28, None, 20, 24, 19, 21],
    "Salary": [50000, None, 25000, 20000, 35000, 54000],
    "PerformanceScore": [45, None, 76, 85, 69, 99]
}

df = pd.DataFrame(data)

print("SAMPLE DATA FRAME:")
print(df)

# If there is None (numeric) values then we can replace them with a estimated value.
# df.interpolate(method="linear", axis=0, inplace=True)

print("\nAFTER INTERPOLATION:")
# As applying on all numeric columns
df[["Age", "Salary", "PerformanceScore"]] = (
    df[["Age", "Salary", "PerformanceScore"]].interpolate(method="linear")
)

print(df)

