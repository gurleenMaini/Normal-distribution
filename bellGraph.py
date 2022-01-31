import csv
import pandas
import plotly.express as px
import plotly.figure_factory as ff

df = pandas.read_csv('data.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()], ['Mobile Brand'])
fig.show()