import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

data = pd.read_csv("data/phemex.csv")
data['Funding Rate'] = data['Funding Rate'].apply(lambda x: float(x.strip('%')) / 100)
data['Time'] = pd.to_datetime(data['Time'])
source = ColumnDataSource(data)

p = figure(title="Funding Rate vsTime Date",
           x_axis_label='Time',
           y_axis_label='Funding Rate',
           x_axis_type='datetime',
           width=1600,
           height=400
           )

p.line(x='Time', y='Funding Rate', source=source, line_width=2)
show(p)
