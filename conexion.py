import os

import psycopg2


def obtener_conexion():
    return psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="Name: vitrina_uea",
        user="postgres",
        password=os.environ["POSTGRES_PASSWORD"]
    )


if __name__ == "__main__":
    try:
        conexion = obtener_conexion()
        print("CONEXION EXITOSA A POSTGRESQL")
        conexion.close()
    except Exception as e:
        print("ERROR:", repr(e))