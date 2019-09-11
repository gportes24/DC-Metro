import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'the Empire State'
myheading1 = 'Step Back! The doors are about to close!'
myheading2 = 'Always a good option'
image1 = 'new-york-flag1.jpg'
image2 = 'nyc_subway.jpg'
textbody = "24 hour service to get you around the city that never sleeps!"
sourceurl = 'https://www.wmata.com/about/back2good/index.cfm'
githublink = 'https://github.com/gportes24/DC-Metro'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.H2(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '50%', 'height': 'auto'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '80%', 'height': 'auto'}),
        ],className='three columns'),
        html.Div([
            html.Div(textbody, style={
                'padding': '16px',
                'font-size': '30px',
                'height': '220px',
                'border': 'thin blue solid',
                'color': 'rgb(60, 80, 182)',
                'backgroundColor': 'rgb(57, 83, 107)',
                'textAlign': 'right',
                }),
        ],className='six columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
