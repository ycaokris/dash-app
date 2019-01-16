import dash_html_components as html

from style import center_style


def new_line(text):
    return html.P(text, style=center_style)


def load_home_page():
    return html.Div(
        children=[
            # todo: change to table for better layout
            html.H3('Welcome to dash sample app', style=center_style),
            new_line('This is a dash sample app based on motor trend car design and performance.'),
            new_line('Click on header to navigate to desired page'),
            new_line('Graph is the main function of this app, it plots features against car model'),
            new_line('Data page displays original table we use for graph, a brief description is included.')
        ],
        style={
            'margin': '0 auto'
        }
    )
