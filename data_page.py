import dash_html_components as html


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


def load_data_page(df, color_dict):
    return html.Div(
        children=[
            generate_table(df, color=color_dict)
        ]
    )
