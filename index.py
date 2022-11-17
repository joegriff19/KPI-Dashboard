# Import Packages and other files for app
from app import app, server #NEED THE IMPORT SERVER FOR RENDER
from pages import page_1
from pages import page_2
from pages import page_3
from pages import page_4
from pages import page_5
from pages import page_6
from pages import page_7
from dash import dcc, html
import base64
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
import plotly.express as px
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from datetime import date
today = date.today()

# styling the sidebar
SIDEBAR_STYLE = {
   "position": "fixed",
   "top": 0,
   "left": 0,
   "bottom": 0,
   "width": "20rem",
   "padding": "2rem 1rem",
   "background-color": "#ffffff",
   "overflow": "scroll"
}

# padding for the page content
CONTENT_STYLE = {
   "margin-left": "24rem",
   "margin-right": "2rem",
   "padding": "2rem 1rem",
}

# Index Page Layout
colors = {
    'background': '#ffffff',
    'text': '#cb177d'  # pink color
}

# labels and links for sidebar
sidebar = html.Div(
   [
       html.Div(children="griffin", style={"fontSize": "82px", 'textAlign': 'center',
                                           'color': colors['text'], 'background': colors['background']}),
       html.Hr(),
       dbc.Nav(
           [
               # this determines order of pages in sidebar
               dbc.NavLink("🏠 Home ", href="/", active="exact"),
               dbc.NavLink("ℹ️ Member Overview", href="/page-1", active="exact"),
               dbc.NavLink("📈 Passive to Active Analysis", href="/page-2", active="exact"),
               dbc.NavLink("📊 Renewed vs. New Members", href="/page-4", active="exact"),
               dbc.NavLink("📝 Separation Reasons", href="/page-5", active="exact"),
               dbc.NavLink("🗓️ Original Member Year", href="/page-6", active="exact"),
               dbc.NavLink("👥 Metal Level Distribution", href="/page-7", active="exact")
           ],
           vertical=True,
           pills=True,
       ),
   ],
   style=SIDEBAR_STYLE,
   className='divBorder'
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

# define sidebar layout
app.layout = html.Div([
   dcc.Location(id="url"),
   sidebar,
   content
])

# index page layout
index_layout = html.Div(
    children=[
            html.Header(
                children=[
                    html.Br(),
                    html.Div(children="💻", style={"fontSize": "100px"}),
                    html.Div(children="Member Insights Dashboard", style={"fontSize": "42px"}),
                    html.Br(),
                ],
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'background': colors['background']
                }
            ),
            html.Div(children='NOTE: ALL DATA HERE IS COMPLETELY RANDOMIZED', style={'textAlign': 'center'}),
            html.Div(children='Hello! This is the Member Insights Dashboard.', style={'textAlign': 'center'}),
            html.Br(),
            html.Div(children='This dashboard was built to better visualize performance of Member Insights segmentation'
                              ' This will allow us to drive strategic member'
                              ' engagement for OE23 Retention.', style={'textAlign': 'center'}),
            html.Br(),
            html.Div(children='The content of this dashboard comes mainly from the following tables: ______', style={'textAlign': 'center'}),
            html.Br(),
            html.Div(children='Data Sources used to create the figures and tables: ______', style={'textAlign': 'center'}),
            html.Br(),
            html.Div(children='Defining terms and calculations: ______', style={'textAlign': 'center'}),
            html.Br(),
            html.Div(children=f'This dashboard was last updated {today} CST.', style={'textAlign': 'center'}),
    ]
)


# app callback
@app.callback(
    Output('page-content', 'children',),
    [Input('url', 'pathname',)]
)
def render_page_content(pathname):
    if pathname == '/':
        return index_layout
    elif pathname == '/page-1':
        return page_1.layout
    elif pathname == '/page-2':
        return page_2.layout
    elif pathname == '/page-3':
        return page_3.layout
    elif pathname == '/page-4':
        return page_4.layout
    elif pathname == '/page-5':
        return page_5.layout
    elif pathname == '/page-6':
        return page_6.layout
    elif pathname == '/page-7':
        return page_7.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
       [
           html.H1("404: Not found", className="text-danger"),
           html.Hr(),
           html.P(f"The pathname {pathname} was not recognised..."),
       ]
    )
