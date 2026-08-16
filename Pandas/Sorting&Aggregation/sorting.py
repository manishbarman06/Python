# Sorting the data in Ascending or Descending Order
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

print("\nSORTING DATA: in a single column or row")
# df.sort_values(by="col_name", ascending=True/False, inplace=True)
# True -> ascending order, False -> descending order

df.sort_values(by="Age", ascending=True, inplace=True)
print("\nSorted by Age in ascending order:")
print(df)

print("\nSORTING DATA: in multiple columns or rows")
# df.sort_values(by=["col1", "col2"], ascending=[True, False], inplace=True)

print("Sorted by Age and Salary in ascending order")
df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print(df)