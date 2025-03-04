import os
from sqlalchemy import create_engine
import urllib

"""
conexion base de datos
"""
class Config(object):
    SECRET_KEY = 'Clave secreta'
    SESION_COOKIES_SECURE = False




class  DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Rocha3107__@localhost:3306/bdidgs803'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
