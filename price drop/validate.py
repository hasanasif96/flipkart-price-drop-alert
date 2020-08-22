# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:28:05 2020

@author: Hasan
"""
from flask import flash, redirect, url_for
import re
def validator(email,url,user):
    if re.search("[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})", email):
        if url .startswith('https://www.flipkart'):
            if len(user)>3:
                return ("ok")
            else:
                flash('Looks like you have entered invalid name!')
                return redirect(url_for('login'))
        else:
            flash('Looks like you have entered invalid url!')
            return redirect(url_for('login'))
    else:
        flash('Looks like you have entered invalid email!')
        return redirect(url_for('login'))
            
