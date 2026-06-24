# 🛍️ Vitrina UEA - Proyecto Integrador

## 📌 Descripción
Este proyecto corresponde a la asignatura **Desarrollo de Aplicaciones Web (UEA)** y representa la evolución del trabajo realizado en la **Semana 3**, ahora mejorado en la **Semana 4** mediante la implementación de **CSS3, diseño responsivo y Bootstrap**.

El objetivo del proyecto es crear una plataforma digital para promocionar emprendimientos de moda local, permitiendo mostrar productos, información y contacto de manera organizada y moderna.

---

# 🔄 Evolución del Proyecto (Semana 3 → Semana 4)

## 🟡 1. Estructura original conservada (Semana 3)
Se mantuvo la estructura semántica original del proyecto:

- `<header>`
- `<nav>`
- `<main>`
- `<section>`
- `<article>`
- `<aside>`
- `<footer>`

✔ Esto permite conservar la base del proyecto y cumplir con la continuidad solicitada por el docente.

---

## 🟢 2. Mejora del diseño con Bootstrap
Se integró el framework:

```html
Bootstrap 5
```

### ✔ Cambios realizados:

- Navbar responsiva con menú colapsable

- Sistema de grillas (`container`, `row`, `col`)

- Tarjetas (cards) para servicios

- Botones estilizados

- Formularios con diseño profesional

- Imágenes responsivas (`img-fluid`)

---

## 🔵 3. Mejora de la sección Inicio

### Antes:

- Texto simple sin diseño

### Ahora:

- Sección centrada

- Fondo diferenciado

- Mejor jerarquía visual

✔ Mejora en presentación y experiencia del usuario

---

## 🟣 4. Quiénes Somos optimizado

### Antes:

- Texto largo sin estructura visual

### Ahora:

- Distribución en dos columnas (texto + imagen)

- Imagen responsiva

- Mejor lectura del contenido

---

## 🟠 5. Productos mejorados

### Antes:

- Lista HTML simple (``)

### Ahora:

- Tarjetas Bootstrap (cards)

- Distribución en grid responsivo

- Diseño más moderno y profesional

---

## 🔴 6. Contacto mejorado

### Antes:

- Información en texto plano

### Ahora:

- Formulario funcional con Bootstrap

- Información organizada en columnas

- Mejor accesibilidad visual

---

## 🟤 7. Multimedia mejorada

- Video incrustado con formato responsivo (`ratio 16x9`)

- Mejor adaptación a dispositivos móviles

---

## ⚫ 8. Diseño responsivo (CSS3)

Se implementó:

- Media queries

- Adaptación a pantallas pequeñas

- Tipografía y espaciado mejorado

- Sombras y efectos hover

---

# 🧠 Tecnologías utilizadas

- HTML5

- CSS3

- Bootstrap 5

- Diseño responsivo

- Flexbox y Grid (Bootstrap)

---

# 🎯 Objetivo alcanzado

✔ Transformar un sitio web básico (Semana 3) en una interfaz moderna y responsiva
✔ Aplicar Bootstrap correctamente
✔ Mejorar la experiencia de usuario
✔ Mantener la estructura original del proyecto

---

# 👨‍🎓 Autor

**Johnny Alberto Vera Vaca**
Desarrollo de Aplicaciones Web - UEA
2026

---

# 🚀 Instrucciones de uso

1. Clonar el repositorio

2. Abrir `index.html`

3. Visualizar en navegador

4. (Opcional) Publicar en GitHub Pages

# Proyecto Integrador U2 - Avance 1: Fundamentos de JavaScript, DOM y Eventos

## Universidad Estatal Amazónica (UEA)

**Asignatura:** Desarrollo de Aplicaciones Web
**Estudiante:** Johnny Alberto Vera Vaca
**Semana:** 5
**Año:** 2026

---

# Descripción del Proyecto

Este proyecto corresponde al Avance 1 del Proyecto Integrador de la Unidad 2 de la asignatura Desarrollo de Aplicaciones Web. Su objetivo es incorporar funcionalidades dinámicas mediante JavaScript, aplicando manipulación del DOM y manejo de eventos sobre una página web desarrollada previamente con HTML5, CSS3 y Bootstrap.

La aplicación está orientada al proyecto **Vitrina UEA**, una plataforma web destinada a la promoción de prendas de vestir y emprendimientos locales. En esta versión se implementó un sistema de registro dinámico de productos que permite agregar, visualizar, contabilizar y eliminar registros sin necesidad de recargar la página.

---

# Objetivos

## Objetivo General

Implementar funcionalidades dinámicas utilizando JavaScript para manipular elementos del DOM y gestionar eventos dentro de una aplicación web interactiva.

## Objetivos Específicos

* Utilizar JavaScript para capturar información ingresada por el usuario.
* Aplicar validaciones básicas en formularios.
* Manipular el DOM mediante la creación y eliminación dinámica de elementos.
* Gestionar eventos utilizando addEventListener().
* Mostrar información actualizada en tiempo real sin recargar la página.
* Aplicar componentes y estilos responsivos mediante Bootstrap.

---

# ¿Qué es JavaScript?

JavaScript es un lenguaje de programación de alto nivel que permite agregar interactividad y comportamiento dinámico a las páginas web. Fue creado inicialmente para ejecutarse en navegadores web y complementar las funcionalidades de HTML y CSS.

Actualmente JavaScript es uno de los lenguajes más utilizados en el desarrollo de aplicaciones web debido a su capacidad para responder a las acciones del usuario, modificar contenido de manera dinámica y comunicarse con servidores.

Entre sus principales características se encuentran:

* Lenguaje interpretado.
* Compatible con todos los navegadores modernos.
* Permite programación orientada a objetos y funcional.
* Facilita la creación de interfaces interactivas.
* Puede utilizarse tanto en el cliente como en el servidor mediante Node.js.

---

# ¿Qué es el DOM?

El DOM (Document Object Model) es una representación estructurada de una página HTML en forma de árbol de objetos.

Gracias al DOM, JavaScript puede:

* Acceder a elementos HTML.
* Modificar contenido y estilos.
* Crear nuevos elementos.
* Eliminar elementos existentes.
* Responder a eventos generados por el usuario.

El DOM constituye el puente de comunicación entre JavaScript y la página web.

---

# Funcionalidades Implementadas

La aplicación desarrollada incorpora las siguientes funcionalidades:

### Registro dinámico de productos

Permite ingresar:

* Nombre del producto.
* Descripción.
* Categoría.

### Validación de datos

Antes de registrar un producto se verifica que todos los campos estén completos.

### Creación dinámica de elementos

Los productos registrados se generan automáticamente mediante JavaScript utilizando createElement().

### Contador de registros

La aplicación mantiene actualizado el número total de productos registrados.

### Eliminación de registros

Cada producto posee un botón que permite eliminarlo dinámicamente mediante eventos de clic.

### Diseño responsivo

La interfaz utiliza Bootstrap para garantizar una correcta visualización en computadoras, tabletas y dispositivos móviles.

---

# Tecnologías Utilizadas

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Git
* GitHub
* GitHub Pages

---

# Estructura del Proyecto

DESARROLLO DE PAGINA WEB

├── index.html
├── script.js
├── README.md
└── carpeta de imágenes

---

# Conclusión

El desarrollo de esta actividad permitió aplicar los fundamentos de JavaScript para crear una página web interactiva capaz de responder a las acciones del usuario sin necesidad de recargar el navegador. Además, se fortalecieron los conocimientos sobre manipulación del DOM, manejo de eventos y validación de formularios, elementos fundamentales para el desarrollo de aplicaciones web modernas y para la futura integración con tecnologías del lado del servidor como Flask.
