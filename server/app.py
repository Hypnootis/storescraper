from selenium_scrape import get_searches
from flask_cors import CORS
from flask import Flask, jsonify

# test_data = {
#     "0": {
#         "comparison_price": "0,89 \u20ac/l",
#         "product_name": "Kotimaista kevytmaito 1 L",
#         "unit_price": "0,89 \u20ac",
#     },
#     "1": {
#         "comparison_price": "1,25 \u20ac/l",
#         "product_name": "Kotimaista laktoositon kevytmaitojuoma 1 L",
#         "unit_price": "1,25 \u20ac",
#     },
#     "2": {
#         "comparison_price": "0,79 \u20ac/l",
#         "product_name": "Kotimaista rasvaton maito 1l",
#         "unit_price": "0,79 \u20ac",
#     },
#     "3": {
#         "comparison_price": "1,19 \u20ac/l",
#         "product_name": "Kotimaista t\u00e4ysmaito 1l",
#         "unit_price": "1,19 \u20ac",
#     },
#     "4": {
#         "comparison_price": "3,16 \u20ac/kg",
#         "product_name": "Kotimaista 250g rasvaton laktoositon maitorahka",
#         "unit_price": "0,79 \u20ac",
#     },
# }

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})


@app.route("/api")
def hello_world():
    return jsonify(message="Hello, World!")


@app.route("/api/search/<param>")
def search(param):
    return jsonify(get_searches(param, False))


if __name__ == "__main__":
    app.run(debug=True, port=8080)


# get_searches("maito", False, "lowest_comparison_price")
