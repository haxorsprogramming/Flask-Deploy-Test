from flask import render_template, request, redirect, url_for, flash
from flask_app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def index():
    return render_template("about.html")