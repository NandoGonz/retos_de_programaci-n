"""Para establecer una conexión MySQL debemos importar mysqlconnector"""

import mysql.connector
import pandas as pd  # Importamos pandas para leer la información de mejor manera

# Establecemos la caonexión de forma plana
# Enviamos los puertos como parametros
conn = mysql.connector.connect(
    host="localhost",  # == 127.1.1
    user="root",
    password="admin",
    database="tienda",
    port=3306,
)

# Hacemos un pin de conexión para validar un funcionamiento correcto
cursor = conn.cursor()  # cursor es el nombre más indicados para estas variables


# Verificamso que todo funciones con una consulta
# usaremos una funcion para aplicar crud
def leer_datos():
    """Muestra los datos de la table selecionada de la BD tienda"""
    cursor.execute("SELECT * FROM clientes;")
    resultado = (
        cursor.fetchall()
    )  # el método fetcall nos ayuda a guardar info cuando la recuperamos

    for i in resultado:
        print(i)


def crear_cliente(nombre, correo, edad):
    """Agrega un cliente nuevo a la tabla clientes de la bd tienda"""
    # creamos una variable query para generar una query tipo MySQL
    # los values %s evita las inyecciones SQL
    query = "INSERT INTO clientes(nombre, correo, edad) VALUES(%s, %s, %s)"
    params = nombre, correo, edad  # creamos una variable para guardar los parametros
    cursor.execute(
        query, params
    )  # pasamos nuestras variables como parametros para no sobrecargar el método execute de info
    conn.commit()  # ejecutamos un commit para guardar los cambios
    print("Cliente creado de forma exitosa")


def login(nombre, password):
    query = "SELECT * FROM usuarios WHERE nombre = %s AND pass = %s;"
    params = (nombre, password)
    cursor.execute(query, params)
    resultado = (
        cursor.fetchone()
    )  # con fetchone para capturar el dato coincidente con nuestros parametros
    if resultado:  # con la condicion verificamos si existe o no el dato en la DB
        print("Loguin exitoso")
    else:
        print("Loguin fallido")


def actualizar_cliente(id_cliente, nombre):
    query = "UPDATE clientes SET nombre = %s WHERE id = %s;"
    params = (nombre, id_cliente)
    cursor.execute(query, params)
    conn.commit()
    print("Cliente actualizado")


def eliminar_cliente(id_cliente):
    query = "DELETE FROM clientes WHERE id = %s;"
    params = id_cliente
    cursor.execute(
        query, (params,)
    )  # para eliminar de forma correcrta la variable va en parentesis y con una ,
    conn.commit()
    print("Cliente eliminado de forma exitosa")


def leer_pandas():
    query = "SELECT * FROM clientes;"
    # Creamso una variablr df(dataframe) y usamos la libreria y el metodo read_sql
    # Le pasamso como parametros la query y la conexión
    df = pd.read_sql(query, conn)
    print(df)


# leer_datos()
# crear_cliente("Alonso", "fernandoalo@Yahoo.com", 58)
# login("admin", "admin123")
# actualizar_cliente(55, "Fernado Alonso")
# eliminar_cliente(56)
leer_pandas()

# Debemos cerrar siempre nuestra conexión
conn.close()
cursor.close()
