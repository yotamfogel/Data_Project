"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Data_Project import app
#from Data_Project import create_LocalDatabaseServiceRoutines


from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from Data_Project.models.QueryFormStructure import QueryFormStructure 
from Data_Project.models.QueryFormStructure import LoginFormStructure 
from Data_Project.models.QueryFormStructure import UserRegistrationFormStructure 

app.config['SECRET_KEY'] = '1234'

###from DemoFormProject.Models.LocalDatabaseRoutines import IsUserExist, IsLoginGood, AddNewUser 

#db_Functions = create_LocalDatabaseServiceRoutines()

#a

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        img_ripple = '/static/imgs/ripple.png',
        img_ethereum = '/static/imgs/ethereum.jpg',
        img_bitcoin = '/static/imgs/bitcoin.jpg',
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='How to contact the creator of the site'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='About the creator of the site'
    )
@app.route('/data')
def data():
    """Renders the about page."""
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='Your data page'
    )

@app.route('/bitcoin')
def bitcoin():
    """Renders the about page."""
    #df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\bitcoin_price.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/bitcoin_price.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')
    return render_template(
        'bitcoin.html',
        title='Bitcoin',
        year=datetime.now().year,
        data_table = raw_data_table,
        message='Bitcoin Prices'

    )

@app.route('/ripple')
def ripple():
    """Renders the about page."""
        #df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\bitcoin_price.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/ripple_price.csv'))
    raw_data_table2 = df.to_html(classes = 'table table-hover')
    return render_template(
        'ripple.html',
        title='Ripple',
        data_table2 = raw_data_table2,
        year=datetime.now().year,
        message='Ripple Prices'
    )

@app.route('/ethereum')
def ethereum():
    """Renders the about page."""
        #df = pd.read_csv(path.join(path.dirname(__file__), 'static\\data\\bitcoin_price.csv'))
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/data/ethereum_price.csv'))
    raw_data_table3 = df.to_html(classes = 'table table-hover')
    return render_template(
        'ethereum.html',
        title='Ethereum',
        data_table3 = raw_data_table3,
        year=datetime.now().year,
        message='Ethereum Prices'
    )

@app.route('/register')
def register():
    return render_template(
        'register.html', 
        title='Register',
        year=datetime.now().year,
        message='Sign up to the site',
        )

@app.route('/login')
def login():
    """Renders the contact page."""
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Login to the site with an existing account'
    )


