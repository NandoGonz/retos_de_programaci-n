# Para el uso de CSV debemos importar este tipo de lectura importamos
import csv
import pandas as pd


with open("estudiantes.csv", "r", encoding="UTF-8") as archivo:
    lector = csv.reader(
        archivo
    )  # para leer creamos una variable, usamnos el modulo CSV
    # seguido del método .reader(archivo) al cual le mandamos como parametro nuestro(archicvo)
    # Lo recoremos con un ciclo for para mostrar la información como lista de listas
    for fila in lector:
        print(fila)

# Importamso la libreria pandas, para leer los datos de una manera más profesional


# Definimos un data frame como df, es un formato estipulado en filas y columnas
df = pd.read_csv("estudiantes.csv")
print(df.head())
print(df.info())  # Con el método .info() podemos observar la información del df
"""
# Creando Dataframe de forma manual

df2 = pd.DataFrame(
    {"nombre": ["Adriana", "Kristina"], "edad": [30, 4], "ciudad": ["Luruaco", "Plato"]}
)
print("DataFrame 2")
print(df2)
"""

df = pd.read_csv("estudiantes.csv")

# Guardando archivos con un formato distinto
# df.to_csv("df.csv", index=False)

# Información general
df.info()

# estadisticas descriptivas
print(df.describe())

# ultimasd 5 filas
print(df.tail())

# dimensiones (filas x columnas)
print(df.shape)
print(type(df.shape))  # este métdod se usa sin parentesis  y con type miramos el tipo

# podemos traer el nombre de cada columna
print(df.columns)  # estosso métodos que no usan parentesis

# indices
print(df.index)

# Selección de los datos
print(df["Nombre"])  # llamma una seríe(columna)
# podemos hacer un llamada multiple
print(df[["Nombre", "Carrera"]])

# Podemso llamar las filas
print(
    df.iloc[0]
)  # usamos la rebanda de las lista que es una llamada de los elmentos por su indice

# para llamar a las columnas de forma individual usamos el método .loc
print(df.loc[df["Edad"] > 20])

# Filtrando datos
print(df[df["Edad"] > 22])

# Agregando nuevsop valores
# df["Institución"] = "Dev Senior" # De esta manera agrega el mismo valor a todas las llaves

# Asignando un nuevo valor de forma inidividual
df["Institución"] = ["Dev Senior", "UNAD", "UNIMAG", "IBERO"]

# Eliminando
df.drop("Edad", axis=1, inplace=True)  # elimina de forma indiviual
df.drop(["Nombre", "Carrera"], axis=1, inplace=True)
print(df)
