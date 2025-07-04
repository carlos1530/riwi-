// URL base de tu API (nota la P mayúscula)
const apiUrl = 'http://localhost:3000/Productos';

const productoForm = document.getElementById('productoForm');
const productosUl = document.getElementById('productosUl');

productoForm.addEventListener('submit', async function (e) {
  e.preventDefault();

  const id = document.getElementById('productoId').value;
  const nombre = document.getElementById('productoNombre').value;
  const precio = parseFloat(document.getElementById('productoPrecio').value);
  const descripcion = document.getElementById('productoDescripcion').value;

  const producto = { nombre, precio, descripcion };

  try {
    if (id) {
      // Actualizar producto
      await fetch(`${apiUrl}/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(producto)
      });
    } else {
      // Crear nuevo producto
      await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(producto)
      });
    }

    productoForm.reset();
    document.getElementById('productoId').value = '';
    cargarProductos();
  } catch (error) {
    console.error('Error al guardar el producto:', error);
  }
});

async function cargarProductos() {
  try {
    const res = await fetch(apiUrl);
    const productos = await res.json();

    productosUl.innerHTML = '';

    productos.forEach(producto => {
      const li = document.createElement('li');
      li.innerHTML = `
        <strong>${producto.nombre}</strong> - $${producto.precio}<br>
        <em>${producto.descripcion}</em><br>
        <button onclick="editarProducto(${producto.id})">Editar</button>
        <button onclick="eliminarProducto(${producto.id})">Eliminar</button>
      `;
      productosUl.appendChild(li);
    });
  } catch (error) {
    console.error('Error al cargar productos:', error);
  }
}

async function editarProducto(id) {
  try {
    const res = await fetch(`${apiUrl}/${id}`);
    const producto = await res.json();

    document.getElementById('productoId').value = producto.id;
    document.getElementById('productoNombre').value = producto.nombre;
    document.getElementById('productoPrecio').value = producto.precio;
    document.getElementById('productoDescripcion').value = producto.descripcion;
  } catch (error) {
    console.error('Error al obtener el producto:', error);
  }
}

async function eliminarProducto(id) {
  try {
    await fetch(`${apiUrl}/${id}`, {
      method: 'DELETE'
    });
    cargarProductos();
  } catch (error) {
    console.error('Error al eliminar el producto:', error);
  }
}

// Cargar productos al iniciar la página
cargarProductos();
