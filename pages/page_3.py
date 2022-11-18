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
pd.options.mode.chained_assignment = None

days_df = pd.DataFrame(np.random.randint(0, 25, size=(100, 2)), columns=list('AB'))

# rename columns
days_df.columns = ['State', 'Days']

# get averages for each state
ave_days_df = days_df.groupby('State').mean()
ave_days_df = ave_days_df.reset_index()
ave_days_df.columns = ['State', 'Days']

# get ave days for all states and append
ave_days = ave_days_df.Days.mean()
app_df = pd.DataFrame([['<b>ALL<br>STATES</b>', ave_days]], columns=['State', 'Days'])
ave_days_df = ave_days_df.append(app_df, ignore_index=True)
ave_days_df = ave_days_df.reset_index()
table_df = ave_days_df[['State', 'Days']].copy()
table_df['Days'] = table_df['Days'].map('{:.0f}'.format)

# Page 2 Layout and Callback
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

colors = {
    'background': '#111111',
    'text': '#FC1CBF'
}

# graph plot and styling
ave_table = go.Figure(data=[go.Table(
                header=dict(values=list(table_df.columns),
                            font=dict(color='#ffffff'),
                            fill_color='#a81367',
                            line_color='black',
                            ),
                cells=(dict(values=[table_df.State, table_df.Days],
                            fill_color=[[rowOddColor, rowEvenColor] * 15],
                            line_color='#000000')),
            )],
)
ave_table.update_layout(width=600, height=800, title_text="Average Number of Days from A to B by State")

layout = html.Div(
    dcc.Graph(figure=ave_table),
    style={'textAlign': 'center',
           "margin-left": "auto",
           "margin-right": "auto"
           }
)
