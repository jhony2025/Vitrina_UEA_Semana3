# Vitrina UEA

**Proyecto Final / Semana 16 — Desarrollo de Aplicaciones Web**  
Universidad Estatal Amazónica  
**Autor:** Johnny Alberto Vera Vaca

## 1. Descripción del proyecto

Vitrina UEA es una aplicación web desarrollada con Flask para gestionar productos, clientes, proveedores y facturación. Utiliza PostgreSQL para almacenar la información y plantillas Jinja2 para presentar las páginas del sistema.

## 2. Objetivo

Desarrollar una aplicación web funcional que integre autenticación, operaciones CRUD, persistencia en una base de datos relacional y navegación entre sus secciones.

## 3. Tecnologías utilizadas

- Python
- Flask
- Flask-Login
- PostgreSQL
- psycopg2
- HTML5
- CSS3
- Bootstrap
- Jinja2
- JavaScript
- Git y GitHub
- Visual Studio Code

## 4. Funcionalidades implementadas

- Inicio de sesión y autenticación.
- Protección de rutas mediante `login_required`.
- Cierre de sesión.
- CRUD de productos.
- CRUD de clientes.
- CRUD de proveedores.
- Registro y consulta de facturas.
- Relación entre clientes y facturas.
- Relación entre facturas y detalle de factura.
- Relación entre detalle de factura y productos.
- Navegación entre las secciones del sistema.

## 5. Base de datos

El sistema utiliza PostgreSQL y las tablas `usuarios`, `categorias`, `productos`, `clientes`, `proveedores`, `facturas` y `detalle_factura`.

Relaciones entre tablas:

- `productos.categoria_id` → `categorias.id`
- `productos.proveedor_id` → `proveedores.id`
- `facturas.cliente_id` → `clientes.id`
- `detalle_factura.factura_id` → `facturas.id`
- `detalle_factura.producto_id` → `productos.id`

## 6. Estructura principal del proyecto

```text
Vitrina_UEA_Semana3/
├── app.py
├── conexion.py
├── README.md
├── static/
│   ├── imagenes/
│   ├── script.js
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── productos.html
    ├── registrar_producto.html
    ├── editar_producto.html
    ├── clientes.html
    ├── registrar_cliente.html
    ├── editar_cliente.html
    ├── proveedores.html
    ├── registrar_proveedor.html
    ├── editar_proveedor.html
    ├── facturacion.html
    └── registrar_factura.html
```

## 7. Pruebas realizadas

Se comprobó el inicio de sesión, la protección de rutas después del cierre de sesión, el CRUD de productos, clientes y proveedores, el registro de facturas, la consulta del detalle de factura, la navegación entre páginas y la conexión y consultas a PostgreSQL.

Como ejemplo de prueba de facturación: factura 1, cliente Johnny Vera, producto Camiseta UEA, cantidad 2, precio 25.00 y total 50.00.

## 8. Repositorio

[https://github.com/jhony2025/Vitrina_UEA_Semana3](https://github.com/jhony2025/Vitrina_UEA_Semana3)

## 9. Resultado final

El sistema se encuentra funcional para la demostración del Proyecto Final / Semana 16 de Desarrollo de Aplicaciones Web.

## 10. Autor

Johnny Alberto Vera Vaca  
Universidad Estatal Amazónica  
Desarrollo de Aplicaciones Web  
2026

## 11. Conclusión

Vitrina UEA evolucionó hasta convertirse en una aplicación web que integra Flask y PostgreSQL para gestionar información de manera organizada. La autenticación, las operaciones CRUD y las relaciones entre tablas conforman una base funcional para la demostración del Proyecto Final / Semana 16.
