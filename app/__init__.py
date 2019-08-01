from flask import Flask
from .config import app_config

app = Flask (__name__, instance_relative_config = True)
app.config.from_object(app_config["development"])