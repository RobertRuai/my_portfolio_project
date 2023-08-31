#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://{}:{}@{}/{}'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB)
db = SQLAlchemy(app)
