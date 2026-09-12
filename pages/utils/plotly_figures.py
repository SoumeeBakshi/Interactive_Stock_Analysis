import plotly.graph_objects as go
import pandas as pd
import pandas_ta as pta
import datetime
from dateutil import relativedelta


def table(dataframe):
    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=[
                        '<b>' + str(i) + '</b>'
                        for i in dataframe.columns
                    ],
                    line_color='black',
                    fill_color='#0077ff',
                    align='center',
                    font=dict(color='white', size=15),
                    height=35
                ),
                cells=dict(
                    values=[
                        dataframe[col].tolist()
                        for col in dataframe.columns
                    ],
                    fill_color=[
                        [rowOddColor, rowEvenColor]
                        * (len(dataframe) // 2 + 1)
                    ],
                    align='left',
                    line_color='black',
                    font=dict(color='black', size=15)
                )
            )
        ]
    )

    fig.update_layout(
        height=400,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return fig
         
    


 






 

    






