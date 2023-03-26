from pandas import read_csv
from matplotlib.pyplot import bar, title, show

def run():
  df = read_csv('csv/filtered_stars.csv')

  name = []
  mass = []
  radius = []
  distance = []
  gravity = []

  for cell in df.iloc:
    name.append(cell['name'])
    mass.append(cell['mass'])
    radius.append(cell['radius'])
    distance.append(cell['distance'])
    gravity.append(cell['gravity'])
  

  def display(x, title_to_show: str):
    title(title_to_show)
    bar(x=name, height=x)
    show()

  display(mass, "Mass")
  display(radius, "Radius")
  display(distance, "Distance")
  display(gravity, "Gravity")