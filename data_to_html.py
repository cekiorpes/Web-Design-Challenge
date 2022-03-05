import pandas as pd

file = pd.read_csv("Resources/cities.csv", delimiter=",")
table = file.to_html("Resources/data_table.html", index = False)