from flask import Flask, render_template, jsonify, redirect, request

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
  return jsonify({'pie ingredient': ingredients[0]})

@app.route('/recipe', methods=["GET", "POST"])
def recipe():
  global ingredients
  if request.method == "POST":
    ingredient = request.form["ingredient"]
    ingredients.append(ingredient)
    return jsonify({'pie ingredients': ingredients})

  else:
    return render_template('recipe.html')
