from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)

DATA_FILE = "view_data.json"

# Initialize the data file
try:
    with open(DATA_FILE) as f:
        view_data = json.load(f)
except FileNotFoundError:
    view_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/track-view', methods=['POST'])
def track_view():
    data = request.json
    product_id = data['productId']
    view_time = int(data['viewTime'])
    user_id = "user123"  # Dummy for now

    if user_id not in view_data:
        view_data[user_id] = {}

    if product_id not in view_data[user_id]:
        view_data[user_id][product_id] = 0

    view_data[user_id][product_id] += view_time

    with open(DATA_FILE, "w") as f:
        json.dump(view_data, f)

    return jsonify({"status": "ok"})

@app.route('/api/recommendations')
def recommendations():
    user_id = "user123"
    user_views = view_data.get(user_id, {})
    sorted_products = sorted(user_views.items(), key=lambda x: x[1], reverse=True)
    top_products = [prod[0] for prod in sorted_products[:2]]
    return jsonify(top_products)

if __name__ == "__main__":
    app.run(debug=True)
