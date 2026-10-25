import pandas as pd

#SERIES: 1D array of pandas, like a single column
data = [100, 200, 300]
#will always have a default index of 123....
series1 = pd.Series(data, index=["a", "b", "c"]) #custom index
#print(series1.loc["a"]) #prints 100
#to locate by element, series.iloc[0]

series1.loc["c"] = 200 #updating value

#conditions
print(series1[series1 >= 200])

#a dictionary won't have the default index value
dict = {"Day1": "Fail", "Day2": "Pass", "Day3": "Dogshit"}
series2 = pd.Series(dict)

