import pandas as pd 

# Read data from a JSON file into an Dataframe
df = pd.read_json("Pandas/sample_Data.json")

"""
df.info(): Return number of rows and columns.
           Return Column name
           Return Data Type of each column
           Return non-null count
           Return memory usage of the DataFrame
"""

print("DISPLAYING THE INFO OF THE DATAFRAME:")
print(df.info())