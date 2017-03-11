import pandas as pd
import plotly
from plotly.graph_objs import *
from plotly.offline import iplot
path = "B:\hadoop_py\work\External_data\P.csv"
df = pd.read_csv(path)
df.head()
plotly.offline.plot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})