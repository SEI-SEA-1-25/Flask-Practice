from flask import Flask, render_template, request, jsonify, redirect
from dotenv import load_dotenv
import os
print(os.environ['SECRET_CODE'])


#  Configure APP

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World! 👽'


@app.route('/greeting/<name>')
def greeting_name(name):
    return render_template('index.html', name=name)


apple_pie_recipe= [
    'apples',
    'sugar',
    'flour',
    'butter',
    'cinnamon',
    'nutmeg',
]

@app.route('/api/recipes', methods=['GET', 'POST'])
def recipe_api():
    global apple_pie_recipe

    if request.method == 'GET':
        return jsonify( {'apple_pie_ingredient': apple_pie_recipe[2] })
    
    if request.method == 'POST':
        request_body = request.get_json()
        apple_pie_recipe.append(request_body['ingredient'])

        return redirect('/api/recipes')


recipe = {
    'ingredient 1': 'Vidalia Onions',
    'ingredient 2': 'Cippolini Onions',
    'ingredient 3': 'Walla Walla Sweet Onions',
    'ingredient 4': 'Shallots',
    'ingredient 5': 'Batonnet of Pork Belly',
    'ingredient 6': 'Garlic',
    'ingredient 7': 'Flour',
    'ingredient 8': 'Butter',
    'ingredient 9': 'Salt',
    'ingredient 10': 'Pedro Ximenez'
}

@app.route('/recipes', methods=['GET', 'POST'])
def recipes():
    global recipe

    if request.method == 'GET':
        return render_template('recipe.html',recipe=recipe)

