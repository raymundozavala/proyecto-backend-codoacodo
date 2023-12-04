# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    subcategoria = db.Column(db.String(100))
    tamano_cc = db.Column(db.Integer)
    precio = db.Column(db.Float)

    def __repr__(self):
        return f"Producto: {self.nombre}"