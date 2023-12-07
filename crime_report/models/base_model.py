#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class CrimeReport(db.Model):
    crime_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    reporter = db.Column(db.String(100), nullable=False)
    suspect = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    crime_type = db.Column(db.String(100), nullable=False)


class Suspect(db.Model):
    suspect_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    crime_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
