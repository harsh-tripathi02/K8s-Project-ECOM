from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = [
        {"id": 1, "product_id": 1, "quantity": 2},
        {"id": 2, "product_id": 3, "quantity": 1},
        {"id": 3, "product_id": 2, "quantity": 5},
    ]
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
