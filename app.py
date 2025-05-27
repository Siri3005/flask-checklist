from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows React to talk to Flask

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print(data)
    return jsonify({"message": "Checklist received!", "data": data})

if __name__ == "__main__":
    app.run(debug=True)
