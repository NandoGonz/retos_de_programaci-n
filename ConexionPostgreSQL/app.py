"""Importamos la librerria psycode2 para establecer la conecxión con la db"""

import os  # Nos permiter movernos entre archivo para identificar las variables de entorno
import psycopg2
from psycopg2 import (
    OperationalError,
    Error,
)  # importamos estos modulos para el control de errores possgrestsql
from dotenv import (
    load_dotenv,
)  # debemso importar la función load_dotenv activar el llamado

# de las variables de entorno

load_dotenv()  # llamams a la función para conectarnso con los archivos.env
# Establecemos una conexión
conn = None

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")  # nombre del usuario
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")  # 127.0.0.1
DB_PORT = os.getenv("DB_PORT")
"""Usamos la librerira psycopg2 y el método connect para establecer 
la conexión"""


def conectar():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        print("Coneción OK")
        return conn
    except OperationalError as oe:
        print(f"[ERROR] Problema operacional al conectar: {oe}")
    except Error as e:
        print(f"[ERROR] Problema operacional al conectar: {e}")
    except Exception as ex:
        print(f"[ERRRO] Inesperado: {ex}")
    return None


def llamar_profesores(conn):
    query = """SELECT first_name FROM teachers"""
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            fila = cur.fetchall()
            for f in fila:
                print(f)
    except Error as e:
        print(f"[ERRROR] No se pudieron recuperar los profesores: {e}")


def insert_teacher(
    conn,
    department_id,
    first_name,
    last_name,
    email,
    phone,
    hire_date,
    salary,
):
    query = """INSERT INTO teachers(department_id, first_name, last_name, email, phone, hire_date, salary)
VALUES(%s, %s, %s, %s, %s, %s, %s);"""
    params = (department_id, first_name, last_name, email, phone, hire_date, salary)
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
        conn.commit()
        print("[OK] Inserción segura realizada")
    except Error as e:
        conn.rollback()  # evitamos que un dato qeude vagando
        print(f"[ERROR] No de pudo insertar el profesor: {e}")


conexion = conectar()
insert_teacher(
    conexion,
    5,
    "Adriana",
    "Rivera",
    "Rivera@adri",
    "123454987",
    "2023-05-15",
    "1500000",
)
