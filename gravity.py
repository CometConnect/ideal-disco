from pandas import read_csv

def sqr(x):
  return x*x

def run():
  gravity = []
  G = 6.674 * pow(10, -11)

  df = read_csv('cleaned.csv')
  for cell in df.iloc:
    try:
      if cell.notnull()['mass'] and cell.notnull()['radius']:
        mass = float(cell['mass']) * 2 * pow(10, 30)
        radius = float(cell['radius']) * 7 * pow(10, 8)
        g = G * mass/sqr(radius)
        gravity.append(g)
        continue
      gravity.append(-1)
    except:
      gravity.append(-1)

  df.drop(columns=['Unnamed: 0'], inplace=True)
  df['gravity'] = gravity
  df.to_csv("gravity.csv")