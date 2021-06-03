from flask import Flask
from os import path

def createapp():
    app = Flask(__name__)
    app.config['SECRET_KEY']='abcdefg'
    from .views import views
    app.register_blueprint(views, url_prefix='/')
	
    return app




