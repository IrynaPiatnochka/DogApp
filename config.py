import os
from dotenv import load_dotenv

load_dotenv()

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/dogs_db'
    CACHE_TYPE = "Simple_Cache"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True