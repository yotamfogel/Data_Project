#----------------------------------------------------
#| Yotam Fogel                                      |
#| י5                                               |
#----------------------------------------------------

from datetime import datetime
from flask import render_template
from Data_Project import app
from Data_Project.models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from flask import render_template, request, redirect

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
@app.route('/home') # The home page
def home():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        img_ripple = '/static/imgs/ripple.png',
        img_ethereum = '/static/imgs/ethereum.jpg',
        img_bitcoin = '/static/imgs/bitcoin.jpg',
    )

@app.route('/contact') # The contact page
def contact():
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='How to contact the creator of the site'
    )

@app.route('/about') # The about page
def about():
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='About the creator of the site'
    )
@app.route('/data') #The data column at the top, doesn't actually get used as a page.
def data():
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='Your data page'
    )

@app.route('/bitcoin') # The bitcoin data page
def bitcoin():
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/bitcoin_price.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')
    return render_template(
        'bitcoin.html',
        title='Bitcoin',
        year=datetime.now().year,
        data_table = raw_data_table,
        message='Bitcoin Prices'

    )

@app.route('/ripple') # The ripple data page
def ripple():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/ripple_price.csv'))
    raw_data_table2 = df.to_html(classes = 'table table-hover')
    return render_template(
        'ripple.html',
        title='Ripple',
        data_table2 = raw_data_table2,
        year=datetime.now().year,
        message='Ripple Prices'
    )

@app.route('/ethereum') # The Ethereum data page
def ethereum():
    df = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/ethereum_price.csv'))
    raw_data_table3 = df.to_html(classes = 'table table-hover')
    return render_template(
        'ethereum.html',
        title='Ethereum',
        data_table3 = raw_data_table3,
        year=datetime.now().year,
        message='Ethereum Prices'
    )

@app.route('/register', methods=['GET', 'POST']) # The register page
def register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            return redirect('login')
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

@app.route('/login', methods=['GET', 'POST']) # The login page
def Login():
    form = LoginFormStructure(request.form)
    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            return redirect('query')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login As Existing User',
        year=datetime.now().year,
        repository_name='Pandas',
    )

@app.route('/query' , methods = ['GET' , 'POST']) # The query pae
def query():

    form1 = CryptoForm(start_date = pd.Timestamp('2017-08-03'), end_date = pd.Timestamp('2019-08-03'))# Saves the CryptoForm from Forms.py as form1.

    chart = 'static/imgs/bitcoin.jpg'
    height_case_1 = "100"
    width_case_1 = "400"

    dfBC = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/bitcoin_price.csv')) # Creates a dataframe called dfBC from the database bitcoin_price.csv
    dfRP = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/ripple_price.csv')) # Creates a dataframe called dfBC from the database ripple_price.csv
    dfET = pd.read_csv(path.join(path.dirname(__file__), 'static/Data/ethereum_price.csv')) # Creates a dataframe called dfBC from the database ethereum_price.csv
    crypto_dict = {'Bitcoin' : dfBC , 'Ripple' : dfRP , 'Ethereum' : dfET}

    if request.method == 'POST':
        backgroundimg = '/static/imgs/bitcoin.jpg'
        cryptocurrency1 = form1.cryptocurrency1.data # Puts our choice in the form into a variable named cryptocurrency1
        cryptocurrency2 = form1.cryptocurrency2.data # Puts our choice in the form into a variable named cryptocurrency2
        start_date = form1.start_date.data # Puts our choice in the form into a variable named start_date
        end_date = form1.end_date.data # Puts our choice in the form into a variable named end_date
        kind = form1.kind.data #Puts our choice in the form into a variable named kind
        height_case_1 = "300"
        width_case_1 = "750"

        dfBC = dfBC[['Date', 'Close']] # Limits the dataframe to the 2 relevant columns we need, date and close price.
        dfRP = dfRP[['Date', 'Close']] # Limits the dataframe to the 2 relevant columns we need, date and close price.
        dfET = dfET[['Date', 'Close']] # Limits the dataframe to the 2 relevant columns we need, date and close price.

        dfBC = dfBC.set_index('Date') # Sets the y axis to the date
        dfRP = dfRP.set_index('Date') # Sets the y axis to the date
        dfET = dfET.set_index('Date') # Sets the y axis to the date

        dfBC.index = pd.to_datetime(dfBC.index) # Turns it into datetime measurements
        dfRP.index = pd.to_datetime(dfRP.index) # Turns it into datetime measurements
        dfET.index = pd.to_datetime(dfET.index) # Turns it into datetime measurements

        dfBC = dfBC[::-1] # Flips the dataset from top to bottom (because I had a problem with that)
        dfRP = dfRP[::-1] # Flips the dataset from top to bottom (because I had a problem with that)
        dfET = dfET[::-1] # Flips the dataset from top to bottom (because I had a problem with that)

        dfBC = dfBC[start_date:end_date] # Limits the data to the start and end dates we chose in the form
        dfRP = dfRP[start_date:end_date] # Limits the data to the start and end dates we chose in the form
        dfET = dfET[start_date:end_date] # Limits the data to the start and end dates we chose in the form

        fig1 = plt.figure() # Honestly i have no idea
        axx = fig1.add_subplot(111) # Honestly i have no idea
        fig1.subplots_adjust(bottom=0.22) # Changes the size of the "box" the graph is in
        if cryptocurrency1 == 'Bitcoin':
            dfBC["Close"].plot(legend = True, ax = axx) # If the chosen cryptocurrency1 is bitcoin, create a plot from dfBC with the bitcoin data
            

        if cryptocurrency1 == 'Ripple':
            dfRP["Close"].plot(legend = True, ax = axx) # If the chosen cryptocurrency1 is ripple, create a plot from dfRP with the ripple data

        if cryptocurrency1 == 'Ethereum':
            dfET["Close"].plot(legend = True, ax = axx) # If the chosen cryptocurrency1 is ethereum, create a plot from dfET with the ethereum data
        
        if cryptocurrency2 == 'Bitcoin':
            dfBC["Close"].plot(secondary_y = True, legend = True, ax = axx) # If the chosen cryptocurrency2 is bitcoin, create a second y axis and set it to bitcoin with data from dfBC

        if cryptocurrency2 == 'Ripple':
            dfRP["Close"].plot(secondary_y = True, legend = True, ax = axx) # If the chosen cryptocurrency2 is ripple, create a second y axis and set it to ripple with data from dfRP

        if cryptocurrency2 == 'Ethereum':
            dfET["Close"].plot(secondary_y = True, legend = True, ax = axx) # If the chosen cryptocurrency2 is ethereum, create a second y axis and set it to ethereum with data from dfET
            
        if cryptocurrency1 == cryptocurrency2 == 'Bitcoin':
            dfBC["Close"].plot(legend = True, ax = axx) # If the chosen cryptocurrencies are the same, don't create a second y axis and don't add another line to the legend

        if cryptocurrency1 == cryptocurrency2 == 'Ethereum':
            dfET["Close"].plot(legend = True, ax = axx) # If the chosen cryptocurrencies are the same, don't create a second y axis and don't add another line to the legend

        if cryptocurrency1 == cryptocurrency2 == 'Ripple':
            dfRP["Close"].plot(legend = True, ax = axx) # If the chosen cryptocurrencies are the same, don't create a second y axis and don't add another line to the legend

        if cryptocurrency2 != 'None':
            axx.right_ax.set_ylabel(cryptocurrency2) # If the chosen cryptocurrency2 isn't none, create a second y axis for the second cryptocurrency. Without this line it will create a y axis and put the word none on it.
                 
        axx.set_ylabel(cryptocurrency1) # Set the first y axis to the first cryptocurrency's name.
        
        chart=plt_to_img(fig1) # Turns the graph into an image
        

    return render_template(
        'query.html',
         form1 = form1,
         chart = chart,
         height_case_1 = height_case_1 ,
         width_case_1 = width_case_1
        )
def plt_to_img(fig):  #The function that turns the graph into an image.
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String



