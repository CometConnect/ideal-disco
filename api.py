from flask import Flask
from pandas import read_csv

app = Flask(__name__)
data = read_csv("csv/gravity.csv")

@app.get("/")
def index():
  to_send = []
  i = 1
  while True:
    res = get_data(i)
    if res == "":
      break
    to_send.append(res)
    i += 1
  return to_send


@app.route("/get/<int:i>")
def get_data(i):
  try:
    to_send = {}
    columns = data.columns[1:]
    response = data.iloc[i].to_json(orient='records')[1:-1].split(",")[1:]
    for j, item in enumerate(response):
      to_send.update({ columns[j]: item.replace("\"", "").replace("\"", "") })
    return to_send
  except:
    return ""