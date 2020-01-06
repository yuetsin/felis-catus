#!/usr/bin/env python


from consts import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['DEBUG'] = DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s/%s' % (
    DOMAIN_NAME, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)
