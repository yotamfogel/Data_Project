from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired

class QueryFormStructure(FlaskForm):
    name   = StringField('Country Name:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')



class LoginFormStructure(FlaskForm):
    username   = StringField('Username:  ' , validators = [DataRequired()])
    password   = PasswordField('Password:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')

class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First Name:  ' , validators = [DataRequired()])
    LastName   = StringField('Last Name:  ' , validators = [DataRequired()])
    PhoneNum   = StringField('Phone Number:  ' , validators = [DataRequired()])
    EmailAddr  = StringField('E-Mail:  ' , validators = [DataRequired()])
    username   = StringField('Username:  ' , validators = [DataRequired()])
    password   = PasswordField('Password:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')



