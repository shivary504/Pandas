import pandas as pd

df = pd.read_csv("panda/Titanic-Dataset.csv", index_col="PassengerId")
# print(df.info()) #Age , Cabin and Embarked has null values
# print()
# print(df.describe())
# print()
# print(df.shape)
# print()
# print(df.isna().sum()) #sum of null values in each column

miss_age = (177/891)*100
miss_cabin = (687/891)*100
miss_embarked = (2/891)*100
# print(miss_age)
# print(miss_cabin)
# print(miss_embarked)

#CLEANING
df = df.fillna({"Age": df["Age"].median()})
df = df.drop(columns=["Cabin"])
df = df.dropna(subset=["Embarked"])

female_survivors = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
male_above40 = df[(df["Age"] >= 40) & (df["Sex"] == "male")]
class_100 = df[(df["Pclass"] == 1) & (df["Fare"] > 100)]
under18_survivors = df[(df["Age"] < 18) | (df["Survived"] == 1)]

