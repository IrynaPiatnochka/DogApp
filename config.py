import os
from dotenv import load_dotenv
import pyodbc 
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

class Config:
    FLASK_APP = os.getenv("FLASK_APP")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    CACHE_TYPE = os.getenv("CACHE_TYPE", "SimpleCache")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    DEBUG = os.getenv("DEBUG") == 'True'
    
    # Mail configuration
    MAIL_DEBUG = os.getenv("MAIL_DEBUG") == 'True' 
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))  
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "True") == "True"  
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

class DevelopmentConfig(Config):
    pass 

class ProductionConfig(Config):
    DEBUG = False  

def create_db_connection():
    if os.getenv('DB_ENV') == 'cloud':
        conn_str = (
            f"Driver={{ODBC Driver 18 for SQL Server}};"
            f"Server={os.getenv('DB_HOST')};"
            f"Database={os.getenv('DB_DATABASE')};"
            f"UID={os.getenv('DB_USERNAME')};"
            f"PWD={os.getenv('DB_PASSWORD')};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=yes;"
            f"Connection Timeout=30;"
        )
    else:
        # Local connection 
        conn_str = (
            f"mysql+mysqlconnector://{os.getenv('LOCAL_DB_USERNAME')}:{os.getenv('LOCAL_DB_PASSWORD')}@"
            f"{os.getenv('LOCAL_DB_HOST')}/{os.getenv('LOCAL_DB_DATABASE')}"
        )
    return pyodbc.connect(conn_str)

db = SQLAlchemy()
