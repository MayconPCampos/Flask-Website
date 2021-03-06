from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = False
    MYSQL_HOST = os.environ.get("MYSQL_HOST")
    MYSQL_USER = os.environ.get("MYSQL_USER")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    MYSQL_DB = os.environ.get("MYSQL_DB")

class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = "development"
    NEWS_IMAGES = "C:/Users/mayco/Programing/portfolio/Website Flask/app/static/images/news"
