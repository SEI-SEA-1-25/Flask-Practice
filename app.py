# import flask
from flask import Flask, render_template,request,jsonify,redirect


#import dotenv
from dotenv import load_dotenv
#import the operating system
import os

print(os.environ['MY_BIG_SECRET'])
# config app
app = Flask(__name__)


# make route!
@app.route('/')
def hello_world():
    return 'Hello World 👋'


    # GET/greeting --landing pages for greeting 
@app.route('/greeting')

def greeting():
    return render_template('greeting.html',name=name_one)

# # GET/greeting/onecats
# @app.route('/greeting/<name>')
# def greeting_name(name):
#     return render_template('greeting.html',name=name)

name_one =[

        'weston the saver',
        'henry the solver',
        'collin the master',
        'me the student'
]

@app.route('/api/greeting',methods=['GET'])
def greeting_api():
    #get the global var
    global name_one
    #use an if check to handle http method
    if request.method =='GET':
        return jsonify({ 'greeting':name_one })



# create initial list of ingredients
ingredients = ["meat", "vegOil", "masala"]

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    global ingredients
    if request.method == 'POST':
        # get user input for ingredient and append to ingredients
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)

        # get a random number between 0-length of list and set to index
        index = random.randint(0, (len(ingredients) - 1))
    
        # return a json object with random pie ingredient
        return jsonify({'pie ingredient': ingredients[index]})
    else:
        return render_template('pieForm.html')
