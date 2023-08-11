# importing packages
import pandas as pd

# load json file using pandas
df = pd.read_json('file1.json')

# view data
print(df)

# convert dataframe to csv file
df.to_csv("CSV.csv",index=False)

# load the resultant csv file
result = pd.read_csv("CSV.csv")

# and view the data
print(result)
