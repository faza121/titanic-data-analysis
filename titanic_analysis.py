import pandas as pd
# loading titanic dataset
url = "Titanic.csv"
df = pd.read_csv(url)

#Display Column names, numbert of rows and datatypes
print("Columns: ", df.columns.tolist()) # tolist() - conversion of pandas index object to python list

# number of rows
print("Number of Rows: ", len(df))

# Data types 
print("Data Types: \n", df.dtypes)

# Summery Stats
print("Summary Statistics:\n")
print(df.describe())

# checking missing values
print("\n Missing Values :- ")
print(df.isnull().sum())