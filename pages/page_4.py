import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dash
from dash import dcc, html
from dash.dependencies import Output, Input, State
import plotly.graph_objects as go
import plotly.express as px
import dash_bootstrap_components as dbc
from app import app
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

new_renew_22_df = pd.DataFrame(np.random.randint(0, 2, size=(100, 2)), columns=list('AB'))
new_renew_22_df.columns = ['category', 'count']
new_renew_22_df = new_renew_22_df.groupby('category').count().reset_index()

col_list = new_renew_22_df["count"].values.tolist()

# Page 4 Layout and Callbacks
colors = {
    'background': '#111111',
    'text': '#FC1CBF'
}

layout = html.Div(
    children=[
        html.Div([
            dcc.Dropdown(
                id='dropdown4',
                options=[{'label': 'bar', 'value': 'bar'},
                         {'label': 'table', 'value': 'table'}],
                value='bar',
            ),
        ],
            style={'width': '30%', "display": "block", "margin-left": "auto", "margin-right": "auto"}
        ),
        html.Br(),
        #html.Div(id='tablecontainer4'),
        html.Br(),
        html.Div(
            dcc.Graph(
                id='graph4',
                className='shadow-lg',
                style={
                    'width': '600px', 'height': '450px',
                    "display": "block",
                    "margin-left": "auto",
                    "margin-right": "auto",
                }
            )
        )
    ]
)


@app.callback(
    Output('graph4', 'figure'),
    [Input('dropdown4', 'value')]
)
def update_the_graph(value):
    if value == 'bar':
        x1 = new_renew_22_df.category
        y1 = col_list
        col = '#cb177d'
        return {'data': [go.Bar(
            x=x1,
            y=y1,
            marker_color=col),
        ],
            'layout': go.Layout(
                title='Renewed vs New Members OE 2022',
                plot_bgcolor='white',
                paper_bgcolor='white',
                xaxis_tickangle=-17,
                font=dict(color='black'),
                xaxis=dict(
                    title=' ',
                    showgrid=True,
                    showline=True,
                    color='black',
                    linewidth=1,
                ),
                yaxis=dict(
                    title='Members',
                    showgrid=True,
                    showline=True,
                    gridcolor='#bdbdbd',
                    color='black',
                    linewidth=1
                ),
                margin={'l': 60, 'b': 40, 't': 30, 'r': 60},
                # legend={'x': 0.5, 'y': 1},
                hovermode='closest',

            )
        }
    if value == 'table':
        return {'data': [go.Table(
            header=dict(values = list (new_renew_22_df.columns),
                        font=dict(color='#ffffff'),
                        fill_color='#a81367',
                        line_color='black',
                        ),
            cells=(dict(values=[new_renew_22_df.category, col_list],
                        fill_color='#ffffff',
                        line_color='#000000')),
        )]}
