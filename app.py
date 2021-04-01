from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World 🦀'

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Luigi')

jason_json = [
    "samoa",
    "alex gordon's brother",
    "schwartzman",
]

@app.route('/pie', methods=['GET'])
def pie():
    global jason_json
    if request.method == 'GET':
        return jsonify({ 'jason': jason_json[0] })

