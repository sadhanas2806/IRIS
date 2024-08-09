from flask import Flask,render_template,request
from flask_session import Session
import os,time
import datetime
from datetime import timedelta,date,datetime
import traceback
import logging

app = Flask(__name__)


app.config.from_object('core.config.SECRET_KEY')
app.config.from_object('core.config.ProductionConfig')

Session(app)

config = app.config



current_app = app


from core.controller.IrisController import app as Iris
app.register_blueprint(Iris, url_prefix='')
