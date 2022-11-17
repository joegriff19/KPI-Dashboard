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

sep_reasons_22_df = pd.DataFrame(np.random.randint(0, 5, size=(100, 2)), columns=list('AB'))

sep_reasons_22_df.columns = ["Reason", "Count"]

sep_reasons_22_df = sep_reasons_22_df.groupby('Reason').count().reset_index()

# Page 5 Layout and Callbacks
colors = {
    'background': '#111111',
    'text': '#FC1CBF'
}

layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Dropdown(
                    id='dropdown5',
                    multi=True,
                    options=[
                        {'label': "0", 'value': "0"},
                        {'label': "1", 'value': "1"},
                        {'label': "2", 'value': "2"},
                        {'label': "3", 'value': "3"},
                        {'label': "4", 'value': "4"},
                    ],
                    value=[0, 1, 2, 3, 4]
                    ),
                dcc.Graph(
                    id='figure5',
                    figure={},
                    className='shadow-lg',
                ),
            ],
        ),
     ]
)


@app.callback(
    Output('figure5', 'figure'),
    [Input('dropdown5', 'value')]
)
def update_this_graph(val_chosen):
    if len(val_chosen) > 0:
        print(f"value user chose: {val_chosen}")
        dff = sep_reasons_22_df[sep_reasons_22_df["Reason"].isin(val_chosen)]
        fig = px.treemap(dff, path=[px.Constant("Separation Reasons 2022"), 'Reason'], values='Count',
                         color='Count',
                         color_continuous_scale='RdBu',
                         color_continuous_midpoint=np.average(dff['Count'], weights=dff['Count'])
                         )
        fig.update_traces(hovertemplate='Reason=%{label}<br>Count=%{value}<extra></extra>')
        fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
        return fig
