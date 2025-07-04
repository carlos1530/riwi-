# 🧾 Sistema de Gestión de Productos – Explicación del Código

Este proyecto permite gestionar productos de una tienda desde el navegador. Es una **aplicación CRUD** (Crear, Leer, Actualizar, Eliminar) hecha con:

- HTML para la estructura
- CSS para el estilo visual
- JavaScript para la lógica
- JSON Server para guardar los productos como una base de datos falsa (API local)

---

## 📂 Archivos principales

### 1. `index.html` – La Interfaz

Contiene el formulario para crear/editar productos y una lista donde se muestran todos los productos.

- `<form id="productoForm">`: Permite agregar o actualizar productos.
- `<ul id="productosUl">`: Aquí se cargan todos los productos usando JavaScript.
- `<script src="app.js">`: Conecta con el archivo JavaScript donde está toda la lógica.

---

### 2. `style.css` – Estilos Visuales

Aplica formato a la página, incluyendo:

- Colores de fondo y bordes
- Espaciado entre elementos
- Estilos para botones y formularios

---

### 3. `app.js` – Lógica del CRUD

#### 🔗 Conexión con la API
```js
const apiUrl = 'http://localhost:3001/Productos';

Usamos esta URL para hacer peticiones a la base de datos JSON Server. 


""" Enviar Datos del formulario """
    productoForm.addEventListener('submit', async function (e) {    
    e.preventDefault();
  ...
    if (id) {
        // PUT: Actualizar producto existente
    } else {
        // POST: Crear nuevo producto
    }
    });

*Si el campo oculto productoId tiene un valor, se hace una petición PUT (editar).

*Si no tiene valor, se hace una POST (crear nuevo).

"""Mostar Productos"""
async function cargarProductos() {
    const res = await fetch(apiUrl);
    const productos = await res.json();
  ...
}
* Se obtienen todos los productos con GET y se muestran como <li> en la lista.


"""Editar Productos"""
async function editarProducto(id) {
    const res = await fetch(`${apiUrl}/${id}`);
    const producto = await res.json();
// Rellena el formulario con los datos del producto
}
* Cuando haces clic en “Editar”, se llenan los campos del formulario con los datos del producto.


"""Eliminar Producto"""
async function eliminarProducto(id) {
    await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });
    cargarProductos();
}
* Al confirmar, se hace una petición DELETE para quitar el producto.





"""🧪 ¿Qué hace cada parte?"""

Archivo	Función Principal

index.html --->	Muestra el formulario y la lista de productos
style.css --->	Da formato visual a la app
app.js --->	Conecta con la API y maneja toda la lógica
db.json	---> Simula la base de datos (API)