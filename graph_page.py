import dash
import dash_core_components as dcc
import dash_html_components as html

from base import app, df


def load_axis_label(dataframe):
    l = list(dataframe)
    return [{'label': l[i], 'value': l[i]} for i in range(len(l))][1:]


def load_graph_page(dataframe):
    axis = load_axis_label(dataframe)
    return html.Div(
        style={
            'height': '100%'
        },
        children=[
            html.H1('Graph'),
            html.Div(
                style={
                    'height': '100%',
                    'width': '100%',
                    'display': 'inline-block',
                },
                children=[
                    html.Div(
                        style={
                            'display': 'inline-block',
                            'verticalAlign': 'top',
                            'width': '20%',
                            'height': '100%'
                        },
                        children=[
                            html.Label('Select Y-axis'),
                            dcc.Dropdown(
                                id='y_axis_dd',
                                options=axis,
                                value=[axis[i]['value'] for i in range(5)],
                                multi=True
                            )
                        ]
                    ),
                    dcc.Graph(
                        style={
                            'display': 'inline-block',
                            'verticalAlign': 'top',
                            'width': '70%',
                            'height': '100%',
                        },
                        id='graph_div'
                    )
                ]
            ),
        ]
    )


def build_axis(col):
    return df[col].tolist()


def build_pairs(x_axis, y_axis):
    ret = []
    for i in range(len(y_axis)):
        ret.append({
            'x': x_axis,
            'y': df[y_axis[i]].tolist(),
            'type': 'bar',
            'name': y_axis[i]
        })
    return ret


@app.callback(dash.dependencies.Output('graph_div', 'figure'),
              [
                  dash.dependencies.Input('y_axis_dd', 'value')
              ])
def build_graph(y_axis):
    x_axis = build_axis('model')
    return {'data': build_pairs(x_axis, y_axis)}
