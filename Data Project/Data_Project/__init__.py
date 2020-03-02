"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = 1234

import Data_Project.views
