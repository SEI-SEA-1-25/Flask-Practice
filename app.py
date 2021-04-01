from flask import Flask, render_template, jsonify, request, redirect
import random

app = Flask(__name__)

# routes
@app.route('/')
def hello_flask():
    return "Hello World"


@app.route('/greeting')
def greeting_msg():
    return render_template('index.html', name="Akilah")

pie_ingredients = [
    "apple",
    "sugar",
    "egg"
]

@app.route('/pie', methods=['GET'])
def pie():
    global pie_ingredients
    random_index = random.randint(0, len(pie_ingredients) - 1)
    return jsonify({ 'pie ingredient': pie_ingredients[random_index]})

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    global pie_ingredients
    if request.method == 'GET':
        return render_template('recipe.html', pie_ingredients=pie_ingredients)
    elif request.method == 'POST':
        ingredient = request.form['ingredient']
        pie_ingredients.append(ingredient)
        return redirect('/recipe')

