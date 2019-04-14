import os

from sayhello import app



DEBUG = True

# SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = os.getenv('password')
HOST = os.getenv('host')
PORT = os.getenv('port')
DATABASE = 'sayhello'

SECRET_KEY = os.getenv('SECRET_KEY','secret string')
SQLALCHEMY_DATABASE_URI = r"{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

print(HOST,PORT,PASSWORD)