import dash_core_components as dcc
import dash_html_components as html


def load_axis_label(dataframe):
    l = list(dataframe)
    return [{'label': l[i], 'value': l[i]} for i in range(len(l))]


def load_graph_page(dataframe):
    axis = load_axis_label(dataframe)
    return html.Div(
        style={
            "height": "100%"
        },
        children=[
            html.H1("Graph"),
            html.Div(
                style={
                    'columnCount': 2,
                    'height': '100'
                },
                children=[
                    html.Label("Select X-axis"),
                    dcc.Dropdown(
                        options=axis,
                        value=axis[0]['value']
                    ),
                    html.Label("Select Y-axis"),
                    dcc.Dropdown(
                        options=axis,
                        value=[axis[i]['value'] for i in range(5)]
                    )
                ]
            ),

        ]
    )
