#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class CrimeRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    reporter = db.Column(db.String(100), nullable=False)
    suspect = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)



class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)


class Cases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
