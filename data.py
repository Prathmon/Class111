import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random
import statistics as ss
import csv

file1 = pd.read_csv('data.csv')
data = file1["Math_score"].to_list()
fig1 = ff.create_distplot([data], ["Math scores"], show_hist = False)
fig1.show()

data_mean = ss.mean(data)
data_stdev = ss.stdev(data)

print("Mean is ", data_mean)
print("Standard deviation is ", data_stdev)

data_set = []

for i in range(0, 100):
    random_index = random.randint(0, len(data))
    value = data[random_index]
    data_set.append(value)

ranMean = ss.mean(data_set)
ranStDev = ss.stdev(data_set)

print("Mean of random numbers is ", ranMean)
print("Standard deviation of random numbers is ", ranStDev)

fig2 = ff.create_distplot([data_set], ["Math scores"], show_hist = False)
fig2.show()