"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Data_Project import app
from Data_Project.models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    chart = 'static/imgs/bitcoin.jpg'
    height_case_1 = "100"
    width_case_1 = "400"

    dfBC = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/bitcoin_price.csv'))
    dfRP = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/ripple_price.csv'))
    dfET = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/ethereum_price.csv'))
    crypto_dict = {'Bitcoin' : dfBC , 'Ripple' : dfRP , 'Ethereum' : dfET}

    if request.method == 'POST':
        cryptocurrency1 = form1.cryptocurrency1.data 
        cryptocurrency2 = form1.cryptocurrency2.data
        start_date = form1.start_date.data
        end_date = form1.end_date.data
        kind = form1.kind.data
        height_case_1 = "300"
        width_case_1 = "750"

        print(cryptocurrency1)
        print(cryptocurrency2)
        print(start_date)
        print(end_date)
        print(type(start_date))
        x = str(start_date)
        print(x)

        

        dfBC = dfBC[['Date', 'Close']]
        dfRP = dfRP[['Date', 'Close']]
        dfET = dfET[['Date', 'Close']]

        dfBC = dfBC.set_index('Date')
        dfRP = dfRP.set_index('Date')
        dfET = dfET.set_index('Date')

        dfBC.index = pd.to_datetime(dfBC.index)
        dfRP.index = pd.to_datetime(dfRP.index)
        dfET.index = pd.to_datetime(dfET.index)

        dfBC = dfBC[::-1]
        dfRP = dfRP[::-1]
        dfET = dfET[::-1]


        dfBC = dfBC[start_date:end_date]
        dfRP = dfRP[start_date:end_date]
        dfET = dfET[start_date:end_date]

        fig1 = plt.figure()
        axx = fig1.add_subplot(111)
        fig1.subplots_adjust(bottom=0.22)
        if cryptocurrency1 == 'Bitcoin':
            dfBC["Close"].plot(legend = True, ax = axx)

        if cryptocurrency1 == 'Ripple':
            dfRP["Close"].plot(legend = True, ax = axx)

        if cryptocurrency1 == 'Ethereum':
            dfET["Close"].plot(legend = True, ax = axx)
        
        if cryptocurrency2 == 'Bitcoin':
            dfBC["Close"].plot(secondary_y = True, legend = True, ax = axx)

        if cryptocurrency2 == 'Ripple':
            dfRP["Close"].plot(secondary_y = True, legend = True, ax = axx)

        if cryptocurrency2 == 'Ethereum':
            dfET["Close"].plot(secondary_y = True, legend = True, ax = axx)
            
        if cryptocurrency2 != 'None':
            axx.right_ax.set_ylabel(cryptocurrency2)
                 

        

        axx.set_ylabel(cryptocurrency1)
        

        chart=plt_to_img(fig1)
        

    return render_template(
        'query.html',
        form1 = form1,
        chart = chart,
        height_case_1 = height_case_1 ,
        width_case_1 = width_case_1 
        )
def plt_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String



