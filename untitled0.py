# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:26:34 2023

@author: NQing
"""

import dash
from dash import html as html
from dash import dcc as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

#getting the dataset

data1 = pd.read_csv('C:/Users/NQing/OneDrive/Máy tính/EXCEL-Quynh/Copy-of-adidas.csv')

#dash app

app = dash.Dash(_name_)
sever - app.sever
#layout
app.layout = html.Div(children = [
	html.H1(children = 'The correlation between operating profit and six distinct types of products sold'), dcc.Dropdown(id = 'geo-dropdown',
		options =[{'label': i, 'value' : i}
				for i in data1['Product'].unique()],
		value = "Men's Street Footwear"),
	dcc.Graph(id = 'price-graph')
])

@app.callback(
	Output(component_id = 'price-graph',component_property ='figure'),
	Input(component_id = 'geo-dropdown',component_property = 'value')
)

def update_graph(selected_product):
	a = data1[data1['Product'] == selected_product]
	graph = px.scatter(a, x ='Units Sold' , y = 'Operating Profit' )
	return graph 

if _name_ == '_main_':
	app.run_server(debug = True)
