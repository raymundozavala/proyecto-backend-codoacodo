from flask import Flask, render_template
from flask_cors import CORS
from app.routes import routes  # Importa las rutas desde el archivo routes.py

app = Flask(__name__)
CORS(app)

# Resto de configuraciones...

app.register_blueprint(routes)  # Registra las rutas en la aplicación Flask

# Rutas y funciones para manejar las solicitudes HTTP
@app.route('/')
def index():
    return render_template('index.html')

# Resto de rutas y funciones...

if __name__ == "__main__":
    app.run(debug=True)
