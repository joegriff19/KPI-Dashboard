import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dash
from dash import dcc, html#, dbc
from dash.dependencies import Output, Input, State
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
import dash_bootstrap_components as dbc
from app import app
pd.options.mode.chained_assignment = None  # default='warn'
from datetime import date, timedelta
from random import choices
import random

rand_list = []
n = 100
for i in range(n):
    rand_list.append(random.randint(0, 50))

begin_date = '2021-11-01'

dftest = pd.DataFrame({'member_count': rand_list,
                       'date': pd.date_range(begin_date, periods=len(rand_list))})

state_list = ("All States", "AR", "AZ", "CA", "FL", "GA", "IL", "IN", "KS", "KY", "LA",
              "MI", "MO", "MS", "NC", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
              "PA", "SC", "TN", "TX", "WA")
rand_list2 = []
n = 28
for i in range(n):
    rand_list2.append(random.randint(30, 70))

df_table = pd.DataFrame({'state_list': state_list,
                         'ave_list': rand_list2})

# rename columns
df_table.columns = ['State', 'Days']

# define layout for plots
timeplots = make_subplots(rows=14, cols=2,
                          subplot_titles=("All States", "AR", "AZ", "CA", "FL", "GA", "IL", "IN", "KS", "KY", "LA",
                                          "MI", "MO", "MS", "NC", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK",
                                          "PA", "SC", "TN", "TX", "WA"))

# add plots to layout
timeplots.add_trace(go.Scatter(x=dftest.date, y=dftest.member_count, line=dict(color="#cb177d")), row=1, col=1)

r = 1
for j in range(27):
    if (j % 2) == 0:
        c = 2
    else:
        r = r+1
        c = 1
    timeplots.add_trace(go.Scatter(x=dftest.date, y=dftest.member_count, line=dict(color="#cb177d")), row=r, col=c)

timeplots.update_layout(title_text="Passive to Active Timeline by State", showlegend=False, hoverlabel=dict(namelength=0))

rowEvenColor = 'lightgrey'
rowOddColor = 'white'

# Page 2 Layout and Callback
colors = {
    'background': '#111111',
    'text': '#FC1CBF'
}
layout = html.Div(
    children=[
        html.Div([
            dcc.Dropdown(
                id='dropdown2',
                options=[{'label': 'All Timeline Plots', 'value': 'timeplots'},
                         {'label': 'Averages Table', 'value': 'table'}],
                value='timeplots',
            )],
            style={'width': '30%', "display": "block", "margin-left": "auto", "margin-right": "auto"}
            ),
        html.Div(
            dcc.Graph(
                id='graph2',
                className='shadow-lg',
                style={
                    'width': '600px', 'height': '2000px',
                    "display": "block",
                    "margin-left": "auto",
                    "margin-right": "auto",
                }
            ),
         ),
    ]
)


@app.callback(
    Output('graph2', 'figure'),
    Input('dropdown2', 'value'),
)
# graph plot and styling
def update_graph(value):
    if value == 'table':
        return {'data': [go.Table(
                header=dict(values=list(df_table.columns),
                            font=dict(color='#ffffff'),
                            fill_color='#a81367',
                            line_color='black',
                            ),
                cells=(dict(values=[df_table.State, df_table.Days],
                            fill_color=[[rowOddColor, rowEvenColor] * 15],
                            line_color='#000000')),
                )
        ],
                'layout': go.Layout(
                    title='Average Number of Days from Passive to Active by State'
                )
        }
    if value == 'timeplots':
        return timeplots
