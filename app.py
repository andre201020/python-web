from flask import Flask, render_template, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask("hello")

db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    title = db.Column(db.String(70), nullable=False)
    body = db.Column(db.String(500))
    author =db.Column(db.String(20))
    created =db.Column(db.Datetime,nullable=False, default=datetime)

@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/populate")
def populate():
    post1 = Post(title="Post 1", body="Texto do Post 1", author="autor do post 1")
    post2 = Post(title="Post 2", body="Texto do Post 2", author="autor do post 2")
    db.session(post1)
    db.session(post2)
    db.session.commit()
    return redirect("/")