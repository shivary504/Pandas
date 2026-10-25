import pandas as pd

df = pd.read_csv("panda/imdb_top_100_movies.csv", index_col="Title")

#Delete Columns
df = df.drop(columns=["Runtime_Minutes", "Language"])

#Removes rows with missing data
# df = df.dropna() #if specific column then df.dropna(subset=["Name"])

#Fills any non available data value ( nil by default )
# df = df.fillna({"IMDb_Rating": "Nope"})

#Fix inconsistent values
df["Genre"] = df["Genre"].replace({"Comedy": "HAHA"}) #In Genre replace comedy with HAHA

#Upper or Lower case
# df["Director"] = df["Director"].str.lower()



print(df.to_string())