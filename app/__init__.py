import os
from flask import Flask
from flask_mail import Mail, Message
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)

from app import routes