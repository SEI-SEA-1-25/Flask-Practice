from flask import flask, redirect
import random

app = Flask(__name__)
print(__name__)

# GET
@app.route('/')
def home():
    return('hello world')

# GET greeting
@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Brinn')

ingredients = [
    'raspberry',
    'blueberry',
    'rhubarb',
    'strawberry'
]
# GET /pie
@app.route('/pie')
def pie():
    global ingredients
    rand_index = random.rand(0, len(ingredients) -1)
    return jsonify({'pie ingredient: ': ingredients[rand_index]})

# GET and POST /recipe
@app.route('/recipe')
def recipe():
    global ingredients
    if request.method == 'GET':
        return render_template('recipe.html', ingredients=ingredients)
    elif request.method == 'POST':
        ingredient = request.form['ingredient']
        ingredients.append(ingredient)
        return redirect('/recipe')
