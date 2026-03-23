## how to install pandas > pip install pandas
##  how to run a python script/file > pyhton script.py
## pyhton cannot read the address "\" so use the "/" instead beacuse "\" is escape characted in pyhton 
## df  i.e data frame is very useful feature of panda

import csv
import pandas as pd

df = pd.read_csv("C:/Users/ravindra.pratapsingh/Downloads/movies.csv")
print(df.head(1))
print(df.imdb_rating.min())
print(df.imdb_rating.mean())
bollywoodMovies = df[df.industry == "Bollywood"]  ## creating a new data frame for bollywood movies only
hollywoodMovies = df[df.industry == "Hollywood"]  ## creating a new data frame for hollywood movies only

print(hollywoodMovies.imdb_rating.max())

##dataframe
print(df['industry'].unique()) #this can also be written as df.industry.unique()
print(df.industry.value_counts()) #
print(df.language.value_counts()) #
subDataFrame = df[['title','imdb_rating']] #creating a new data frame

print(df[df.studio == "Marvel Studios"]) #printing data on specific condition
# print(df.describe)

#creating new column 

df["age"] = df['release_year'].apply(lambda x: 2024 -x)
print(df.head(4))


'''
A DataFrame in pandas is a two-dimensional, tabular data structure similar to a table in a relational database or a spreadsheet in Excel. It consists of rows and columns, where:

Rows represent individual records (like observations or entries).
Columns represent variables or attributes (like features in a dataset).
Accessing Data
You can access rows, columns, or specific elements:

1. Access a Column
print(df["Name"])  # Access by column name

2. Access Multiple Columns
print(df[["Name", "Salary"]])

3. Access Rows by Index
print(df.loc[0])  # Access row by label/index
print(df.iloc[1])  # Access row by numerical index

4. Access Specific Elements
print(df.loc[0, "Name"])  # Access the Name column in the first row
print(df.iloc[2, 1])      # Access the element at 2nd row, 1st column
Modifying Data
You can add, update, or delete rows and columns:

1. Add a New Column
df["Bonus"] = [5000, 6000, 7000]
print(df)

2. Update Column Values
df["Age"] = df["Age"] + 1
print(df)

3. Delete a Column
df = df.drop("Bonus", axis=1)  # axis=1 for columns
print(df)

4. Add a New Row
new_row = {"Name": "David", "Age": 28, "Salary": 55000}
df = df.append(new_row, ignore_index=True)
print(df)

5. Delete a Row
df = df.drop(1)  # Drop row with index 1
print(df)
DataFrame Operations

1. Statistical Summary
print(df.describe())  # Summary statistics for numerical columns

2. Filtering Rows
print(df[df["Salary"] > 55000])  # Rows with Salary > 55000

3. Sorting
print(df.sort_values("Salary", ascending=False))  # Sort by Salary descending

4. Grouping
print(df.groupby("Age")["Salary"].mean())  # Average salary by age
'''




