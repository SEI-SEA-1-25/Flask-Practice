from flask import Flask, render_template
app = Flask(__name__)




# make Home route
@app.route('/')
def hello():
  return render_template('home.html', name="Chris")


#Greeting route

@app.route('/greeting/<name>')
def greeting():
  return render_template('greeting.html')


# JSON route
@app.route('/pie')
def pie():
  return jsonify({'pie ingredient': ingredients[0]})
