import numpy as np

data = np.loadtxt("data/soil_average.csv", delimiter=",")
data2 = np.swapaxes(data,0,1)

import plotly.express as px

fig=px.line(data2)
fig.show()