# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:37:12 2020

@author: Hasan
"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from validate import validator
#from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from scraper import scrape
from mail import send_mails

#sched = BackgroundScheduler(daemon=True)

app = Flask(__name__)
sched = BackgroundScheduler(daemon=True)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b3543651e1d610:038afb89@us-cdbr-east-02.cleardb.com/heroku_9f363e97731959a'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 499
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
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


###getting data fro database 
def alert_gen():
    users = Users.query.all()
    url=[]
    price=[]
    mail=[]
    name=[]
    print(url,name)
    for user in users:
        url.append(user.url)
        price.append(user.user_price)
        mail.append(user.email)
        name.append(user.username)
    for i in range(0,len(url)):
        try:
            if scrape(url[i])<price[i]:
                send_mails(mail[i],name[i],url[i])
            else:
                continue
        except:
            continue
    
sched.add_job(alert_gen,'interval', minutes=2)
 
sched.start()
   
    
#users = Users.query.all()
#url=[]
#price=[]
#mail=[]
#name=[]
#for user in users:
#    url.append(user.url)
#    price.append(user.user_price)
#    mail.append(user.email)
#    name.append(user.username)

#    new_price=[]
#    page=requests.get(user.url)
#    soup=BeautifulSoup(page.text,"html.parser")
#    price_text=soup.find_all(class_="a-size-medium a-color-price priceBlockBuyingPriceString")
#    for item in price_text:
#        new_price.append(item.text)
#    new_price = re.findall(r'\d+', new_price[0])
#    new_price.pop()
#    new_price="".join(new_price)
#    new_price=int(new_price)
#    if user.user_price<new_price:
#        send_mails(user.email,user.username)
#    else:
#        continue

#    if scrape(url)< price:
#        send_mails(user.email,user.username)
#    else:
#        continue
        

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)