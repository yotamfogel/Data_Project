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
    FirstName  = StringField('First Name:  ' , [validators.Length(min=1, max=10)])
    LastName   = StringField('Last Name:  ' , [validators.Length(min=1, max=25)])
    PhoneNum   = StringField('Phone Number:  ' , [validators.Length(min=9, max=10)])
    EmailAddr  = StringField('E-Mail:  ' , [validators.Email()])
    username   = StringField('Username:  ' ,  [validators.Length(min=1, max=10)])
    password   = PasswordField('Password:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')



