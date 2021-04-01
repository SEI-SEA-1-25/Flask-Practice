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
    return render_template("greeting", name="Strawberry Shortcakes")

ingredients = {
    "apple caramel",
    "pecan",
    "sprinkles",
    "blueberry"
}


@app.route('/pie')
def pie():
    global ingredients
    rand_idx = random.randint(0, len(ingredients) - 1)
    return jsonify({"pie ingredient": ingredients[rand_idx]})