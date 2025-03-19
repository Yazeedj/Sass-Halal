from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Halal SaaS App on AWS!"

@app.route("/prayer-times/<city>")
def get_prayer_times(city):
    # Replace with your preferred Islamic API endpoint
    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country=Saudi%20Arabia&method=2"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
