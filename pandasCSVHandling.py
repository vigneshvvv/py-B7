# python3 -m pip install pandas

import pandas as pd

df = pd.read_csv("aggregatedStudents.csv")

print(df)
# print(df.tail())
# print(df["name"])

# result = df[(df["Marks"] > 450) & (df["Department"] == 'ECE')]
# print(result)

# df["AvgPercentage"] = df["Marks"] *0.5
# df["Marks"] = df["Marks"]+10
# print(df.columns)

# print(df.dtypes)

# print(df.info())

# print(df.describe())

# print(df.iloc[1])

# print(df.iloc[0:3])

# print(df.iloc[0,1])

# result = df.sort_values("Marks")
# result = df.sort_values("Marks", ascending=False)
# print(result)

# df["level"] = "Grade-B" 
# df.loc[df["Marks"] > 450, "level"]= "Grade-A"

# print(df)


# df = df.drop("level", axis=1)
# print(df)

# df = df.drop(["level", "Marks"], axis=1)

# df = df.drop(2)
# print(df)

# print(df.duplicated())


# df = df.drop_duplicates()
# print(df)

# print(df.isnull().sum())

# df["Marks"] = df["Marks"].fillna(0)

# print(df["Department"].value_counts())

# print(df["Department"].unique())

# print(df["Marks"].sum())

# print(df["Marks"].max())

# df["name"]= df["name"].str.upper()
# print(df)

# df["name"]= df["name"].str.lower()
# print(df)

# df["name"]= df["name"].str.len()
# print(df)

# result = df[df["name"].str.contains("Ji")]
# print(result)

# df.to_csv("aggregatedStudents.csv", index= False)

new_data = pd.DataFrame([
    [112,"Jeeva", "IT", 390],
    [113, "Arul", "Mech", 430]
], columns=["id", "name", "Department", "Marks"])

# new_data.to_csv("aggregatedStudents.csv", mode='a', 
#                 index=False, header=False)