from flask import Flask, render_template, redirect, jsonify, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_route():
    return 'Hellooo 🐻'


@app.route('/greeting', methods='GET')
def greeting():
    return render_template('index.html', name="Akilah")

ingredients = [
    'mango', 
    'apple', 
    'banana'
]

@app.route('/pie', methods=["GET"])
def ingredients_api():
    global ingredients
    random_ind = random.randint(0, len(ingredients) - 1)
    return jsonify({'pie ingredient': ingredients[random_ind]})

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    if request.method == 'GET':
        return render_template('recipe.html', ingredients=ingredients)
    elif request.method == 'POST':
        ingredient = request.form['ingredient']
        ingredients.append(ingredient)
        return redirect('/recipe')

