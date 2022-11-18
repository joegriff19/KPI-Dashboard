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
pd.options.mode.chained_assignment = None

# pull data into df
means_df = pd.DataFrame(np.random.randint(0, 100, size=(25, 10)), columns=list('ABCDEFGHIJ'))

# rename columns and group by state
means_df.columns = ['State', 'Age', 'Group', 'A', 'B',
                         'X', 'Spending', 'Claims', 'C', 'D']
means_df = means_df.groupby('State').mean().reset_index()

means_df['Age'] = means_df['Age'].map('{:.0f}'.format)
means_df['X'] = means_df['X'].map('{:.0f}'.format)
means_df['Spending'] = means_df['Spending'].map('${:,.0f}'.format)
means_df['Claims'] = means_df['Claims'].map('{:.0f}'.format)
means_df['A'] = means_df['A'].map('{:.0f}%'.format)
means_df['B'] = means_df['B'].map('{:.0f}%'.format)
means_df['C'] = means_df['C'].map('{:.0f}%'.format)
means_df['D'] = means_df['D'].map('{:.0f}%'.format)

# create df purely for column names (no data in df)
cols_df = pd.DataFrame(columns=['State', 'Mean Age', 'Mean Number of X', 'Spending',
                                'Mean Number of Y',
                                'Members with A', 'Members with B', 'Members with C', 'Members with D',
                                ])
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

# format table
summ_table = go.Figure(data=[go.Table(
                # use cols_df for column names
                header=dict(values=list(cols_df.columns),
                            font=dict(color='#ffffff'),
                            fill_color='#a81367',
                            line_color='black',
                            align=['center'],
                            ),
                # bring in all the other data columns
                cells=(dict(values=[means_df.State, means_df.Age, means_df.Claims, means_df.Spending,
                                    means_df.X,
                                    means_df.A, means_df.B, means_df.C, means_df.D
                                    ],
                            fill_color=[[rowOddColor, rowEvenColor] * 15],
                            line_color='#000000',
                            align=['center'],
                            )),
            )],
)
summ_table.update_layout(width=1000, height=1000, title_text="Summary by State")

# Page 6 Layout and Callbacks #
colors = {
    'background': '#111111',
    'text': '#FC1CBF'
}

layout = html.Div(
    dcc.Graph(figure=summ_table),
    style={'textAlign': 'center'},
)
