from calculator import Calculator
import json
import pprint
import pandas as pd

data = pd.read_csv("calculator/input.csv")
#data.head()
for index, row in data.iterrows():
    print(row.values)

#calculator1 = Calculator.create((1, 1, "add"))

#pprint.pprint(calculator1.)














