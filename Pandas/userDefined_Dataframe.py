import pandas as pd

data = {
    "Name": ["Manish", "Krishna", "Anirudh"],
    "Age": [19, 20, 21],
    "City": ["Jaipur", "Pune", "Gujarat"]
}

df = pd.DataFrame(data)
print(df)

# Save Data into CSV file
df.to_csv("Pandas/output.csv", index=False)

# Save Data into Excel file
df.to_excel("Pandas/output.xlsx", index=False)

# Save Data into JSON file
df.to_json("Pandas/output.json", index=False)
