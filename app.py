from flask import Flask, render_template
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "👋🏾 Hello World! 🌍"

@app.route("/greeting")
def greeting():
  return render_template("index.html", name=greeting)