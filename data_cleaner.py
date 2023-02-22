from pandas import read_csv, DataFrame

def remove_null(df: DataFrame):
  df.isnull().values.any()
def run():
  df = read_csv('csv/data.csv')
  remove_null(df)
  df.drop(columns=['Unnamed: 0', 'luminosity'], inplace=True)
  df.to_csv('csv/cleaned.csv')