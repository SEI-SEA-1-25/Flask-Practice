from flask import Flask, render_template, jsonify, request
import random

app=Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return 'Hello,!'


@app.route('/greeting')
def greeting():
    return render_template('index.html', name="Semuel")


ingredients = ["Strawberry", "Blueberry", "Rasberry"]

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    global ingredients
    if request.method == 'POST':
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)

        index = random.randint(0, (len(ingredients) - 1))
    
        # return a json object with random pie ingredient
        return jsonify({'pie ingredient': ingredients[index]})
    else:
        return render_template('pieForm.html')