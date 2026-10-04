CREATE TABLE categorias (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100)
);

CREATE TABLE proveedores (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100)
);

CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    imagen VARCHAR(255),
    categoria_id INTEGER REFERENCES categorias(id),
    proveedor_id INTEGER REFERENCES proveedores(id)
);

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE facturas (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES clientes(id),
    fecha TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    total NUMERIC(10, 2) NOT NULL,
    estado VARCHAR(30) NOT NULL DEFAULT 'Pendiente'
);

CREATE TABLE detalle_factura (
    id SERIAL PRIMARY KEY,
    factura_id INTEGER NOT NULL REFERENCES facturas(id),
    producto_id INTEGER NOT NULL REFERENCES productos(id),
    cantidad INTEGER NOT NULL,
    precio NUMERIC(10, 2) NOT NULL
);
