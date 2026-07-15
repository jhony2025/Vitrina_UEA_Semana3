# Vitrina UEA

## Avance del proyecto final - Componente práctico experimental

Este repositorio contiene un avance práctico y experimental del proyecto final para el curso, diseñado como una vitrina digital de emprendimientos de moda local. La entrega actual adapta y mejora el diseño y la funcionalidad solicitados por el docente.

## Resumen del proyecto

Vitrina UEA es una página web estática que reúne secciones de presentación, información de la propuesta, espacios para tiendas destacadas y un registro dinámico de productos. El diseño se construyó con Bootstrap para garantizar una presentación responsiva y con JavaScript para que el contenido pueda manejarse de forma interactiva.

## Qué se incorporó según lo solicitado

- Se restauró y reconstruyó el archivo `index.html` con una estructura clara de secciones: Inicio, Quiénes Somos, Servicios y Productos, Registro, Contacto y lista dinámica.
- Se incorporó una barra de navegación fija, anclas internas y un encabezado visual moderno con Bootstrap.
- Se agregó una sección de tiendas con tarjetas de imágenes más altas y verticales, mejorando el encuadre para no cortar rostros.
- Se incluyó una sección de registro de productos con formulario validado, spinner visual y generación dinámica de la tabla de resultados.
- En JavaScript se mantuvo y mejoró la lógica para crear productos, mostrar mensajes de alerta y borrar elementos con confirmación.
- Se emplearon alertas, modal y spinner para cumplir los requerimientos de interactividad y feedback visual.
- Se aplicaron estilos personalizados en `style.css` para dar más presencia al contenido, mejorar el contraste y mantener el sitio responsive.

## Explicación del código anterior y su evolución

- `index.html`: Organiza la interfaz en secciones semánticas y usa clases Bootstrap para layout responsivo. Contiene también el markup para el modal de confirmación y una cubierta de video que puede reemplazarse en versiones posteriores.
- `style.css`: Añade reglas de estilo propias para el diseño general, tarjetas, imágenes y comportamiento visual. En la última iteración, se ajustaron las imágenes de las tarjetas para que sean más altas y verticales sin ampliar demasiado el ancho.
- `script.js`: Controla la interacción del usuario al registrar productos. Valida el formulario, muestra mensajes temporales, agrega filas a la tabla y permite eliminar productos.

## Resultado del avance

Este avance demuestra que el proyecto ya cuenta con:

- una interfaz de usuario funcional y mejorada,
- una lógica dinámica con JavaScript,
- componentes visuales solicitados por el docente (alertas, modal, spinner, tarjetas verticales),
- y una base sólida para continuar con el desarrollo del proyecto final.

## Archivos principales

- `index.html`: página principal y estructura del sitio.
- `style.css`: estilos personalizados y ajustes visuales.
- `script.js`: lógica de registro dinámico y manejo de interfaz.
- `imagenes/`: recursos gráficos utilizados.

## Instrucciones de uso

1. Clonar o descargar el repositorio.
2. Abrir `index.html` en un navegador.
3. Navegar por las secciones y probar el registro de productos.
4. Revisar los cambios en `style.css` y `script.js` para adaptar la lógica en futuras entregas.

## Estructura del proyecto

```
VITRINA_UEA_SEMANA3
│
├── index.html
├── style.css
├── script.js
├── README.md
└── imagenes/
    ├── moda.jpg.avif
    ├── moda2.jpg.avif
    ├── moda3.jpg.avif
    └── otras imágenes relacionadas
```

## Tecnologías utilizadas

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Autor

Johnny Alberto Vera Vaca

Universidad Estatal Amazónica

Tecnología de la Información

2026