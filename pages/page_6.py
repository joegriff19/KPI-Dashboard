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
warnings.simplefilter(action='ignore', category=UserWarning)
og_member_year_df = pd.DataFrame(np.random.randint(2014, 2023, size=(100, 2)), columns=list('AB'))
og_member_year_df.columns = ['year', 'members']
og_member_year_df = og_member_year_df.groupby('year').count().reset_index()

# Page 1 Layout and Callback
rowEvenColor = 'lightgrey'
rowOddColor = 'white'
colors = {
    'background': '#111111',
    'text': '#FC1CBF'
}
layout = html.Div(
    children=[
        html.Div([
            dcc.Dropdown(
                id='dropdown6',
                options=[{'label': 'Bar', 'value': 'bar'},
                         {'label': 'Scatter', 'value': 'scatter'},
                         {'label': 'Table', 'value': 'table'}],
                value='bar',
            ),
        ],
            style={'width': '30%', "display": "block", "margin-left": "auto", "margin-right": "auto"}
        ),
        html.Br(),
        html.Br(),
        html.Div(
            dcc.Graph(
                id='graph6',
                className='shadow-lg',
                style={
                    'width': '700px', 'height': '500px',
                    "display": "block",
                    "margin-left": "auto",
                    "margin-right": "auto",
                }
            ),
        ),
    ]
)


@app.callback(
    Output('graph6', 'figure'),
    [Input('dropdown6', 'value')]
)
# graph plot and styling
def update_graph(value):
    if value == 'bar':
        x1 = og_member_year_df.year
        y1 = og_member_year_df.members
        col = '#cb177d'
        return {'data': [go.Bar(
            x=x1,
            y=y1,
            marker_color=col),

        ],
            'layout': go.Layout(
                title='Active Members by Original Year',
                plot_bgcolor='white',
                paper_bgcolor='white',
                xaxis_tickangle=-17,
                font=dict(color='black'),
                xaxis=dict(
                    title='Year',
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
                hovermode='closest',
            )
        }
    if value == 'scatter':
        x1 = og_member_year_df.year
        y1 = og_member_year_df.members
        col = '#cb177d'
        return {'data': [go.Scatter(
            x=x1,
            y=y1,
            marker_color=col
            ),
        ],
            'layout': go.Layout(
                title='Active Members by Original Year',
                plot_bgcolor='white',
                paper_bgcolor='white',
                xaxis_tickangle=-17,
                font=dict(color='black'),
                xaxis=dict(
                    # type='line',
                    title='Year',
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
                hovermode='closest',
            )
        }
    if value == 'table':
        return {'data': [go.Table(
            header=dict(values=list(og_member_year_df.columns),
                        font=dict(color='#ffffff'),
                        fill_color='#cb177d',
                        line_color='black',
                        ),
            cells=(dict(values=[og_member_year_df.year, og_member_year_df.members],
                        fill_color = [[rowOddColor, rowEvenColor] * 15],
                        line_color = '#000000',
                        align = ['center'],
                        )),
        )]}
