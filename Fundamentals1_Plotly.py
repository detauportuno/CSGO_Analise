#Fundamentals 1: The Figure Data Structure
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("IRIS.csv")

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                  facet_col="species", title="Using The add_trace() method With A Plotly Express Figure")
#OBS: se eu quiser que todas as infos estejam contidas no mesmo grafico, basta tirar o facet_col
'''fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines",
        line=go.scatter.Line(color="black"),
        showlegend=False)
)'''

fig = px.bar(df, x="sepal_width", y="sepal_length", color="species",
                  facet_col="species", title="Using The add_trace() method With A Plotly Express Figure" )
fig.show()


