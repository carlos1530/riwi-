const apiUrl = 'http://localhost:3001/Productos';

const productoForm = document.getElementById('productoForm');
const productosUl = document.getElementById('productosUl');
productoForm.addEventListener('submit', async function (e) {
  e.preventDefault();

  const id = document.getElementById('productoId').value;
  const nombre = document.getElementById('productoNombre').value.trim();
  const precio = parseFloat(document.getElementById('productoPrecio').value);
  const descripcion = document.getElementById('productoDescripcion').value.trim();

  const producto = { nombre, precio, descripcion };

  try {
    if (!id) {
      // 🛑 Verificar si ya existe un producto con ese nombre
      const res = await fetch(`${apiUrl}?nombre=${encodeURIComponent(nombre)}`);
      const productosExistentes = await res.json();

      if (productosExistentes.length > 0) {
        alert('Ya existe un producto con ese nombre.');
        return;
      }

      // Crear nuevo producto
      await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(producto)
      });
    } else {
      // Actualizar producto
      await fetch(`${apiUrl}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
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

      const nombre = document.createElement('strong');
      nombre.textContent = producto.nombre;

      const precio = document.createElement('span');
      precio.textContent = ` - $${producto.precio}`;

      const descripcion = document.createElement('div');
      descripcion.innerHTML = `<em>${producto.descripcion}</em>`;

      const btnEditar = document.createElement('button');
      btnEditar.textContent = 'Editar';
      btnEditar.addEventListener('click', () => editarProducto(producto.id));

      const btnEliminar = document.createElement('button');
      btnEliminar.textContent = 'Eliminar';
      btnEliminar.addEventListener('click', () => eliminarProducto(producto.id));

      li.appendChild(nombre);
      li.appendChild(precio);
      li.appendChild(document.createElement('br'));
      li.appendChild(descripcion);
      li.appendChild(document.createElement('br'));
      li.appendChild(btnEditar);
      li.appendChild(btnEliminar);

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
  if (!confirm('¿Estás seguro de eliminar este producto?')) return;
  try {
    await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });
    cargarProductos();
  } catch (error) {
    console.error('Error al eliminar el producto:', error);
  }
}

// Cargar productos al iniciar la página
cargarProductos();
