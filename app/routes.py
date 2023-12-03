from flask import Blueprint, request, jsonify, render_template
from app.models import Producto

routes = Blueprint('routes', __name__)

# Ruta para mostrar los productos
@routes.route('/productos')
def mostrar_productos():
    productos = Producto.query.all()  # Obtener todos los productos de la base de datos
    return render_template('productos.html', productos=productos)

@routes.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    return jsonify([producto.__dict__ for producto in productos])


# Creación de un nuevo producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nuevo_producto = Producto(
        categoria=data['categoria'],
        nombre=data['nombre'],
        subcategoria=data['subcategoria'],
        tamano_cc=data['tamano_cc'],
        precio=data['precio']
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify({"mensaje": "Producto creado exitosamente"})

