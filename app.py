# app.py
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_BASE = "https://api.waifu.pics/sfw/"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/next/<category>")
def next_waifu(category):
    resp = requests.get(API_BASE + category)
    if resp.status_code == 200:
        data = resp.json()
        return jsonify({"url": data.get("url")})
    return jsonify({"error": "Ni slike"}), 500

if __name__ == "__main__":
    app.run(debug=True)


