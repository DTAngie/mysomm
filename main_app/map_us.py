import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd
# from .models import Test_Data 
# ANGIE -- you may need to import data here...if render map can't accept args

def render_map(query):
    df=pd.DataFrame(query)
    print(df)
    df.head()
    df['text'] = df['name'] + '<br>Population ' + (df['count']/1e6).astype(str)+' million'
    limits = [(0,2),(3,10),(11,20),(21,50),(50,3000)]
    colors = ["royalblue","crimson","lightseagreen","orange","lightgrey"]
    cities = []
    scale = 5000

    fig = go.Figure()

    for i in range(len(limits)):
        lim = limits[i]
        df_sub = df[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode = 'USA-states',
            lon = df_sub['lon'],
            lat = df_sub['lat'],
            text = df_sub['text'],
            marker = dict(
                size = df_sub['count']/scale,
                color = colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode = 'area'
            ),
            name = '{0} - {1}'.format(lim[0],lim[1])))

    fig.update_layout(
            height=500,
            margin= {"r":0,"t":0,"l":0,"b":0},
            title_text = '2014 US city populations<br>(Click legend to toggle traces)',
            showlegend = False,
            geo = dict(
                scope = 'usa',
                landcolor = 'rgb(217, 217, 217)',
            )
        )
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div