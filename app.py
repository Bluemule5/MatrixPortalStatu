from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({'quote': 'Hello world!', 'color': '#ed0c0c'})

if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')