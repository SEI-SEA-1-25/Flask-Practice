from flask import Flask, render_template, request, jsonify, redirect
from dotenv import load_dotenv
import os, random
app = Flask(__name__)
# print(os.environ['SECRET'])
@app.route('/')
def hello():
    return 'hello from app'

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='sarah')
ingredients = [
    'chocolate',
    'peanutbutter',
    'coconut milk'
]

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    global ingredients
    if request.method == 'GET':
        num = (int(random.uniform(0,3)))
        return jsonify({'ingredient': ingredients[num]})
    if request.method == 'POST':
        pass