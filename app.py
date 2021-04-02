# imported modules
from flask import Flask, render_template, jsonify, request, redirect
import random 

# Create the app variable
app = Flask(__name__)
print(__name__)

# Get /
@app.route('/')
def home():
    return 'Hello World'

# GET /greeting 
@app.route('/greeting')
def greeting():
    return render_template('index.html', name="Henry")


ingredients = [
    'marionberry',
    'blueberry',
    'raspberry'
]

# GET /pie
@app.route('/pie')
def pie():
    global ingredients
    rand_idx = random.randint(0, len(ingredients) - 1)
    return jsonify({'pie ingredient': ingredients[rand_idx]})


# GET and Post /recipe 
@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    global ingredients 
    if request.method == 'GET':
        return render_template('recipe.html', ingredients=ingredients)
    elif reques.method == 'POST':
        ingredient = request.form['ingredient']
        ingredients.append(ingredient)
        return redirect('/recipe')

