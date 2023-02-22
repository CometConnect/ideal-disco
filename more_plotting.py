from plotly.express import scatter
from pandas import read_csv

def run():
  df = read_csv('csv/cleaned.csv')
  radius = df['radius'].to_list()
  mass = df['mass'].to_list()
  name = df['name'].to_list()
  color = []
  for m in mass:
    try:
      float_m = float(m)
      color.append(1 if round(float_m) == 1 else 0)
    except:
      color.append(0)
    

  fig = scatter(x=mass, y=radius, color=color, hover_data=[name])
  fig.show()