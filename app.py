from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import joblib
import re
import numpy as np

from datetime import datetime

app = Flask(__name__)
run_with_ngrok(app)

model = joblib.load('files/model1.pkl')
mappings = joblib.load('files/mappings1.pkl')

# @app.route('/')
# def home():
#   return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def api():
  if request.method == 'GET':
    return render_template('api.html')
  else:
    row = []
    airline = request.form['airline']
    source = request.form['source']
    destination = request.form['destination']
    dep_date= request.form['dep_date']
    dep_time = request.form['dep_time']
    # stops = request.form['stops']

    # convert to form understandable by ML model
    airline_mappings = mappings['airline']
    source_mappings = mappings['source']
    destination_mappings = mappings['destination']

    airline = airline_mappings[airline]
    source = int(source_mappings[source])
    destination = destination_mappings[destination]

    dep_hour = int(re.findall(r'(\d+):\d', dep_time)[0])
    dep_min = int(re.findall(r'\d+:(\d+)', dep_time)[0])

    dep_date = datetime.strptime(dep_date,'%Y-%m-%d')
    dep_month = dep_date.month
    dep_day = dep_date.day
    dep_dayofweek = dep_date.weekday()
    dep_weekofyear = dep_date.isocalendar()[1]

    texts = []
    for stops in [0,1,2]:
      row = [airline, source, destination, stops, dep_month, dep_day, dep_dayofweek, dep_weekofyear, dep_hour, dep_min]
      # names = ['airline', 'source', 'destination', 'stops', 'dep_month', 'dep_day', 'dep_dayofweek', 'dep_weekofyear', 'dep_hour', 'dep_min']
      price = int(model.predict(np.array(row).reshape(1, -1))[0])
      # text = f"flight fare with {stops} stops is {price}"
      text = (stops, price)
      texts.append(text)

    # text = f'''
    # airline : {airline} | source : {source} | destination : {destination} | stops : {stops}\n
    # dep date : {dep_date} | dep day : {dep_day} | dep month : {dep_month} | dep dayofweek : {dep_dayofweek} \n
    # departure time : {dep_time} | departure hour {dep_hour} | departure min : {dep_min}
    # '''

    return render_template('api.html', print_this = texts)

if __name__ == '__main__':
  app.run()