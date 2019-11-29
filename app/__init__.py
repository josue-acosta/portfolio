from flask import Flask

# app congfigurations
app = Flask(__name__, static_url_path='/static')

#-- app environment
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

# import views
from app import views
