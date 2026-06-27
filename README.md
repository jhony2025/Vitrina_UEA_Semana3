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

## Continuidad del Proyecto

Este proyecto corresponde a la continuación del trabajo desarrollado en la Semana 4, donde se diseñó la estructura de la página web utilizando HTML5, CSS3 y Bootstrap. En la Semana 5 se incorporaron funcionalidades dinámicas mediante JavaScript, aplicando manipulación del DOM, validación de formularios y manejo de eventos, fortaleciendo la interactividad de la aplicación web.