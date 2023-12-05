import json
from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from marshmallow import Schema, fields

# Importar configuración
from config import SQLALCHEMY_DATABASE_URI

# Crear la aplicación Flask
app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la extensión SQLAlchemy
db = SQLAlchemy(app)

# Habilitar CORS
CORS(app)

# Definir la clase Producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    subcategoria = db.Column(db.String(100))
    tamano_cc = db.Column(db.Integer)
    precio = db.Column(db.Float)

    def __repr__(self):
        return f"Producto: {self.nombre}"

# Definir las rutas
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/vinos')
def mostrar_productos():
    productos = Producto.query.all()  # Obtener todos los productos de la base de datos
    return render_template('vino.html', productos=productos)

@app.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    return jsonify({
        'productos': [
            {
                'id': producto.id,
                'categoria': producto.categoria,
                'nombre': producto.nombre,
                'subcategoria': producto.subcategoria,
                'tamano_cc': producto.tamano_cc,
                'precio': producto.precio
            }
            for producto in productos
        ]
    })

@routes.route('/productos', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nuevo_producto = Producto(
        id=data['id'],
        categoria=data['categoria'],
        nombre=data['nombre'],
        subcategoria=data['subcategoria'],
        tamano_cc=data['tamano_cc'],
        precio=data['precio']
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify({"mensaje": "Producto creado exitosamente"})

@routes.route('/productos/<int:producto_id>', methods=['PUT'])
def modificar_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    data = request.get_json()

    producto.categoria = data.get('categoria', producto.categoria)
    producto.nombre = data.get('nombre', producto.nombre)
    producto.subcategoria = data.get('subcategoria', producto.subcategoria)
    producto.tamano_cc = data.get('tamano_cc', producto.tamano_cc)
    producto.precio = data.get('precio', producto.precio)

    db.session.commit()
    return jsonify({"mensaje": "Producto modificado exitosamente"})

@routes.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)

    db.session.delete(producto)
    db.session.commit()

    return jsonify({"mensaje": "Producto eliminado exitosamente"})

# Registrar las rutas
app.register_blueprint(routes)

# Iniciar la aplicación si se ejecuta este archivo directamente
if __name__ == '__main__':
    app.run(debug=True)