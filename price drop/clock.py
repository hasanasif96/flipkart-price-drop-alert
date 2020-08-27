# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:41:21 2020

@author: Hasan
"""
from app4 import Users
from scraper import scrape
from mail import send_mails
#from apscheduler.schedulers.background import BackgroundScheduler

#users = Users.query.all()
def alert_gens():
    for i in users:
            try:
                if scrape(i.url)<i.user_price:
                    send_mails(i.email,i.username)
                else:
                    continue
            except:
                continue

#sched = BackgroundScheduler(daemon=False)
  
#sched.add_job(alert_gens,'interval', minutes=3)
 
#sched.start()


from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def alert_gen():
    users = Users.query.all()
    for i in users:
            try:
                if scrape(i.url)<i.user_price:
                    send_mails(i.email,i.username,i.url)
                else:
                    continue
            except:
                continue

sched.start()
#if __name__ == '__main__':
#    from apscheduler.schedulers.background import BackgroundScheduler
#    sched = BackgroundScheduler()
#    sched.add_job(alert_gen,'interval', minutes=5)
#sched.start()
