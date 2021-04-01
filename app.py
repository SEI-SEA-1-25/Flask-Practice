from flask import Flask, render_template, jsonify, redirect, request
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, world!'

@app.route('/greeting')
def greeting():
  return render_template('index.html', name="Akilah")

ingredients = ['banana', 'chocolate', 'peanut butter']

@app.route('/pie', methods=["GET"])
def ingredients_api():
  global ingredients
  rand_idx = random.randint(0, len(ingredients) - 1)
  return jsonify({'pie ingredient': ingredients[rand_idx]})

@app.route('/recipe', methods=["GET", "POST"])
def recipe():
  global ingredients
  if request.method == "GET":
    return render_template('recipe.html', ingredients=ingredients)
  elif request.method == "POST":
    ingredient = request.form['ingredient']
    ingredients.append(ingredient)
    return redirect('/recipe')