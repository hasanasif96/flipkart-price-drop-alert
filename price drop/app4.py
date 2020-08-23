# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:37:12 2020

@author: Hasan
"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from validate import validator




app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b3543651e1d610:038afb89@us-cdbr-east-02.cleardb.com/heroku_9f363e97731959a'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

app.secret_key = 'hello'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    url = db.Column(db.String(1200))
    user_price = db.Column(db.Integer)
    def __init__(self, username, email,url,user_price):
        self.username = username
        self.email = email
        self.url = url
        self.user_price = user_price
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        mail = request.form["mail_id"]
        url= request.form["url"]
        price= request.form["price"]
        if validator(mail,url,user)=="ok":
            usr=Users(user,mail,url,price)
            db.session.add(usr)
            db.session.commit()
            return render_template("success.html")
        else:
            return render_template("home.html")
    
    else:
        return render_template("home.html")   

        

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
