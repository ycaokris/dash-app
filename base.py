import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from style import color

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv('https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/'
                 'raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv')

app.layout = html.Div(
    style={
        'backgroundColor': color['titleBackground'],
        'height': '100vh'
    },
    children=[
        # represents the URL bar, doesn't render anything
        dcc.Location(id='url', refresh=False),
        html.Header(
            style={
                'columnCount': 3,
            },
            children=[
                html.Div([dcc.Link('Home', href='/')], style={'textAlign': 'center'}),
                html.Div(dcc.Link('Graph', href='/graph'), style={'textAlign': 'center'}),
                html.Div(dcc.Link('Data', href='/data'), style={'textAlign': 'center'})
            ]),
        html.H1(children="Motor Trend", style={
            'textAlign': 'center',
            'color': color['title']
        }),
        html.Div(
            id='page-content',
            style={
                "height": "100%"
            }
        ),
        html.Div(

        )
    ])

app.config['suppress_callback_exceptions'] = True
