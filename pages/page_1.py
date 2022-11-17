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
means_df.columns = ['State', 'Age', 'Metal_Level', 'CSR', 'APTC',
                         'Med_Claims', 'Med_Spend', 'RX_Claims', 'MHP', 'Autopay']
means_df = means_df.groupby('State').mean().reset_index()

means_df['Age'] = means_df['Age'].map('{:.0f}'.format)
means_df['Med_Claims'] = means_df['Med_Claims'].map('{:.0f}'.format)
means_df['Med_Spend'] = means_df['Med_Spend'].map('${:,.0f}'.format)
means_df['RX_Claims'] = means_df['RX_Claims'].map('{:.0f}'.format)
means_df['CSR'] = means_df['CSR'].map('{:.0f}%'.format)
means_df['APTC'] = means_df['APTC'].map('{:.0f}%'.format)
means_df['Autopay'] = means_df['Autopay'].map('{:.0f}%'.format)
means_df['MHP'] = means_df['MHP'].map('{:.0f}%'.format)
# means_df['Num_Members'] = means_df['Num_Members'].map('{:,.0f}'.format)

# create df purely for column names (no data in df)
cols_df = pd.DataFrame(columns=['State', 'Mean Age', 'Mean Number of Medical Claims', 'Mean Medical Spending',
                                'Mean Number of RX Claims',
                                'Members with CSR', 'Members with APTC', 'Members with MHP', 'Members with Autopay',
                                # 'Bronze Members', 'Silver Members', 'Gold Members',
                                # 'Total Number of Members'
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
                cells=(dict(values=[means_df.State, means_df.Age, means_df.Med_Claims, means_df.Med_Spend,
                                    means_df.RX_Claims,
                                    means_df.CSR, means_df.APTC, means_df.MHP, means_df.Autopay
                                    # csr_df.Yes_Pct, aptc_df.Yes_Pct, mhp_df.Yes_Pct,
                                    # autopay_df.Yes_Pct, metal_df.Bronze_Pct, metal_df.Silver_Pct, metal_df.Gold_Pct,
                                    # autopay_df.Num_Members
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
