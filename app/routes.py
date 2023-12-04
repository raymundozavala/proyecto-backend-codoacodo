from flask import Blueprint, request, jsonify, render_template

from app import db


routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    return render_template('index.html')


@routes.route('/vinos')
def mostrar_productos():
    productos = Producto.query.all()  # Obtener todos los productos de la base de datos
    return render_template('vino.html', productos=productos)


@routes.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    return jsonify([producto.__dict__ for producto in productos])


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