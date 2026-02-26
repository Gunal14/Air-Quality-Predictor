from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import random
import requests
from pymongo import MongoClient
from model import predict_all
from lstm_model import predict_lstm

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["purecast"]
collection = db["aqi"]

def generate_forecast(base):
    forecast=[]
    for i in range(7):
        forecast.append(int(base+np.sin(i)*10+random.randint(-5,5)))
    return forecast

@app.route("/forecast")
def forecast():
    base=random.randint(50,120)
    return jsonify(generate_forecast(base))

@app.route("/realtime")
def realtime():
    try:
        url="https://api.openaq.org/v2/latest"
        r=requests.get(url).json()
        return jsonify(r)
    except:
        return jsonify({"error":"API error"})

@app.route("/nasa")
def nasa():
    url="https://api.nasa.gov/planetary/earth/assets?lon=77&lat=12&date=2024-01-01&api_key=DEMO_KEY"
    r=requests.get(url).json()
    return jsonify(r)

@app.route("/save")
def save():
    data={"aqi":random.randint(50,150)}
    collection.insert_one(data)
    return jsonify({"status":"saved"})

@app.route("/predict",methods=["POST"])
def predict():

    data=request.json

    co2=float(data["co2"])
    o2=float(data["o2"])
    temp=float(data["temp"])

    aqi,cat,knn=predict_all(co2,o2,temp)

    lstm_pred=predict_lstm()

    return jsonify({
        "Predicted_AQI":float(aqi),
        "AQI_Category":int(cat),
        "Pollution_Level":int(knn),
        "LSTM_Forecast":float(lstm_pred),
        "CO2":co2,
        "O2":o2,
        "Temperature":temp
    })

if __name__=="__main__":
    app.run(debug=True)
    