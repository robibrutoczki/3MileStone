import os
from os import path
from datetime import datetime
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, request, url_for
if path.exists("env.py"):
    import env

app = Flask(__name__)
SECRET_KEY = os.environ.get('SECRET_KEY')
print(SECRET_KEY)