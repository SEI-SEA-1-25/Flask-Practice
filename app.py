from flask import Flask, render_template, jsonify


app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    pass

@app.route('/greeting')
def greeting():
    return render_template('index.html', name='Dagm')

ingredients = {
    'piebary'
    'banana'
    'rasbary'
}
@app.route('/pie')
def pie():
    global ingredients
    rand_idx = random.randint(0, len(ingredients) - 1)
    return jsonify({'pie ingredient': ingredients[rand_idx]})