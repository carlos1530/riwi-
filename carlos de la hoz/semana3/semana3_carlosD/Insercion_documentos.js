// ----- COLECCIÓN: usuarios -----
db.usuarios.insertMany([
  {
    nombre: "Carlos De la Hoz",
    correo: "carlos@example.com",
    pais: "Colombia",
    generos_preferidos: ["Acción", "Comedia"],
    historial_visualizacion: [
      { contenido_id: ObjectId(), fecha: ISODate("2025-08-01T20:00:00Z"), minutos_vistos: 120 }
    ]
  },
  {
    nombre: "Ana Torres",
    correo: "ana@example.com",
    pais: "México",
    generos_preferidos: ["Drama", "Romance"],
    historial_visualizacion: [
      { contenido_id: ObjectId(), fecha: ISODate("2025-07-20T18:00:00Z"), minutos_vistos: 90 },
      { contenido_id: ObjectId(), fecha: ISODate("2025-07-22T19:30:00Z"), minutos_vistos: 100 }
    ]
  }
]);

// ----- COLECCIÓN: peliculas -----
db.peliculas.insertMany([
  {
    titulo: "Inception",
    duracion_min: 148,
    anio_lanzamiento: 2010,
    generos: ["Ciencia Ficción", "Acción"],
    reparto: ["Leonardo DiCaprio", "Elliot Page"],
    valoraciones: [
      { usuario_id: ObjectId(), calificacion: 5, comentario: "Excelente película" }
    ]
  },
  {
    titulo: "Titanic",
    duracion_min: 195,
    anio_lanzamiento: 1997,
    generos: ["Drama", "Romance"],
    reparto: ["Leonardo DiCaprio", "Kate Winslet"],
    valoraciones: [
      { usuario_id: ObjectId(), calificacion: 4, comentario: "Muy emotiva" }
    ]
  }
]);

// ----- COLECCIÓN: series -----
db.series.insertOne({
  titulo: "Stranger Things",
  temporadas: 4,
  episodios: [
    {
      titulo: "Capítulo Uno",
      duracion_min: 50,
      valoraciones: [
        { usuario_id: ObjectId(), calificacion: 4, comentario: "Muy intrigante" }
      ]
    },
    {
      titulo: "Capítulo Dos",
      duracion_min: 52,
      valoraciones: []
    }
  ]
});

// ----- COLECCIÓN: listas_reproduccion -----
db.listas_reproduccion.insertOne({
  usuario_id: ObjectId(),
  nombre_lista: "Mis Favoritas",
  fecha_creacion: ISODate("2025-07-15T18:30:00Z"),
  contenidos: [
    { contenido_id: ObjectId(), tipo: "pelicula" },
    { contenido_id: ObjectId(), tipo: "serie" }
  ]
});

// =======================
// CONSULTAS BÁSICAS
// =======================

// Películas con duración mayor a 120 minutos
db.peliculas.find({ duracion_min: { $gt: 120 } });

// Usuarios que vieron más de 1 contenido
db.usuarios.find({ $expr: { $gt: [ { $size: "$historial_visualizacion" }, 1 ] } });

// Películas del género Acción (usando regex)
db.peliculas.find({ generos: { $regex: /Acción/i } });

// =======================
// ACTUALIZACIONES Y ELIMINACIONES
// =======================

// Agregar una nueva valoración a "Inception"
db.peliculas.updateOne(
  { titulo: "Inception" },
  { $push: { valoraciones: { usuario_id: ObjectId(), calificacion: 5, comentario: "Me encantó" } } }
);

// Eliminar la lista "Mis Favoritas"
db.listas_reproduccion.deleteOne({ nombre_lista: "Mis Favoritas" });

// =======================
// ÍNDICES
// =======================

// Crear índice en el título de películas
db.peliculas.createIndex({ titulo: 1 });

// Consultar índices
db.peliculas.getIndexes();

// =======================
// AGREGACIONES
// =======================

// Promedio de calificación por película
db.peliculas.aggregate([
  { $unwind: "$valoraciones" },
  { $group: { _id: "$titulo", promedio_calificacion: { $avg: "$valoraciones.calificacion" } } }
]);

// Número total de contenidos vistos por usuario
db.usuarios.aggregate([
  { $project: { nombre: 1, total_vistos: { $size: "$historial_visualizacion" } } }
]);

// Géneros más populares en películas
db.peliculas.aggregate([
  { $unwind: "$generos" },
  { $group: { _id: "$generos", total: { $sum: 1 } } },
  { $sort: { total: -1 } }
]);
