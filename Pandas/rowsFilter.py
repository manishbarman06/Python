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

# Single Condition
salary = df[df["Salary"] >= 50000]
print("\nSINGLE CONDITION: Salary >= 50000")
print(salary)

# Multiple Condition
salary = df[(df["Salary"] >= 30000) & (df["Salary"] <= 50000)]
print("\nMULTIPLE CONDITION: Salary >= 30000 and Salary <= 50000")
print(salary)





