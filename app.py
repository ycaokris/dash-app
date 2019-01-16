import dash

from base import app, df
from data_page import load_data_page
from graph_page import load_graph_page
from home_page import load_home_page
from style import *


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/graph':
        return load_graph_page(df)
    elif pathname == '/data':
        return load_data_page(df, color)
    else:
        return load_home_page()


if __name__ == '__main__':
    app.run_server(debug=True)
