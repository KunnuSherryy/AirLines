from flask import Flask, request, render_template, Blueprint, session
from app2 import view
from auth import auth_bp
import os
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    load_dotenv()
    SECRET_KEY = os.getenv("SECRET_KEY")
    app.secret_key = SECRET_KEY

    #registering the blueprints
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/')
    return app
