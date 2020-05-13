from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField , HiddenField , DateTimeField , IntegerField , DecimalField , FloatField , RadioField
from wtforms import Form, SelectMultipleField , BooleanField
from wtforms import TextField, TextAreaField, SelectField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired
from wtforms.validators import InputRequired


class CryptoForm(FlaskForm):
    cryptocurrency1 = SelectField('Cryptocurrency 1' , validators = [DataRequired()] , choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('Ripple', 'Ripple')]) # Makes a new input field on the query page with a predetermined selection
    cryptocurrency2 = SelectField('Cryptocurrency 2' , validators = [DataRequired()] , choices=[('Bitcoin', 'Bitcoin'), ('Ethereum', 'Ethereum'), ('Ripple', 'Ripple'), ('None', 'None')]) # Makes a new input field on the query page with a predetermined selection
    start_date = DateField('Start Date' , format='%Y-%m-%d' , validators = [DataRequired()]) # Makes a new input field on the query page with a limited date range to pick from, this will be our start date
    end_date = DateField('End Date' , format='%Y-%m-%d' , validators = [DataRequired()]) # Makes a new input field on the query page with a limited date range to pick from, this will be our end date
    kind = SelectField('Chart Kind' , validators = [DataRequired()] , choices=[('Line', 'Line'), ('Bar', 'Bar')]) # Delete this it's useless
    subnmit = SubmitField('Display') # Sumbit button



