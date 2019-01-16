import dash_html_components as html

from style import center_style


def round_wt(dataframe, i, col):
    if col == 'wt':
        return html.Td(round(dataframe.iloc[i][col], 3))
    else:
        return html.Td(dataframe.iloc[i][col])


def generate_table(dataframe, max_rows=None, color=None):
    if color is None:
        color = {'color': '#7FDB00'}
    if max_rows is None:
        max_rows = len(dataframe)

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            round_wt(dataframe, i, col) for col in dataframe.columns
        ]) for i in range(max_rows)],
        style={
            'margin': '0 auto',
            'color': color['table']
        }
    )


def new_line(text):
    return html.P(text, style=center_style)


def load_data_page(df, color_dict):
    return html.Div(
        children=[
            html.H3('Data description', style=center_style),
            new_line('The data was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption '
                     'and 10 aspects of automobile design and performance for 32 automobiles (1973–74 models).'),
            new_line('Data source: https://gist.github.com/seankross/a412dfbd88b3db70b74b#file-mtcars-csv'),
            generate_table(df, color=color_dict)
        ]
    )
