from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from models import Producto
from routes import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Inicializar la extensión SQLAlchemy
db = SQLAlchemy(app)

# Importar rutas
app.register_blueprint(routes)

# Iniciar la aplicación si se ejecuta este archivo directamente
if __name__ == '__main__':
    app.run(debug=True)