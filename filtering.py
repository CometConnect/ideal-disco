from pandas import read_csv, DataFrame, concat

def close_check(df: DataFrame) -> DataFrame:
  output = DataFrame()

  for cell in df.iloc:
    dist = cell['distance']
    try:
      dist_float = float(dist)
      if dist_float < 100:
        output = concat([output, cell.to_frame().T], ignore_index=True)

    except:
      continue

  return output

def gravity_check(df: DataFrame) -> DataFrame:
  output = DataFrame()

  for cell in df.iloc:
    gravity = cell['gravity']
    try:
      gravity_float = float(gravity)
      if gravity_float < 0:
        # unknown gravity
        continue
      if gravity_float <= 150 and gravity_float >= 300:
        output = concat([output, cell.to_frame().T], ignore_index=True)

    except:
      continue

  return output

def run():
  close = close_check(read_csv('csv/gravity.csv'))
  gravity = gravity_check(close)

  gravity.drop(columns=['Unnamed: 0'], inplace=True)
  gravity.to_csv("csv/filtered_stars.csv")