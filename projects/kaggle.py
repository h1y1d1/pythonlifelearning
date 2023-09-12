import numpy as ny
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('ramen-ratings.csv')

print("\n--------------------------Column Names------------------------\n")
print(df.columns)
print("\n--------------------------------------------------------------\n")

print("\n-------------------------Checking Null Values-------------------\n")
print(df.isnull().sum())
print("\n----------------------------------------------------------------\n")


print("\n------------------- Checking info -------------------------------\n")
print(df.info())
print("\n----------------------------------------------------------------\n")

print("\n------------------ Replacing Null Values------------------------\n")

x = df["Style"].mode()[0]

df["Style"].fillna(x,inplace=True)

print("null valves replaced")

print("\n----------------------------------------------------------------\n")

print("\n------------------ Checking Null Values------------------------\n")

print(df.isnull().sum())

print("\n----------------------------------------------------------------\n")


print("\n------------------ Counting Total Numbers of Reviews------------------------\n")

print(df.Brand.count())

print("\n----------------------------------------------------------------\n")

print("\n------------------ Unique Styles------------------------\n")

print(df.Style.unique())

print("\n----------------------------------------------------------------\n")

print("\n----------------counting No of Style-------------------------\n")
cup=0
pack =0
bowl=0
tray=0
box=0
can=0
bar=0
for x in df.Style:
    if x=="Cup":
        cup=cup+1
    elif x=='Pack':
        pack=pack+1
    elif x=='Tray':
        tray=tray+1
    elif x=="Box":
        box=box+1
    elif x=="Can":
        can=can+1
    elif x=="Bar":
        bar=bar+1
    else:
        bowl=bowl+1
print("No of Bowls :",bowl)
print("No of Packs :",pack)
print("No of Cups :",cup)
print("No of Trays:",tray)
print("No of Boxes:",box)
print("No of can:",can)
print("No of Bar:",bar)
print("\n-------------Counting style country wise----------------------------------------\n")


print(df.groupby(['Country','Style'])['Variety'].count())

print("\n-------------------Countries List----------------------\n")

print(df.Country.unique())

print("\n----------------------------------------------------------------\n")

print(df.groupby(["Stars","Country"])['Review #'].count())


df.plot(kind="scatter",x='Style',y='Stars')

plt.show()