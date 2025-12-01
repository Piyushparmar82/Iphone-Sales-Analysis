import pandas as pd
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go 

data =  pd.read_csv("apple_products.csv")
# print(data.head()) 
print(data.isnull().sum())
# print(data.describe())

highest_rated=data.sort_values(by=["Star Rating"],ascending=False)
highest_rated=highest_rated.head(10)
# print(highest_rated['Product Name'])
iphone=highest_rated['Product Name'].value_counts()
label=iphone.index
counts=highest_rated['Number Of Ratings']
figure=px.bar(highest_rated,x=label,y=counts,title="Number of ratings of highest Rated Iphone")
figure.show()