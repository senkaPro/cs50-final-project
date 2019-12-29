from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///shortener.db")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')