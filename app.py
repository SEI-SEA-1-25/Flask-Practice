# Imported Modules
from flask import Flask, render_template, jsonify
import random

# Create the app variables
app = Flask(__name__)
print(__name__)

# Get /
@app.route('/')
def home():
    return 'Hello, World'

# GET / greeting
@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Ian')

ingredients = [
    'peaches',
    'blueberry',
    'raspberry'
]


# GET /pie
@app.route('/pie')
def pie():
    rand_idx = random.rand(0, len(ingredients) - 1)
    return jsonify({'pie ingredient': indredients[rand_idx]})

# go back and do bonus!