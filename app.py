from flask import Flask, render_template, redirect, jsonify, request
app = Flask(__name__)

@app.route('/')
def home_route():
    return 'Hellooo 🐻'


@app.route('/greeting')
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
  return jsonify({'pie ingredient': ingredients[0]})

  