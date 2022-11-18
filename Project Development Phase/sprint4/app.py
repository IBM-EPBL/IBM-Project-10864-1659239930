'''import flask
from flask import request,render_template
from flask_cors import CORS
import joblib

app=flask.Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predictFlight():
    fname = float (request.form['fname'])
    month = float (request.form['month'])
    daymonth = float (request.form['daymonth'])
    dayweek = float (request.form['dayweek'])
    origin = float (request.form['origin'])
    if origin == 0:
        origin_0 = 1
        origin_1 = 0
        origin_2 = 0
        origin_3 = 0
        origin_4 = 0
    if origin == 1:
        origin_0 = 0
        origin_1 = 1
        origin_2 = 0
        origin_3 = 0
        origin_4 = 0
    if origin == 2:
        origin_0 = 0
        origin_1 = 0
        origin_2 = 1
        origin_3 = 0
        origin_4 = 0
    if origin == 3:
        origin_0 = 0
        origin_1 = 0
        origin_2 = 0
        origin_3 = 1
        origin_4 = 0
    if origin == 4:
        origin_0 = 0
        origin_1 = 0
        origin_2 = 0
        origin_3 = 0
        origin_4 = 1
    destination = float (request.form['destination'])
    if destination == 0:
        destination_0 = 1
        destination_1 = 0
        destination_2 = 0
        destination_3 = 0
        destination_4 = 0
    if destination == 1:
        destination_0 = 0
        destination_1 = 1
        destination_2 = 0
        destination_3 = 0
        destination_4 = 0
    if destination == 2:
        destination_0 = 0
        destination_1 = 0
        destination_2 = 1
        destination_3 = 0
        destination_4 = 0
    if destination == 3:
        destination_0 = 0
        destination_1 = 0
        destination_2 = 0
        destination_3 = 1
        destination_4 = 0
    if destination == 4:
        destination_0 = 0
        destination_1 = 0
        destination_2 = 0
        destination_3 = 0
        destination_4 = 1
    sarrivaltime = float (request.form['sarrivaltime'])
    sdeparttime = float (request.form['sdeparttime'])
    adeparttime = float (request.form['adeparttime'])
    delay15 =  adeparttime - sdeparttime
    X = [[fname, month, daymonth, dayweek, sarrivaltime, delay15, origin_0, origin_1, origin_2, origin_3, origin_4, destination_0, destination_1, destination_2, destination_3, destination_4]]
    model = joblib.load('picklee.pkl')
    delay = model.predict(X)[0]
    #return render_template('predict.html',predict=delay)

    msg = ''

    if delay == 0.0:
        msg = 'The flight will be on time'
        return render_template('index.html',predict = msg)
    if delay == 1.0:
        msg = 'The flight will delayed'
        return render_template('index.html',predict = msg)


if __name__ == '__main__':
    app.debug = True
    app.run()'''


'''import flask
from flask import request,render_template
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
import pickle 
import os

app=flask.Flask(__name__)
CORS(app)

@app.route('/')
def sendHomePage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    fname = float (request.form['fname'])
    month = float (request.form['month'])
    daymonth = float (request.form['daymonth'])
    dayweek = float (request.form['dayweek'])
    origin = request.form['origin']
    if origin == "msp":
        origin1,origin2,origin3,origin4,origin5 = 0,0,0,0,1
    if origin == "dtw":
        origin1,origin2,origin3,origin4,origin5 = 1,0,0,0,0
    if origin == "jfk":
        origin1,origin2,origin3,origin4,origin5 = 0,0,1,0,0
    if origin == "sea":
        origin1,origin2,origin3,origin4,origin5 = 0,1,0,0,0
    if origin == "alt":
        origin1,origin2,origin3,origin4,origin5 = 0,0,0,1,0

    destination = request.form['destination']
    if destination == "msp":
        destination1,destination2,destination3,destination4,destination5 = 0,0,0,0,1
    if destination == "dtw":
        destination1,destination2,destination3,destination4,destination5 = 1,0,0,0,0
    if destination == "jfk":
        destination1,destination2,destination3,destination4,destination5 = 0,0,1,0,0
    if destination == "sea":
        destination1,destination2,destination3,destination4,destination5 = 0,1,0,0,0
    if destination == "alt":
        destination1,destination2,destination3,destination4,destination5 = 0,0,0,1,0

    sarrivaltime = float (request.form['sarrivaltime'])
    sdeparttime = float (request.form['sdeparttime'])
    adeparttime = float (request.form['adeparttime'])
    dept15=int(sdeparttime)-int(adeparttime)
    X = [[fname, month, daymonth, dayweek, sarrivaltime, dept15, origin1, origin2, origin3, origin4, origin5, destination1, destination2, destination3, destination4, destination5]]

    model = joblib.load('picklee.pkl')

    y_pred=model.predict(X)

    if y_pred == [0.]:
        ans="The Flight will be on time"
    
    else:
        ans="The Flight will be delayed"
    
    return render_template("index.html",predict = ans)

if __name__ == '__main__':
    app.debug = True
    app.run()'''

'''import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "2AjKeBOMtc_4WMPYUQe2GI-opbRdU3E0q7VEZkBiPUkA"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["FL_NUM", "MONTH", "DAY_OF_MONTH", "DAY_OF_WEEK", "CRS_ARR_TIME", "DEP_DEL15", "ORIGIN_0", "ORIGIN_1", "ORIGIN_2", "ORIGIN_3", "ORIGIN_4", "DEST_0", "DEST_1", "DEST_2", "DEST_3", "DEST_4"]], "values": [[1768, 6, 13, 1, 13, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/70ba7f52-fcd7-4553-bc8b-afbc37d1a0be/predictions?version=2022-11-18', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions = response_scoring.json()
#print(predictions)
#Sprint(predictions['predictions'][0]['values'][0][0])
pred = predictions['predictions'][0]['values'][0][0]
if pred == [0.]:
    print("the flight will be on time")
else :
    print("the flight will be delayed")'''

import flask
from flask import request,render_template
from flask_cors import CORS
import numpy as np
import pandas as pd
import requests

app=flask.Flask(__name__)
CORS(app)


API_KEY = "2AjKeBOMtc_4WMPYUQe2GI-opbRdU3E0q7VEZkBiPUkA"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

@app.route('/')
def sendHomePage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    fname = float (request.form['fname'])
    month = float (request.form['month'])
    daymonth = float (request.form['daymonth'])
    dayweek = float (request.form['dayweek'])
    origin = request.form['origin']
    if origin == "msp":
        origin1,origin2,origin3,origin4,origin5 = 0,0,0,0,1
    if origin == "dtw":
        origin1,origin2,origin3,origin4,origin5 = 1,0,0,0,0
    if origin == "jfk":
        origin1,origin2,origin3,origin4,origin5 = 0,0,1,0,0
    if origin == "sea":
        origin1,origin2,origin3,origin4,origin5 = 0,1,0,0,0
    if origin == "alt":
        origin1,origin2,origin3,origin4,origin5 = 0,0,0,1,0

    destination = request.form['destination']
    if destination == "msp":
        destination1,destination2,destination3,destination4,destination5 = 0,0,0,0,1
    if destination == "dtw":
        destination1,destination2,destination3,destination4,destination5 = 1,0,0,0,0
    if destination == "jfk":
        destination1,destination2,destination3,destination4,destination5 = 0,0,1,0,0
    if destination == "sea":
        destination1,destination2,destination3,destination4,destination5 = 0,1,0,0,0
    if destination == "alt":
        destination1,destination2,destination3,destination4,destination5 = 0,0,0,1,0

    sarrivaltime = float (request.form['sarrivaltime'])
    sdeparttime = float (request.form['sdeparttime'])
    adeparttime = float (request.form['adeparttime'])
    dept15=int(sdeparttime)-int(adeparttime)

    X = [[fname, month, daymonth, dayweek, sarrivaltime, dept15, origin1, origin2, origin3, origin4, origin5, destination1, destination2, destination3, destination4, destination5]]

    payload_scoring = {"input_data": [{"field": [["FL_NUM", "MONTH", "DAY_OF_MONTH", "DAY_OF_WEEK", "CRS_ARR_TIME", "DEP_DEL15", "ORIGIN_0", "ORIGIN_1", "ORIGIN_2", "ORIGIN_3", "ORIGIN_4", "DEST_0", "DEST_1", "DEST_2", "DEST_3", "DEST_4"]], "values": X}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/70ba7f52-fcd7-4553-bc8b-afbc37d1a0be/predictions?version=2022-11-18', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    predictions = response_scoring.json()

    pred = predictions['predictions'][0]['values'][0][0]

    if pred == 0:
        ans = "The flight will be on time"
    else :
        ans = "The flight will be delayed"

    return render_template("index.html",predict = ans)

if __name__ == '__main__':
    app.debug = True
    app.run()