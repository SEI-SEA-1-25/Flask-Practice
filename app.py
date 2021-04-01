from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
import random
app = Flask(__name__)

@app.route('/')
def home_page():
    return "🌎 🌍 🌏"

# GET /
@app.route("/greeting")
def greeting():
    return render_template("greeting")


@app.route('/pie')
def return_pie_ingredients():
    ingredients = ['crust','filling','pie pan', 'sugar', 'love', '45 minutes' ,'mama\'s homestyle technique']
    randIndex = random.randrange(0,len(ingredients),1)
    return jsonify({'pie ingredient':ingredients[randIndex]})