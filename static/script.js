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
const tabla = document.getElementById("tablaProductos");
const spinnerRegistro = document.getElementById("spinnerRegistro");
const videoSpinner = document.getElementById("videoSpinner");
const deleteProductNameEl = document.getElementById("deleteProductName");
const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");

let total = 0;
let tarjetaAEliminar = null;

const confirmDeleteModal = new bootstrap.Modal(document.getElementById("confirmDeleteModal"));

// =============================
// MOSTRAR MENSAJES
// =============================

function mostrarMensaje(tipo, texto) {

    mensaje.className = `alert ${tipo} mt-3`;
    mensaje.textContent = texto;
}

function limpiarMensaje() {

    mensaje.className = "mt-4 d-none";
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

    spinnerRegistro.classList.remove("d-none");
    formulario.querySelector("button[type=submit]").disabled = true;

    setTimeout(() => {
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
        spinnerRegistro.classList.add("d-none");
        formulario.querySelector("button[type=submit]").disabled = false;
    }, 700);
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

    const fila = document.createElement("tr");
    fila.innerHTML = `
        <td>${nombre}</td>
        <td>${descripcion}</td>
        <td>${categoria}</td>
        <td>
            <button class="btn btn-sm btn-danger eliminar-tabla">Eliminar</button>
        </td>
    `;

    tabla.appendChild(fila);
    lista.appendChild(tarjeta);

    total++;

    actualizarContador();

    const botonEliminar =
        tarjeta.querySelector(".eliminar");
    const botonEliminarTabla =
        fila.querySelector(".eliminar-tabla");

    const confirmarEliminacion = () => {
        tarjetaAEliminar = { tarjeta, fila };
        deleteProductNameEl.textContent = nombre;
        confirmDeleteModal.show();
    };

    botonEliminar.addEventListener("click", confirmarEliminacion);
    botonEliminarTabla.addEventListener("click", confirmarEliminacion);

}

confirmDeleteBtn.addEventListener("click", () => {
    if (!tarjetaAEliminar) return;

    tarjetaAEliminar.tarjeta.remove();
    tarjetaAEliminar.fila.remove();
    tarjetaAEliminar = null;

    total--;
    actualizarContador();
    mostrarMensaje("alert-warning", "Producto eliminado correctamente.");
    confirmDeleteModal.hide();
});

// =====================================================
// VIDEO PORTADA
// =====================================================

const playVideoBtn = document.getElementById("playVideoBtn");
const videoIframe = document.getElementById("videoIframe");
const videoContainer = document.querySelector(".video-container");

if (playVideoBtn && videoIframe && videoContainer) {
    playVideoBtn.addEventListener("click", () => {
        videoIframe.src = `${videoIframe.dataset.src}?autoplay=1`;
        videoContainer.classList.add("loaded");
    });
}
