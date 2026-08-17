# <div align="center"><font color="#1565C0">VITRINA UEA</font></div>

## <div align="center"><font color="#2E7D32">Plataforma Web para la Promoción de Emprendimientos de Moda Local</font></div>

<div align="center">

**Proyecto Integrador**
**Desarrollo de Aplicaciones Web**
**Universidad Estatal Amazónica**

**Tecnología utilizada: Python y Flask**

</div>

---

# <font color="#1565C0">1. DESCRIPCIÓN DEL PROYECTO</font>

**Vitrina UEA** es una aplicación web desarrollada con el propósito de presentar y organizar información relacionada con emprendimientos de moda local.

El proyecto inició como una página web desarrollada con HTML, CSS y JavaScript. Posteriormente, se realizó una adaptación progresiva utilizando el framework **Flask**, permitiendo transformar el sitio web estático en una aplicación web estructurada mediante rutas, plantillas HTML y archivos estáticos.

La aplicación permite navegar entre diferentes secciones mediante rutas administradas por Flask. Cada sección utiliza una plantilla HTML independiente y comparte una estructura general mediante la plantilla `base.html`.

El proyecto utiliza una organización basada en la separación de responsabilidades entre:

* Aplicación y rutas desarrolladas en Python.
* Plantillas HTML administradas mediante Jinja2.
* Archivos CSS y JavaScript almacenados en la carpeta `static`.
* Imágenes utilizadas por las diferentes páginas.
* Entorno virtual de Python para administrar las dependencias del proyecto.

---

# <font color="#2E7D32">2. OBJETIVO DEL PROYECTO</font>

## <font color="#388E3C">Objetivo general</font>

Desarrollar una aplicación web utilizando Flask que permita organizar y presentar información de una plataforma digital orientada a la promoción de productos y emprendimientos de moda local.

## <font color="#388E3C">Objetivos específicos</font>

1. Configurar un proyecto web utilizando Python y Flask.

2. Crear y administrar rutas mediante el decorador `@app.route()`.

3. Utilizar plantillas HTML mediante `render_template()`.

4. Implementar una plantilla base reutilizable mediante Jinja2.

5. Organizar correctamente los archivos HTML dentro de la carpeta `templates`.

6. Organizar los archivos CSS, JavaScript e imágenes dentro de la carpeta `static`.

7. Ejecutar y comprobar el funcionamiento de la aplicación mediante el servidor de desarrollo de Flask.

8. Implementar una navegación funcional entre las diferentes secciones de la aplicación.

---

# <font color="#6A1B9A">3. TECNOLOGÍAS UTILIZADAS</font>

El proyecto utiliza las siguientes tecnologías:

| Tecnología         | Utilidad                                                           |
| ------------------ | ------------------------------------------------------------------ |
| Python             | Lenguaje de programación utilizado para el desarrollo del servidor |
| Flask              | Framework utilizado para construir la aplicación web               |
| HTML5              | Estructura de las páginas web                                      |
| CSS3               | Diseño y presentación visual                                       |
| JavaScript         | Funcionalidad e interacción del sitio                              |
| Bootstrap          | Diseño responsive y componentes visuales                           |
| Jinja2             | Sistema de plantillas utilizado por Flask                          |
| Visual Studio Code | Entorno de desarrollo                                              |
| Git y GitHub       | Control y almacenamiento del proyecto                              |

---

# <font color="#1565C0">4. ESTRUCTURA DEL PROYECTO</font>

La estructura actual del proyecto se encuentra organizada de la siguiente manera:

```text
VITRINA_UEA_SEMANA3/
│
├── static/
│   ├── imagenes/
│   ├── script.js
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── clientes.html
│   ├── facturacion.html
│   ├── index.html
│   ├── productos.html
│   └── proveedores.html
│
├── venv/
│
├── app.py
├── index.html
└── README.md
```

---

# <font color="#EF6C00">5. DESCRIPCIÓN DE LAS CARPETAS Y ARCHIVOS</font>

## <font color="#F57C00">Carpeta `templates`</font>

La carpeta `templates` contiene las páginas HTML utilizadas por Flask.

Dentro de esta carpeta se encuentran:

### `base.html`

Es la plantilla principal del proyecto.

Contiene los elementos comunes que se utilizan en las diferentes páginas, como:

* Estructura general del documento HTML.
* Configuración de Bootstrap.
* Hoja de estilos.
* Encabezado.
* Menú de navegación.
* Área destinada al contenido de cada página.
* Pie de página.
* Archivos JavaScript.

La utilización de `base.html` evita repetir la misma estructura HTML en todas las páginas.

### `index.html`

Es la página principal de Vitrina UEA.

Esta plantilla utiliza:

```html
{% extends "base.html" %}
```

para heredar la estructura definida en `base.html`.

El contenido específico de la página se coloca dentro del bloque:

```html
{% block content %}
```

### `productos.html`

Contiene la sección correspondiente a los productos disponibles en la plataforma.

### `clientes.html`

Contiene la sección correspondiente a la información de clientes.

### `proveedores.html`

Contiene la sección correspondiente a los proveedores.

### `facturacion.html`

Contiene la sección correspondiente al módulo de facturación.

---

# <font color="#00838F">6. CARPETA STATIC</font>

La carpeta `static` almacena los recursos estáticos utilizados por la aplicación.

Su estructura actual contiene:

```text
static/
│
├── imagenes/
├── style.css
└── script.js
```

## <font color="#0097A7">style.css</font>

Contiene los estilos personalizados utilizados para mejorar la presentación visual de la aplicación.

## <font color="#0097A7">script.js</font>

Contiene el código JavaScript utilizado para las funciones interactivas del proyecto.

## <font color="#0097A7">imagenes</font>

Esta carpeta contiene las imágenes utilizadas en la página principal y en las diferentes secciones de Vitrina UEA.

---

# <font color="#6A1B9A">7. ARCHIVO PRINCIPAL APP.PY</font>

El archivo `app.py` es el punto principal de ejecución de la aplicación Flask.

Su función es crear la aplicación, definir las rutas y determinar qué plantilla debe mostrarse cuando el usuario accede a una determinada dirección.

La aplicación se inicia mediante:

```python
from flask import Flask, render_template

app = Flask(__name__)
```

La función `Flask(__name__)` crea la aplicación y permite que Flask identifique correctamente la ubicación del proyecto.

La función `render_template()` permite cargar las plantillas HTML almacenadas dentro de la carpeta `templates`.

---

# <font color="#1565C0">8. CONFIGURACIÓN DE LAS RUTAS</font>

El proyecto cuenta actualmente con cinco rutas principales.

## <font color="#1976D2">Ruta de inicio</font>

```python
@app.route("/")
def inicio():
    return render_template("index.html")
```

Esta ruta se utiliza para mostrar la página principal de Vitrina UEA.

La dirección correspondiente es:

```text
http://127.0.0.1:5000/
```

## <font color="#1976D2">Ruta de productos</font>

```python
@app.route("/productos")
def productos():
    return render_template("productos.html")
```

Dirección:

```text
http://127.0.0.1:5000/productos
```

## <font color="#1976D2">Ruta de clientes</font>

```python
@app.route("/clientes")
def clientes():
    return render_template("clientes.html")
```

Dirección:

```text
http://127.0.0.1:5000/clientes
```

## <font color="#1976D2">Ruta de proveedores</font>

```python
@app.route("/proveedores")
def proveedores():
    return render_template("proveedores.html")
```

Dirección:

```text
http://127.0.0.1:5000/proveedores
```

## <font color="#1976D2">Ruta de facturación</font>

```python
@app.route("/facturacion")
def facturacion():
    return render_template("facturacion.html")
```

Dirección:

```text
http://127.0.0.1:5000/facturacion
```

---

# <font color="#2E7D32">9. CONFIGURACIÓN DEL ENTORNO VIRTUAL</font>

El proyecto utiliza un entorno virtual denominado:

```text
venv
```

El entorno virtual permite mantener separadas las dependencias de este proyecto de las demás instalaciones de Python existentes en el equipo.

En Windows PowerShell, el entorno puede activarse mediante:

```powershell
.\venv\Scripts\Activate.ps1
```

Cuando el entorno se encuentra activo, la terminal muestra:

```text
(venv) PS D:\Vitrina_UEA_Semana3>
```

Esto indica que los comandos de Python se están ejecutando dentro del entorno virtual del proyecto.

---

# <font color="#EF6C00">10. INSTALACIÓN DE FLASK</font>

Si Flask todavía no está instalado dentro del entorno virtual, se puede instalar mediante:

```powershell
pip install flask
```

Para comprobar la instalación:

```powershell
pip show flask
```

También se puede comprobar la versión instalada mediante:

```powershell
flask --version
```

---

# <font color="#6A1B9A">11. EJECUCIÓN DEL PROYECTO</font>

Para ejecutar la aplicación se deben seguir los siguientes pasos.

## <font color="#7B1FA2">Paso 1. Abrir la carpeta del proyecto</font>

Abrir el proyecto:

```text
D:\Vitrina_UEA_Semana3
```

en Visual Studio Code.

## <font color="#7B1FA2">Paso 2. Abrir la terminal</font>

Desde Visual Studio Code se puede utilizar:

```text
Terminal > Nueva terminal
```

## <font color="#7B1FA2">Paso 3. Activar el entorno virtual</font>

Ejecutar:

```powershell
.\venv\Scripts\Activate.ps1
```

La terminal debe mostrar:

```text
(venv)
```

## <font color="#7B1FA2">Paso 4. Ejecutar Flask</font>

Ejecutar:

```powershell
python app.py
```

Si la configuración es correcta, Flask mostrará un mensaje similar a:

```text
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

## <font color="#7B1FA2">Paso 5. Abrir la aplicación</font>

Abrir el navegador y acceder a:

```text
http://127.0.0.1:5000/
```

---

# <font color="#1565C0">12. FUNCIONAMIENTO DE LA APLICACIÓN</font>

El funcionamiento general de la aplicación se puede comprender mediante el siguiente proceso:

```text
Usuario
   |
   v
Navegador web
   |
   v
Ruta Flask
   |
   v
Función Python
   |
   v
render_template()
   |
   v
Plantilla HTML
   |
   v
Contenido mostrado al usuario
```

Cuando el usuario ingresa a una dirección determinada, Flask identifica la ruta correspondiente.

Por ejemplo:

```text
/productos
```

es asociada con:

```python
@app.route("/productos")
def productos():
    return render_template("productos.html")
```

Flask ejecuta la función `productos()` y posteriormente carga la plantilla `productos.html`.

---

# <font color="#00838F">13. HERENCIA DE PLANTILLAS CON JINJA2</font>

Una de las mejoras realizadas durante la adaptación del proyecto a Flask fue la implementación de una plantilla base.

El archivo `base.html` contiene la estructura común del sitio.

La página `index.html` utiliza:

```html
{% extends "base.html" %}
```

Esto permite reutilizar la estructura de `base.html`.

El título de cada página puede modificarse mediante:

```html
{% block title %}
Inicio - Vitrina UEA
{% endblock %}
```

Mientras que el contenido específico se coloca dentro de:

```html
{% block content %}
```

Esta metodología permite evitar la duplicación de código HTML y facilita el mantenimiento de la aplicación.

---

# <font color="#2E7D32">14. NAVEGACIÓN MEDIANTE URL_FOR</font>

El menú principal utiliza la función `url_for()` de Flask para generar las direcciones de las diferentes rutas.

Por ejemplo:

```html
<a class="nav-link"
   href="{{ url_for('inicio') }}">
    Inicio
</a>
```

También se utilizan:

```html
{{ url_for('productos') }}
```

```html
{{ url_for('clientes') }}
```

```html
{{ url_for('proveedores') }}
```

```html
{{ url_for('facturacion') }}
```

La utilización de `url_for()` permite que Flask genere automáticamente las direcciones correspondientes a las funciones definidas en `app.py`.

---

# <font color="#EF6C00">15. COMPROBACIÓN DEL FUNCIONAMIENTO</font>

Durante las pruebas realizadas, la aplicación respondió correctamente a las diferentes solicitudes.

Las rutas comprobadas fueron:

```text
/
```

```text
/productos
```

```text
/clientes
```

```text
/proveedores
```

```text
/facturacion
```

Las solicitudes fueron respondidas mediante el código HTTP:

```text
200
```

El código `200` indica que la solicitud fue procesada correctamente por el servidor.

También se comprobó la carga de:

```text
style.css
```

```text
script.js
```

y las imágenes almacenadas dentro de:

```text
static/imagenes/
```

---

# <font color="#6A1B9A">16. MODO DEBUG</font>

Durante el desarrollo se utiliza:

```python
app.run(debug=True)
```

El modo `debug` facilita el desarrollo porque permite detectar errores y reiniciar automáticamente el servidor cuando se realizan cambios en los archivos.

Este modo está destinado al desarrollo y las pruebas locales.

Para un entorno de producción se debería utilizar un servidor web apropiado y una configuración diferente.

---

# <font color="#1565C0">17. PROBLEMA IDENTIFICADO Y SOLUCIONADO</font>

Durante la adaptación del proyecto a Flask se identificó una duplicación de la estructura HTML.

La página `index.html` contenía elementos que ya estaban definidos dentro de `base.html`, incluyendo:

```text
DOCTYPE
html
head
body
header
menú de navegación
```

Esto generaba una estructura HTML duplicada.

La solución consistió en centralizar los elementos comunes dentro de `base.html` y utilizar la herencia de plantillas mediante:

```html
{% extends "base.html" %}
```

De esta manera, `index.html` contiene únicamente el contenido específico de la página.

Esta modificación permitió obtener una estructura más organizada y adecuada para una aplicación Flask.

---

# <font color="#2E7D32">18. RESULTADO ACTUAL DEL PROYECTO</font>

Actualmente, **Vitrina UEA** cuenta con una estructura funcional basada en Flask.

La aplicación dispone de:

* Una aplicación Flask principal.
* Un entorno virtual de Python.
* Cinco rutas funcionales.
* Plantillas HTML independientes.
* Una plantilla base reutilizable.
* Navegación mediante `url_for()`.
* Archivos CSS y JavaScript.
* Imágenes organizadas dentro de `static`.
* Diseño basado en Bootstrap.
* Ejecución mediante servidor local de Flask.
* Comprobación de las diferentes rutas mediante solicitudes HTTP.

---

# <font color="#00838F">19. PRÓXIMAS ETAPAS</font>

El proyecto puede continuar evolucionando mediante la incorporación progresiva de nuevas funcionalidades.

Entre las posibles etapas de desarrollo se encuentran:

1. Implementación de formularios para el registro de información.

2. Conexión con una base de datos.

3. Gestión de productos.

4. Gestión de clientes.

5. Gestión de proveedores.

6. Implementación de procesos de facturación.

7. Validación de información ingresada por los usuarios.

8. Incorporación de operaciones de creación, consulta, modificación y eliminación de registros.

9. Mejoramiento de la interfaz de usuario.

10. Implementación de funcionalidades adicionales para la plataforma Vitrina UEA.

---

# <font color="#1565C0">20. AUTOR</font>

**Johnny Alberto Vera Vaca**

**Universidad Estatal Amazónica**

**Tecnología de la Información**

**Proyecto Integrador**

**Desarrollo de Aplicaciones Web**

**Año: 2026**

---

# <font color="#2E7D32">21. CONCLUSIÓN</font>

El proyecto **Vitrina UEA** ha evolucionado desde una estructura web basada en HTML, CSS y JavaScript hacia una aplicación web organizada mediante Flask.

La implementación de rutas, plantillas Jinja2, herencia de `base.html` y organización de archivos estáticos permite disponer de una estructura más ordenada, reutilizable y fácil de mantener.

La comprobación realizada demuestra que las principales rutas de la aplicación funcionan correctamente y que los recursos estáticos son cargados de manera adecuada.

La utilización de Flask constituye una base importante para continuar desarrollando las siguientes etapas del proyecto, especialmente aquellas relacionadas con formularios, bases de datos y gestión dinámica de la información.

---

<div align="center">

# <font color="#1565C0">VITRINA UEA</font>

<font color="#2E7D32">Desarrollo progresivo de una aplicación web con Flask</font>

**2026**

</div>
