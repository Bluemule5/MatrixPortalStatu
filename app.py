from flask import Flask, jsonify, render_template, redirect, g
app = Flask(__name__)


def parse_file():
    with open ('test') as file:
        content = file.readlines()
        line_1 = content[0]
        line_split = line_1.split(",")
        return {'quote': str(line_split[0]), 'color': str(line_split[1])}


def add_message(quote, color):
    message = quote + "," + color
    with open("test", 'w') as file:
        file.write(message)
    pass


def clear_message():
    message = "test,#000000"
    with open("test", 'w') as file:
        file.write(message)
    pass


@app.route('/')
def hello():
    return jsonify(parse_file())


@app.route('/outofoffice')
def outofoffice():
    add_message("Out of Office", "#0000ff")
    return redirect("/")

@app.route('/inoffice')
def inoffice():
    add_message("In Office", "#00ff00")
    return redirect("/")

@app.route('/inmeeting')
def inameeting():
    add_message("In A Meeting", "#ff0000")
    return redirect("/")

@app.route('/gonehome')
def gonehome():
    add_message("Gone Home", "#ffffff")
    return redirect("/")

@app.route('/blankmessage')
def blankmessage():
    clear_message()
    return redirect("/")

if __name__ == '__main__':
    #app.run(port=80, host='0.0.0.0')
    app.run()