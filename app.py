from flask import Flask, render_template, request, redirect, url_for
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required
)
from werkzeug.security import check_password_hash
from conexion import obtener_conexion


app = Flask(__name__)

# ==============================
# CONFIGURACIÓN DE FLASK-LOGIN
# ==============================

app.secret_key = "vitrina_uea_clave_secreta"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# ==============================
# MODELO DE USUARIO
# ==============================

class Usuario(UserMixin):

    def __init__(self, id, usuario):
        self.id = id
        self.usuario = usuario


@login_manager.user_loader
def cargar_usuario(user_id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, usuario
        FROM usuarios
        WHERE id = %s
    """, (user_id,))

    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    if usuario:
        return Usuario(usuario[0], usuario[1])

    return None


# ==============================
# LOGIN
# ==============================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        password = request.form["password"]

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT id, usuario, password
            FROM usuarios
            WHERE usuario = %s
        """, (usuario,))

        datos_usuario = cursor.fetchone()

        cursor.close()
        conexion.close()

        if datos_usuario:

            password_correcta = check_password_hash(
                datos_usuario[2],
                password
            )

            if password_correcta:

                usuario_obj = Usuario(
                    datos_usuario[0],
                    datos_usuario[1]
                )

                login_user(usuario_obj)

                return redirect(url_for("inicio"))

        return render_template(
            "login.html",
            error="Usuario o contraseña incorrectos."
        )

    return render_template("login.html")


# ==============================
# CERRAR SESIÓN
# ==============================

@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("login"))


# ==============================
# RUTA PRINCIPAL
# ==============================

@app.route("/")
@login_required
def inicio():

    return render_template("index.html")


# ==============================
# PRODUCTOS - LISTAR
# ==============================

@app.route("/productos")
@login_required
def productos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, descripcion, categoria, imagen
        FROM productos
        ORDER BY id
    """)

    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "productos.html",
        productos=productos
    )


# ==============================
# PRODUCTOS - REGISTRAR
# ==============================

@app.route("/registrar_producto", methods=["GET", "POST"])
@login_required
def registrar_producto():

    if request.method == "POST":

        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        categoria = request.form["categoria"]
        imagen = request.form["imagen"]

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT id
            FROM categorias
            WHERE nombre = %s
        """, (categoria,))

        categoria_encontrada = cursor.fetchone()

        categoria_id = (
            categoria_encontrada[0]
            if categoria_encontrada
            else 1
        )

        cursor.execute("""
            INSERT INTO productos
            (
                nombre,
                descripcion,
                categoria,
                imagen,
                categoria_id,
                proveedor_id
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nombre,
            descripcion,
            categoria,
            imagen,
            categoria_id,
            1
        ))

        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("productos"))

    return render_template("registrar_producto.html")


# ==============================
# PRODUCTOS - EDITAR
# ==============================

@app.route("/editar_producto/<int:id>", methods=["GET", "POST"])
@login_required
def editar_producto(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        categoria = request.form["categoria"]
        imagen = request.form["imagen"]

        cursor.execute("""
            SELECT id
            FROM categorias
            WHERE nombre = %s
        """, (categoria,))

        categoria_encontrada = cursor.fetchone()

        categoria_id = (
            categoria_encontrada[0]
            if categoria_encontrada
            else 1
        )

        cursor.execute("""
            UPDATE productos
            SET
                nombre = %s,
                descripcion = %s,
                categoria = %s,
                imagen = %s,
                categoria_id = %s,
                proveedor_id = %s
            WHERE id = %s
        """, (
            nombre,
            descripcion,
            categoria,
            imagen,
            categoria_id,
            1,
            id
        ))

        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("productos"))

    cursor.execute("""
        SELECT
            id,
            nombre,
            descripcion,
            categoria,
            imagen,
            categoria_id,
            proveedor_id
        FROM productos
        WHERE id = %s
    """, (id,))

    producto = cursor.fetchone()

    cursor.close()
    conexion.close()

    return render_template(
        "editar_producto.html",
        producto=producto
    )


# ==============================
# PRODUCTOS - ELIMINAR
# ==============================

@app.route("/eliminar_producto/<int:id>", methods=["POST"])
@login_required
def eliminar_producto(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM productos
        WHERE id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect(url_for("productos"))


# ==============================
# CLIENTES
# ==============================

@app.route("/clientes")
@login_required
def clientes():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, telefono, correo
        FROM clientes
        ORDER BY id
    """)

    clientes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "clientes.html",
        clientes=clientes
    )


@app.route("/registrar_cliente", methods=["GET", "POST"])
@login_required
def registrar_cliente():

    if request.method == "POST":

        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO clientes (nombre, telefono, correo)
            VALUES (%s, %s, %s)
        """, (nombre, telefono, correo))

        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("clientes"))

    return render_template("registrar_cliente.html")


@app.route("/editar_cliente/<int:id>", methods=["GET", "POST"])
@login_required
def editar_cliente(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]

        cursor.execute("""
            UPDATE clientes
            SET nombre = %s, telefono = %s, correo = %s
            WHERE id = %s
        """, (nombre, telefono, correo, id))

        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("clientes"))

    cursor.execute("""
        SELECT id, nombre, telefono, correo
        FROM clientes
        WHERE id = %s
    """, (id,))

    cliente = cursor.fetchone()

    cursor.close()
    conexion.close()

    return render_template(
        "editar_cliente.html",
        cliente=cliente
    )


@app.route("/eliminar_cliente/<int:id>", methods=["POST"])
@login_required
def eliminar_cliente(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM clientes
        WHERE id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect(url_for("clientes"))


# ==============================
# PROVEEDORES
# ==============================

@app.route("/proveedores")
@login_required
def proveedores():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, telefono, correo
        FROM proveedores
        ORDER BY id
    """)

    proveedores = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "proveedores.html",
        proveedores=proveedores
    )


@app.route("/registrar_proveedor", methods=["GET", "POST"])
@login_required
def registrar_proveedor():

    if request.method == "POST":

        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO proveedores (nombre, telefono, correo)
            VALUES (%s, %s, %s)
        """, (nombre, telefono, correo))

        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("proveedores"))

    return render_template("registrar_proveedor.html")


@app.route("/editar_proveedor/<int:id>", methods=["GET", "POST"])
@login_required
def editar_proveedor(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    if request.method == "POST":

        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]

        cursor.execute("""
            UPDATE proveedores
            SET nombre = %s, telefono = %s, correo = %s
            WHERE id = %s
        """, (nombre, telefono, correo, id))

        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("proveedores"))

    cursor.execute("""
        SELECT id, nombre, telefono, correo
        FROM proveedores
        WHERE id = %s
    """, (id,))

    proveedor = cursor.fetchone()

    cursor.close()
    conexion.close()

    return render_template(
        "editar_proveedor.html",
        proveedor=proveedor
    )


@app.route("/eliminar_proveedor/<int:id>", methods=["POST"])
@login_required
def eliminar_proveedor(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM proveedores
        WHERE id = %s
    """, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect(url_for("proveedores"))


# ==============================
# FACTURACIÓN
# ==============================

@app.route("/facturacion")
@login_required
def facturacion():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            facturas.id,
            clientes.nombre,
            facturas.fecha,
            facturas.total,
            facturas.estado
        FROM facturas
        JOIN clientes ON facturas.cliente_id = clientes.id
        ORDER BY facturas.id
    """)

    facturas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "facturacion.html",
        facturas=facturas
    )


@app.route("/registrar_factura", methods=["GET", "POST"])
@login_required
def registrar_factura():

    if request.method == "POST":

        from decimal import Decimal

        cliente_id = request.form["cliente_id"]
        producto_id = request.form["producto_id"]
        cantidad = int(request.form["cantidad"])
        precio = Decimal(request.form["precio"])
        total = cantidad * precio

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                INSERT INTO facturas (cliente_id, total, estado)
                VALUES (%s, %s, %s)
                RETURNING id
            """, (cliente_id, total, "Pendiente"))

            factura_id = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO detalle_factura
                    (factura_id, producto_id, cantidad, precio)
                VALUES (%s, %s, %s, %s)
            """, (factura_id, producto_id, cantidad, precio))

            conexion.commit()
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()

        return redirect(url_for("facturacion"))

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre
        FROM clientes
        ORDER BY nombre
    """)
    clientes = cursor.fetchall()

    cursor.execute("""
        SELECT id, nombre
        FROM productos
        ORDER BY nombre
    """)
    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "registrar_factura.html",
        clientes=clientes,
        productos=productos
    )


@app.route("/ver_factura/<int:id>")
@login_required
def ver_factura(id):

    from decimal import Decimal

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            facturas.id,
            clientes.nombre,
            facturas.fecha,
            productos.nombre,
            detalle_factura.cantidad,
            detalle_factura.precio,
            facturas.total,
            facturas.estado
        FROM facturas
        JOIN clientes ON facturas.cliente_id = clientes.id
        JOIN detalle_factura ON facturas.id = detalle_factura.factura_id
        JOIN productos ON detalle_factura.producto_id = productos.id
        WHERE facturas.id = %s
    """, (id,))

    registros = cursor.fetchall()

    cursor.close()
    conexion.close()

    if not registros:
        return "Factura no encontrada", 404

    factura = {
        "id": registros[0][0],
        "cliente": registros[0][1],
        "fecha": registros[0][2],
        "total": registros[0][6],
        "estado": registros[0][7]
    }
    subtotal = Decimal(str(factura["total"]))
    iva = subtotal * Decimal("0.15")
    total_con_iva = subtotal + iva

    detalles = [
        {
            "producto": registro[3],
            "cantidad": registro[4],
            "precio": registro[5]
        }
        for registro in registros
    ]

    return render_template(
        "ver_factura.html",
        factura=factura,
        detalles=detalles,
        subtotal=subtotal,
        iva=iva,
        total_con_iva=total_con_iva
    )


# ==============================
# EJECUCIÓN
# ==============================

if __name__ == "__main__":
    app.run(debug=True)