from flask import Flask, render_template, request, jsonify, redirect
from dotenv import load_dotenv
import os, random
app = Flask(__name__)
# print(os.environ['SECRET'])
@app.route('/')
def hello():
    return 'hello from app'

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Sarah Marie')

ingredients = [
    'chocolate',
    'peanutbutter',
    'coconut milk'
]

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    global ingredients
    if request.method == 'GET':
        # my way
        # num = (int(random.uniform(0,2)))
        # henry's way
        num = random.randint(0,len(ingredients)- 1)
        return jsonify({'ingredient': ingredients[num]})
    if request.method == 'POST':
        pass

@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    global ingredients
    if request.method == 'GET':
        return render_template('recipe.html', ingredients=ingredients)
    elif request.method == 'POST':
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)
        return redirect('/recipe')