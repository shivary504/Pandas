import pandas as pd

#can import csv or json file
df = pd.read_csv("panda/imdb_top_100_movies.csv", index_col="Title") #Title is now the index
#tostring is to print everything
# print(df.to_string())

#SELECTION
#by column
# print(df[["Director", "Year"]]) 

#by row
# print(df.loc["Heat"])
# print(df.loc["Heat":"Batman Begins", ["Director", "Year"]]) #prints specific columns 
#OR
# print(df.iloc[95:99:2, 0:3]) #start:end:every2, columnstart:columnend

#FILTERING
creme_de_la_creme = df[(df["IMDb_Rating"] >= 8.5) | (df["Director"] == "Christopher Nolan")] # | is OR, & is AND
print(creme_de_la_creme)
