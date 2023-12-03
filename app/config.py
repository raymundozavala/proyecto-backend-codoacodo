import os
from os import environ

DEBUG = True

# Configuración de la base de datos local MySQL
DB_USERNAME = 'cacgrupo5'
DB_PASSWORD = 'Paste2023*'
DB_HOST = 'localhost'
# DB_HOST = cacgrupo5.mysql.pythonanywhere-services.com
DB_NAME = 'productos_db'
# DB_NAME = 'cacgrupo5$default'

# Cadena de conexión para MySQL
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False