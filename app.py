from flask import Flask, jsonify
app = Flask(__name__)


def parse_file():
    with open ('quote_color') as file:
        content = file.readlines()
        return {'quote': str(content[0]), 'color': str(content[1])}

@app.route('/')
def hello():
    return jsonify(parse_file())

if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0')