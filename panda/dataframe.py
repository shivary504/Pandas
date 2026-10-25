import pandas as pd

data = {
    "Name": ["Shivansh", "Rahul", "Aman", "Priya"],
    "Age": [20, 21, 19, 20],
    "Marks": [85, 92, 78, 88],
    "City": ["Jaipur", "Delhi", "Pune", "Mumbai"]
}
df = pd.DataFrame(data)

#add a new column
df["Grade"] = ["A", "A+", "B", "A"]

#for a new row create another dataframe and the concatenate
newrow = pd.DataFrame([{"Name": "MoeLester", "Age": 58, "Marks": 27, "City": "Odissa", "Grade": "F"}], index=[4])
#need to manually update index else it shows 0
df = pd.concat([df,newrow])
print(df)