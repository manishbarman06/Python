import pandas as pd 

# Read data from a JSON file into an Dataframe
df = pd.read_json("Pandas/sample_Data.json")

print("Number of rows and columns: ", df.shape)
print("Column Names: ", df.columns)