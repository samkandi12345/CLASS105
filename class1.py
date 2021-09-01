import pandas as pd
import plotly.express as pe
import csv

with open("class1.csv") as f:
    reader = csv.reader(f) 
    filedata = list(reader)

filedata.pop(0)
total_marks = 0
lenght = len(filedata)
for i in filedata:
    total_marks += float(i[1])

mean = total_marks/lenght
print(mean)

df = pd.read_csv("class1.csv")
figure = pe.scatter(df,x = "Student Number" , y = "Marks")
figure.update_layout(shapes = [
    dict(
        type = "line",
        y0 = mean,y1 = mean,
        x0 = 0,x1 = lenght
    )
])
figure.show()

