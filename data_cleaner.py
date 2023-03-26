from pandas import read_csv, DataFrame

def run():
  df = read_csv('csv/data.csv')
  df.drop(columns=['Unnamed: 0', 'luminosity'], inplace=True)
  df.to_csv('csv/cleaned.csv')