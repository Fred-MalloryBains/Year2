from flask import render_template
from app import app

@app.route('/fruit')
def displayFruit():
    fruits = ["Apple", "Banana", "Orange", "Kiwi"]
    return render_template("fruit.html",fruits=fruits)