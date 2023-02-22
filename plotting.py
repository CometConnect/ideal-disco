from plotly.express import scatter
from pandas import read_csv, DataFrame

def run():
  df = read_csv('gravity.csv')
  
  print("a> mass and radius")
  print("b> mass and gravity")
  print("c> radius and gravity")
  mode = input('> ')
  if mode == "a":
    set_axis(df, 'mass', 'radius')
  elif mode == "b":
    set_axis(df, 'mass', 'gravity')
  elif mode == "c":
    set_axis(df, 'radius', 'gravity')
  else:
    print("Invalid Input")

def set_axis(df: DataFrame, x_input: str, y_input: str):
  fig = scatter(x=df[x_input].to_list(), y=df[y_input].to_list())
  fig.show()