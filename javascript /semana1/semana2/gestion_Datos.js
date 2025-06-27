console.log("Bienvenidos a nuestra gestion de Datos");
// 1. Objeto con productos
const productos = {
  1: { id: 1, nombre: 'Laptop', precio: 1500 },
  2: { id: 2, nombre: 'Teclado', precio: 100 },
  3: { id: 3, nombre: 'Mouse', precio: 50 }
};

const setProductos = new Set(Object.values(productos));


console.log('Contenido del Set:');
setProductos.forEach(producto => console.log(producto));


const categorias = new Map();
categorias.set('Tecnología', 'Laptop');
categorias.set('Accesorios', 'Teclado');
categorias.set('Periféricos', 'Mouse');

console.log('\n--- for...in (productos) ---');
for (let key in productos) {
  console.log(`ID: ${productos[key].id}, Nombre: ${productos[key].nombre}, Precio: $${productos[key].precio}`);
}

console.log('\n--- for...of (Set) ---');
for (let prod of setProductos) {
  console.log(prod);
}

console.log('\n--- forEach (Map) ---');
categorias.forEach((valor, clave) => {
  console.log(`Categoría: ${clave}, Producto: ${valor}`);
});

