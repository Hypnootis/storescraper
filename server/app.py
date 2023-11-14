from selenium_scrape import get_searches
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})


@app.route("/api")
def hello_world():
    return jsonify(message="Hello, World!")


@app.route("/api/search")
def search():
    return jsonify(get_searches("maito", False))


if __name__ == "__main__":
    app.run(debug=True, port=8080)


# get_searches("maito", False, "lowest_comparison_price")
