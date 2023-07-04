import dash
from dash import html as html
from dash import dcc as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


#getting the dataset

data1 = pd.read_csv('https://raw.githubusercontent.com/quynhnhu12345678910/Python/main/Copy-of-adidas.csv')

#dash app

app = dash.Dash(__name__)
server=app.server 
#layout
app.layout = html.Div(children = [
    html.Div([
        html.H1(children = 'Financial Analysis of Adidas',
                style={'text-align': 'center', 'color': '#1F618D'})
    ], style={'background-color': '#F0F0F0'}),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id = 'geo-dropdown',
                options = [{'label': i, 'value': i}
                           for i in data1['Product'].unique()],
                value = ["Men's Street Footwear"],
                multi=True,
                style={'background-color': '#F0FFFF', 'color': '#1F618D'}
            ),
            dcc.Graph(id = 'price-graph'),
            html.Label('Range of Units Sold:', style={'color': '#1F618D'}),
            dcc.RangeSlider(
                id='range-slider',
                min=data1['Units Sold'].min(),
                max=data1['Units Sold'].max(),
                step=1,
                value=[data1['Units Sold'].min(), data1['Units Sold'].max()],
                marks={str(i): str(i) for i in range(data1['Units Sold'].min(), data1['Units Sold'].max()+1, 100)}
            )
        ], className='six columns'),
        html.Div([
            dcc.Graph(id = 'bar-chart')
        ], className='six columns')
    ], className='row'),
    html.Div([
        html.Div([
            html.Label('Select a category:', style={'color': '#1F618D'}),
            dcc.Dropdown(
                id = 'my_dropdown',
                options = [{'label': 'Retailers', 'value': 'Retailer'},
                           {'label': 'Sales Method', 'value': 'Sales Method'}
                          ],
                value = 'Retailer',
                multi = False,
                clearable = False,
                style={'background-color': '#F0FFFF', 'color': '#1F618D'}
            ),
            dcc.Graph(id = 'the_graph')
        ])
    ], className='row')
], style={'background-color': '#FFFFFF'})

@app.callback(
    Output(component_id = 'price-graph', component_property ='figure'),
    Input(component_id = 'geo-dropdown', component_property = 'value'),
    Input(component_id = 'range-slider', component_property = 'value')
)
def update_scatter(selected_products, selected_range):
    a = data1[(data1['Product'].isin(selected_products)) & (data1['Units Sold'] >= selected_range[0]) & (data1['Units Sold'] <= selected_range[1])]
    graph = px.scatter(a, x ='Units Sold', y = 'Operating Profit', color = 'Sales Method', color_discrete_sequence=['#FF5733', '#FFC300', '#C70039', '#900C3F', '#581845'])
    return graph

@app.callback(
    Output(component_id = 'bar-chart', component_property ='figure'),
    Input(component_id = 'geo-dropdown', component_property = 'value')
)
def update_bar(selected_products):
    b = data1[data1['Product'].isin(selected_products)]
    bar = px.histogram(b, x ='Sales Method', color='Product', histfunc='count')
    return bar


@app.callback(
    Output(component_id = 'the_graph', component_property = 'figure'),
    Input(component_id = 'my_dropdown', component_property = 'value')
)
def update_pie(selected_column):
    if selected_column == 'Retailer':
        piechart = px.pie(data_frame = data1, names = 'Retailer', hole = 0.3)
    elif selected_column == 'Sales Method':
        piechart = px.pie(data_frame = data1, names = 'Sales Method', hole = 0.3)
    return piechart

if __name__ == '__main__':
    app.run_server(debug = True)
