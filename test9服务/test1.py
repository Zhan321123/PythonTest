from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求

@app.route('/receive_points', methods=['POST'])
def receive_points():
    data = request.get_json()
    points = data.get('points', [])
    print("Received points:")
    print(points)
    return jsonify({"message": "Points received successfully"})

if __name__ == '__main__':
    app.run(debug=True)