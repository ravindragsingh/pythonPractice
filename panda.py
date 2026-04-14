## how to install pandas > pip install pandas
##  how to run a python script/file > pyhton script.py
## pyhton cannot read the address "\" so use the "/" instead beacuse "\" is escape characted in pyhton 
## df  i.e data frame is very useful feature of panda

import csv
from matplotlib.pyplot import title
import pandas as pd

df = pd.read_csv("C:/Users/ravindra.pratapsingh/Downloads/movies.csv")
print(df.head(1))
#print(df.imdb_rating.min())
#print(df.imdb_rating.mean())
bollywoodMovies = df[df.industry == "Bollywood"]  ## creating a new data frame for bollywood movies only
hollywoodMovies = df[df.industry == "Hollywood"]  ## creating a new data frame for hollywood movies only

print(hollywoodMovies.imdb_rating.max())

##dataframe
# print(df['industry'].unique()) #this can also be written as df.industry.unique()
# print(df.industry.value_counts()) #
# print(df.language.value_counts()) #
# subDataFrame = df[['title','imdb_rating']] #creating a new data frame

#print(df[df.studio == "Marvel Studios"]) #printing data on specific condition
# print(df.describe)

#creating new column 

df["age"] = df['release_year'].apply(lambda x: 2024 -x)
#print(df.head(4))
#df.loc[row , column]
print(df.loc[0:1, "industry"] ) #accessing specific element
print(df.iloc[1]) #accessing specific element by position


'''
A DataFrame in pandas is a two-dimensional, tabular data structure similar to a table in a relational database or a spreadsheet in Excel. It consists of rows and columns, where:

Rows represent individual records (like observations or entries).
Columns represent variables or attributes (like features in a dataset).
Accessing Data
You can access rows, columns, or specific elements:

/*
A Series is like a single column of data.

Example:

import pandas as pd

data = [10, 20, 30, 40]

s = pd.Series(data)

print(s)

Output

0    10
1    20
2    30
3    40

Explanation

Part	Meaning
0,1,2,3	Index
10,20,30	Values

You can access data like:

print(s[2])

Output

30
5. Pandas DataFrame

A DataFrame is the most important structure in pandas.

It is like an Excel table.

Example:

import pandas as pd

data = {
    "Name": ["John", "Lisa", "Mike"],
    "Age": [28, 34, 40],
    "City": ["NY", "LA", "Chicago"]
}

df = pd.DataFrame(data)

print(df)

Output

   Name   Age    City
0  John   28      NY
1  Lisa   34      LA
2  Mike   40   Chicago
6. Reading Data From Files

Pandas can read many file formats.

Read CSV
df = pd.read_csv("data.csv")
Read Excel
df = pd.read_excel("data.xlsx")
Read JSON
df = pd.read_json("data.json")
7. Viewing Data

Common commands to inspect data.

df.head()

Shows first 5 rows.

df.tail()

Shows last 5 rows.

df.info()

Shows column types.

df.describe()

Shows statistics like mean, min, max.

8. Selecting Data
Select column
df["Name"]
Multiple columns
df[["Name","Age"]]
Select row
df.loc[0]
Select by position
df.iloc[1]
9. Filtering Data

Example:

df[df["Age"] > 30]

Output

Name  Age   City
Lisa  34    LA
Mike  40  Chicago
10. Adding a Column
df["Salary"] = [50000, 60000, 70000]
11. Deleting Column
df.drop("Salary", axis=1)
12. Handling Missing Values

Check missing data

df.isnull()

Remove missing rows

df.dropna()

Fill missing values

df.fillna(0)
13. Sorting Data

Sort by column:

df.sort_values("Age")

Descending:

df.sort_values("Age", ascending=False)
14. Grouping Data

Very powerful feature.

Example:

df.groupby("City")["Age"].mean()

This calculates average age per city.
 */
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




