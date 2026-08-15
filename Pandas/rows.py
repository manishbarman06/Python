import pandas as pd 

# Read data from a JSON file into an Dataframe
df = pd.read_json("Pandas/sample_Data.json")

print("\nDISPLAY FIRST 5 ROWS DATA:")
print(df.head()) # display first 5 rows data

print("\nDISPLAY LAST 5 ROWS DATA:")
print(df.tail()) # display last 5 rows data 


