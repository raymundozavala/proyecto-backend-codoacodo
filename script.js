// Función para cargar los datos desde el archivo JSON usando Fetch API
function cargarDatos() {
    // Ruta del archivo JSON
    const url = 'productos.json';
  
    // Realizar la solicitud Fetch
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error(`Error al cargar el archivo JSON: ${response.status}`);
        }
        return response.json();
      })
      .then(productos => {
        // Llamar a la función para actualizar el HTML con los datos cargados
        actualizarHTML(productos);
      })
      .catch(error => {
        console.error('Error de Fetch:', error);
      });
  }
  
  // Función para actualizar el HTML con los datos del archivo JSON
  function actualizarHTML(productos) {
    // Supongamos que tienes un elemento div con el id "lista-productos" en tu HTML
    const listaProductos = document.getElementById('lista-productos');
  
    // Crear elementos HTML para cada producto y agregarlos al div
    productos.forEach(producto => {
        console.log("llega hasta acá");
      const productoElement = document.createElement('div');
      productoElement.textContent = `${producto.nombre}: $${producto.precio}`;
      listaProductos.appendChild(productoElement);
    });
  }
  
  // Llamar a la función para cargar los datos cuando se carga la página
  cargarDatos();