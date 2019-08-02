import os
from configparser import ConfigParser


class BaseConfig(object):
    """
    Common configurations
    """
    TESTING = False
    DEBUG = False
    SECRET_KEY = "awesome nakatudde"


class TestingConfig(BaseConfig):
    """Configurations for Testing, with a separate test database."""
    MONGO_URI = 'mongodb://localhost/pymongo-test'
    TESTING = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """
    Development configurations
    """
    MONGO_URI = 'mongodb://localhost/pymongo'
    DEBUG = True

class ProductionConfig(BaseConfig):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
