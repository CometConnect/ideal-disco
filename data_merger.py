from pandas import read_csv, DataFrame, concat


def run():
    table2: DataFrame = read_csv("csv/table2.csv")
    table2.drop(columns=['Unnamed: 0'], inplace=True)

    # convert to solar radii
    table2['radius'] = table2['radius'].apply(lambda x: x * 0.102763)
    # convert to solar mass
    table2['mass'] = table2['mass'].apply(lambda x: x * 0.00095458)

    table1 = read_csv("csv/table1.csv")
    table1.drop(columns=['Unnamed: 0'], inplace=True)
    concat([
        table1,
        table2
    ]).to_csv("csv/data.csv")
