from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

API_KEY = os.getenv('KEY')
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/convert", methods= ["POST"])
def convert():
    #data = requests.get_json()
    data = request.get_json()
    amount = float(data["amount"])
    from_currency = data["from"]
    to_currency = data["to"]

    response = requests.get(BASE_URL + from_currency)
    result = response.json()

    if result["result"] == "success":
        rate = result["conversion_rates"][to_currency] 
        converted = round(amount * rate, 2)      
        return jsonify({"converted": converted})
    
    else: 
        return jsonify({"error":"Conversion Fallida"}), 500
    

if __name__ == "__main__":
    app.run(debug=True)