import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label("a"),
    dcc.Input(id='my-id1', value='1', type='text'),
    html.Label("b"),
    dcc.Input(id='my-id2', value='2', type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [
        Input(component_id='my-id1', component_property='value'),
        Input(component_id='my-id2', component_property='value')
    ]
)
def update_output_div(input_value1, input_value2):
    return 'a + b = {}'.format(int(input_value1) + int(input_value2))


if __name__ == '__main__':
    app.run_server(debug=True)
