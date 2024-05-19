from flask import Flask, request, jsonify, send_from_directory
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def convert_currency(api_key, from_currency, to_currency, amount):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}'

    try:
        response = requests.get(url)
        response.raise_for_status()
       
        data = response.json()
        if data['result'] == 'success':
            exchange_rate = data['conversion_rate']
            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()
    from_currency = data.get('from_currency')
    to_currency = data.get('to_currency')  
    amount = float(data.get('amount'))  # Convert amount to float
    
    api_key = '018a4fedccf6b49d868eb530'
    
    # Call the convert_currency function to get the converted amount
    converted_amount = convert_currency(api_key, from_currency, to_currency, amount)
    
    if converted_amount is not None:
        print(f"Converted amount: {converted_amount}")  # Print the converted amount to the terminal
    
    return jsonify({'amount': converted_amount})

if __name__ == "__main__":
    app.run(port=3125, debug=True)
