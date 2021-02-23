from flask import Flask, jsonify, json

app = Flask(__name__)

# Decorator
@app.route('/')
def index():
    return jsonify({'name': 'praveen', 'age':28})


if __name__ == "__main__":
    app.run(debug = True)