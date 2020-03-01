__author__ = "BATIKAN BORA ORMANCI"
# These are just some random tests on flask, nothing important

# To run:
"""
flask run
"""
# If you get following error : 
"""
Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
"""
# Do
"""
export FLASK_APP=application.py
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hi():
    return "Hello, git!"

@app.route("/<string:name>")
def greet(name):
    return f"Hello, {name.capitalize()}"