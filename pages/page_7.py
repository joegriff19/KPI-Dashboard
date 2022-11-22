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

metal_levels_22_df = pd.DataFrame(np.random.randint(0, 3, size=(100, 2)), columns=list('AB'))
metal_levels_22_df.columns = ['Metal_Level', 'Members']
metal_levels_22_df = metal_levels_22_df.groupby('Metal_Level').count().reset_index()

# Page 3 Layout and Callbacks
colors = {
    'background': '#111111',
    'text': '#FC1CBF'
}

layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Dropdown(
                    id='dropdown7',
                    multi=True,
                    options=[{'label': x, 'value': x} for x in metal_levels_22_df.Metal_Level],
                    value=[0, 1, 2, 3]
                    ),
                dcc.Graph(
                    id='figure7',
                    figure={},
                    className='shadow-lg',
                ),
            ],
        ),
    ]
)


@app.callback(
    Output('figure7', 'figure'),
    [Input('dropdown7', 'value')]
)
def update_my_graph(val_chosen):
    if len(val_chosen) > 0:
        print(f"value user chose: {val_chosen}")
        dff = metal_levels_22_df[metal_levels_22_df["Metal_Level"].isin(val_chosen)]
        fig = px.pie(dff, values="Members", names="Metal_Level", title="Metal Level Distribution 2022")
        fig.update_traces(textinfo="percent").update_layout(title_x=0.5)
        return fig
