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
