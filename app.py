from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {
        "title": "1o Post",
        "body": "texto do 1o Post",
        "author": "autor 1o Post",
        "created": datetime(2022,7,25)
    },
    {
        "title": "2o Post",
        "body": "texto do 2o Post",
        "author": "autor 2o Post",
        "created": datetime(2022,7,26)
    }
]

@app.route("/")
def index():
    return render_template("index.html", posts = posts)