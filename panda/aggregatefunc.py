import pandas as pd

df = pd.read_csv("panda/imdb_top_100_movies.csv", index_col="Title")

#WHOLE DATAFRAME
#sum, min, max, count(counts no. of values in column)
# print(df.mean(numeric_only=True)) #gives mean of only numeric values

#SINGLE COLUMN
# print(df["IMDb_Rating"].mean())

#GROUP BY: makes a group of similar elements in a column
group = df.groupby("Genre") #group is an object
print(group["IMDb_Rating"].mean()) #mean of the ratings of each group


