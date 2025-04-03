from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/payments', methods=['GET'])
def get_payments():
    payments = [
        {"id": 1, "order_id": 1, "status": "completed"},
        {"id": 2, "order_id": 2, "status": "pending"},
        {"id": 3, "order_id": 3, "status": "failed"},
    ]
    return jsonify(payments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
