from flask import Flask, render_template, request, jsonify, redirect
import random

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
        random_index = random.randint(0, 2)
        return jsonify({ 'jason': jason_json[random_index] })

ingredients = [
    'Sugar',
    'Spice',
    'Everything nice'
]

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    global ingredients
    idx_range = range(len(ingredients))
    if request.method == 'GET':
        return render_template(
            'recipe.html', 
            piename='Rhubarbara Anne', 
            ingredients=ingredients
            )
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        ingredients.append(ingredient)
        return redirect('/recipe')


