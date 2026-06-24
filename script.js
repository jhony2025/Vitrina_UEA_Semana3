const formulario = document.getElementById("formProducto");
const lista = document.getElementById("listaProductos");
const contador = document.getElementById("contador");
const mensaje = document.getElementById("mensaje");

let total = 0;

formulario.addEventListener("submit", function(event){

    event.preventDefault();

    const nombre =
    document.getElementById("nombre").value;

    const descripcion =
    document.getElementById("descripcion").value;

    const categoria =
    document.getElementById("categoria").value;

    if(nombre === "" || descripcion === "" || categoria === ""){

        mensaje.innerHTML =
        "Por favor complete todos los campos.";

        mensaje.className =
        "text-danger mt-3";

        return;
    }

    mensaje.innerHTML =
    "Producto registrado correctamente.";

    mensaje.className =
    "text-success mt-3";

    crearProducto(nombre, descripcion, categoria);

    formulario.reset();

});

function crearProducto(nombre, descripcion, categoria){

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

            <button class="btn btn-danger mt-3 eliminar">
                Eliminar
            </button>

        </div>
    `;

    lista.appendChild(tarjeta);

    total++;

    contador.innerText = total;

    const botonEliminar =
    tarjeta.querySelector(".eliminar");

    botonEliminar.addEventListener("click", () => {

        tarjeta.remove();

        total--;

        contador.innerText = total;

    });
}