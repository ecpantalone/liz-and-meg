import os
from flask import Flask
from flask_mail import Mail
import logging
from config import Config
from logging.handlers import RotatingFileHandler


app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)

if not app.debug:
  if not os.path.exists('logs'):
      os.mkdir('logs')
      file_handler = RotatingFileHandler('logs/liz-and-meg.log', maxBytes=10240,
                                        backupCount=10)
      file_handler.setFormatter(logging.Formatter(
          '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
      file_handler.setLevel(logging.DEBUG)
      app.logger.addHandler(file_handler)

      app.logger.setLevel(logging.DEBUG)
      app.logger.info('Liz & Meg startup')
from app import routes