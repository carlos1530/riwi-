const express = require('express');
const app = express();
const port = 3000;
const db = require('./db');

app.use(express.json());

// Endpoint para obtener todos los estudiantes
app.get('/estudiantes', (req, res) => {
    db.query('SELECT * FROM estudiantes', (err, results) => {
        if (err) {
            return res.status(500).json({ error: err });
        }
        res.json(results);
    });
});

app.listen(port, () => {
    console.log(`Servidor corriendo en http://localhost:${port}`);
});
