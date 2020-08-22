# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:17:38 2020

@author: Hasan
"""
import re
import requests
from bs4 import BeautifulSoup
def scrape(x):
    new_price=[]
    page=requests.get(x)
    soup=BeautifulSoup(page.text,"html.parser")
    price_text=soup.find_all(class_="_1vC4OE _3qQ9m1")
    for item in price_text:
        new_price.append(item)
    new_price = re.findall(r'\d+', new_price[0])
    new_price="".join(new_price)
    new_price=int(new_price)
    return (new_price)

