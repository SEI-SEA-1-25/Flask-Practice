from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
import random

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
  return "👋🏾 Hello World! 🌍"

@app.route("/greeting")
def greeting():
  return render_template("index.html", name="Nakisha")

ingredients = [
  "marionberry",
  "blueberry",
  "raspberry"
]

@app.route("/pie")
def pie():
  global ingredients
  rand_idx = random.randint(0, len(ingredients) - 1)
  return jsonify({"pie ingredient": ingredients[rand_idx]})

#GET and POST /recipe
@app.route("/recipe", methods=["GET", "POST"])
def recipe():
  global ingredients
  if request.method == "GET":
    return render_template("recipe.html", ingredients=ingredients)
  elif request.method == "POST":
    ingredient = request.form["ingredient"]

    ingredients.append(ingredient)
    return redirect('/recipe')
