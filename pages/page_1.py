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

# # group different variables by state
# metal_df = pcts_df.groupby(['State', 'Metal_Level']).size().unstack(fill_value=0).reset_index()
# csr_df = pcts_df.groupby(['State', 'CSR']).size().unstack(fill_value=0).reset_index()
# aptc_df = pcts_df.groupby(['State', 'APTC']).size().unstack(fill_value=0).reset_index()
# mhp_df = pcts_df.groupby(['State', 'MHP']).size().unstack(fill_value=0).reset_index()
# autopay_df = pcts_df.groupby(['State', 'Autopay']).size().unstack(fill_value=0).reset_index()
#
# # create new columns with percents
# metal_df['All_bronze'] = metal_df['BRONZE'] + metal_df['EXPANDED BRO']
# metal_df['Bronze_Pct'] = 100 * metal_df['All_bronze'] / (metal_df['All_bronze'] + metal_df['SILVER'] + metal_df['GOLD'])
# metal_df['Silver_Pct'] = 100 * metal_df['SILVER'] / (metal_df['All_bronze'] + metal_df['SILVER'] + metal_df['GOLD'])
# metal_df['Gold_Pct'] = 100 * metal_df['GOLD'] / (metal_df['All_bronze'] + metal_df['SILVER'] + metal_df['GOLD'])
# csr_df['Yes_Pct'] = 100 * csr_df['Yes'] / (csr_df['Yes'] + csr_df['No'])
# aptc_df['Yes_Pct'] = 100 * aptc_df['Yes'] / (aptc_df['Yes'] + aptc_df['No'])
# mhp_df['Yes_Pct'] = 100 * mhp_df['Y'] / (mhp_df['Y'] + mhp_df['N'])
# autopay_df['Yes_Pct'] = 100 * autopay_df['Y'] / (autopay_df['Y'] + autopay_df['N'])
# autopay_df['Num_Members'] = autopay_df['Y'] + autopay_df['N']
#
# calculate grand total of all Ambetter members
# member_total = means_df.Num_Members.sum()

# # add row with averages to dfs in table
# means_df.loc['<b>ALL<br>STATES</b>'] = means_df.mean()
# csr_df.loc['<b>ALL<br>STATES</b>'] = csr_df.mean()
# aptc_df.loc['<b>ALL<br>STATES</b>'] = aptc_df.mean()
# mhp_df.loc['<b>ALL<br>STATES</b>'] = mhp_df.mean()
# autopay_df.loc['<b>ALL<br>STATES</b>'] = autopay_df.mean()
# metal_df.loc['<b>ALL<br>STATES</b>'] = metal_df.mean()
#
# # rename state as 'all states' in each df in table
# means_df.State.loc['<b>ALL<br>STATES</b>'] = '<b>ALL<br>STATES</b>'
# csr_df.State.loc['<b>ALL<br>STATES</b>'] = '<b>ALL<br>STATES</b>'
# aptc_df.State.loc['<b>ALL<br>STATES</b>'] = '<b>ALL<br>STATES</b>'
# mhp_df.State.loc['<b>ALL<br>STATES</b>'] = '<b>ALL<br>STATES</b>'
# autopay_df.State.loc['<b>ALL<br>STATES</b>'] = '<b>ALL<br>STATES</b>'
# metal_df.State.loc['<b>ALL<br>STATES</b>'] = '<b>ALL<br>STATES</b>'
#
# # replace mean total member number with actual total member number
# autopay_df.Num_Members.loc['<b>ALL<br>STATES</b>'] = member_total

# format numbers in table
# means_df['Yes_Pct'] = means_df['Yes_Pct'].map('{:,.0f}%'.format)
# means_df['Yes_Pct'] = means_df['Yes_Pct'].map('{:,.0f}%'.format)
# means_df['Yes_Pct'] = means_df['Yes_Pct'].map('{:,.0f}%'.format)
# means_df['Yes_Pct'] = means_df['Yes_Pct'].map('{:,.0f}%'.format)
# means_df['Bronze_Pct'] = means_df['Bronze_Pct'].map('{:,.0f}%'.format)
# means_df['Silver_Pct'] = means_df['Silver_Pct'].map('{:,.0f}%'.format)
# means_df['Gold_Pct'] = means_df['Gold_Pct'].map('{:,.0f}%'.format)
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
