import dash
import dash_bootstrap_components as dbc
# Dash instance
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        suppress_callback_exceptions=True
        )
server = app.server #NEED THIS FOR RENDER
