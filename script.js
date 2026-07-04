// =============================
// ELEMENTOS DEL DOM
// =============================

const formulario = document.getElementById("formProducto");
const lista = document.getElementById("listaProductos");
const contador = document.getElementById("contador");
const mensaje = document.getElementById("mensaje");

const nombre = document.getElementById("nombre");
const descripcion = document.getElementById("descripcion");
const categoria = document.getElementById("categoria");

const errorNombre = document.getElementById("errorNombre");
const errorDescripcion = document.getElementById("errorDescripcion");
const errorCategoria = document.getElementById("errorCategoria");

let total = 0;

// =============================
// MOSTRAR MENSAJES
// =============================

function mostrarMensaje(tipo, texto) {

    mensaje.className = `alert ${tipo} mt-3`;
    mensaje.textContent = texto;
}

function limpiarMensaje() {

    mensaje.className = "mt-4";
    mensaje.textContent = "";
}

// =============================
// ACTUALIZAR CONTADOR
// =============================

function actualizarContador() {

    contador.innerText = total;
}

// =============================
// LIMPIAR FORMULARIO
// =============================

function limpiarFormulario() {

    formulario.reset();

    [nombre, descripcion, categoria].forEach((campo) => {
        campo.classList.remove("is-valid", "is-invalid");
    });

    [errorNombre, errorDescripcion, errorCategoria].forEach((elemento) => {
        elemento.textContent = "";
    });

    limpiarMensaje();
}

// =============================
// FUNCIONES DE VALIDACIÓN
// =============================

function mostrarError(campo, elementoError, texto) {

    campo.classList.remove("is-valid");
    campo.classList.add("is-invalid");
    elementoError.textContent = texto;

    return false;
}

function mostrarExito(campo, elementoError) {

    campo.classList.remove("is-invalid");
    campo.classList.add("is-valid");
    elementoError.textContent = "";

    return true;
}

function validarNombre() {

    const valor = nombre.value.trim();

    if (valor === "") {
        return mostrarError(nombre, errorNombre, "El nombre es obligatorio.");
    }

    if (valor.length < 3) {
        return mostrarError(nombre, errorNombre, "Debe tener mínimo 3 caracteres.");
    }

    return mostrarExito(nombre, errorNombre);
}

function validarDescripcion() {

    const valor = descripcion.value.trim();

    if (valor === "") {
        return mostrarError(descripcion, errorDescripcion, "La descripción es obligatoria.");
    }

    if (valor.length < 10) {
        return mostrarError(descripcion, errorDescripcion, "Debe contener mínimo 10 caracteres.");
    }

    return mostrarExito(descripcion, errorDescripcion);
}

function validarCategoria() {

    if (categoria.value === "") {
        return mostrarError(categoria, errorCategoria, "Seleccione una categoría.");
    }

    return mostrarExito(categoria, errorCategoria);
}

function validarFormulario() {

    const nombreValido = validarNombre();
    const descripcionValida = validarDescripcion();
    const categoriaValida = validarCategoria();

    return nombreValido && descripcionValida && categoriaValida;
}

// =============================
// EVENTOS EN TIEMPO REAL
// =============================

nombre.addEventListener("input", () => {
    validarNombre();
    limpiarMensaje();
});

descripcion.addEventListener("input", () => {
    validarDescripcion();
    limpiarMensaje();
});

categoria.addEventListener("change", () => {
    validarCategoria();
    limpiarMensaje();
});

nombre.addEventListener("blur", validarNombre);
descripcion.addEventListener("blur", validarDescripcion);
categoria.addEventListener("blur", validarCategoria);

// =============================
// EVENTO SUBMIT
// =============================

formulario.addEventListener("submit", function (event) {

    event.preventDefault();
    limpiarMensaje();

    if (!validarFormulario()) {

        mostrarMensaje(
            "alert-danger",
            "Corrija los errores antes de registrar el producto."
        );

        return;
    }

    mostrarMensaje(
        "alert-success",
        "Producto registrado correctamente."
    );

    crearProducto(
        nombre.value.trim(),
        descripcion.value.trim(),
        categoria.value
    );

    limpiarFormulario();
});

// =============================
// CREAR PRODUCTO
// =============================

function crearProducto(nombre, descripcion, categoria) {

    const tarjeta =
        document.createElement("div");

    tarjeta.className =
        "col-md-4 mb-3";

    tarjeta.innerHTML = `

        <div class="card shadow p-3">

            <h5>${nombre}</h5>

            <p>${descripcion}</p>

            <span class="badge bg-primary">
                ${categoria}
            </span>

            <button
                class="btn btn-danger mt-3 eliminar">

                Eliminar

            </button>

        </div>

    `;

    lista.appendChild(tarjeta);

    total++;

actualizarContador();

    const botonEliminar =
        tarjeta.querySelector(".eliminar");

    botonEliminar.addEventListener("click", () => {

        tarjeta.remove();

        total--;

actualizarContador();

    });

}