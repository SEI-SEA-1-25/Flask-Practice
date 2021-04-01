from flask import Flask, render_template, rand_idx, jsonify, request
from dotenv import load_dotenv
import os

app = Flask(__name__)

# make home page route
@app.route('/')
def hello_flask():
    return 'Hello world'

# GET /greeting
@app.route('/greeting')
def greeting():
    return render_template('greeting.html', name='Kathy')

ingredients = [
    'applepie',
    'peach cobbler',
    'strawberry rhubarb'
]

# GET /pie
@app.route('/pie')
def pie():
    global ingredients
    rand_idx = random.randint(0, len(ingredients) - 1)
    return jsonify({'pie ingredients: ingredients[rand_idx]'})

# GET and POST 
@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    global ingredients
    if request.method == 'GET':
        return render_template('recipe.html', ingredients=ingredients)