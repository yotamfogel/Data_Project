"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Data_Project import app
from Data_Project.models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

from flask import render_template, request

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


from Data_Project.models.Forms import CryptoForm
from Data_Project.models.Forms import AllOfTheAboveForm


from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from Data_Project.models.QueryFormStructure import QueryFormStructure 
from Data_Project.models.QueryFormStructure import LoginFormStructure 
from Data_Project.models.QueryFormStructure import UserRegistrationFormStructure 

db_Functions = create_LocalDatabaseServiceRoutines()

from os import path
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'The first argument to the field'


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
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/bitcoin_price.csv'))
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
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/ripple_price.csv'))
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
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/ethereum_price.csv'))
    raw_data_table3 = df.to_html(classes = 'table table-hover')
    return render_template(
        'ethereum.html',
        title='Ethereum',
        data_table3 = raw_data_table3,
        year=datetime.now().year,
        message='Ethereum Prices'
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)
    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            return redirect('')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login As Existing User',
        year=datetime.now().year,
        repository_name='Pandas',
    )

@app.route('/query' , methods = ['GET' , 'POST'])
def query():

    print("Query")

    form1 = CryptoForm()
    chart = {}
    height_case_1 = "100"
    width_case_1 = "400"

    df_ripple = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/ripple_price.csv'))
    df_ethereum = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/ethereum_price.csv'))
    df_bitcoin = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/bitcoin_price.csv'))
    crypto_dict = {'bitcoin' : df_bitcoin , 'ripple' : df_ripple , 'ethereum' : df_ethereum}

    if request.method == 'POST':
        cryptocurrency = form1.cryptocurrency.data 
        start_date = form1.start_date.data
        end_date = form1.end_date.data
        kind = form1.kind.data
        height_case_1 = "300"
        width_case_1 = "750"

        print(cryptocurrency)
        print(start_date)
        print(end_date)
        print(type(start_date))
        x = str(start_date)
        print(x)

    return render_template(
        'query.html',
        form1 = form1,
        src_case_1 = chart,
        height_case_1 = height_case_1 ,
        width_case_1 = width_case_1 
        )



