import random

letras = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

caracteres_especiales = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "[",
    "]",
    "{",
    "}",
    "\\",
    "|",
    ";",
    ":",
    "'",
    '"',
    ",",
    ".",
    "<",
    ">",
    "/",
    "?",
    "`",
    "~",
]

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

ususarios_letras = int(input("Cuantas letras desea en la contraseña?: "))
ususarios_numeros = int(input("Cuantos números desea en la contraseña?: "))
ususarios_caracteres_especiales = int(
    input("Cuantoa caracteres especiales desea en la contraseña?: ")
)

"""
La contraseña se genera según el orden de los inputs
"""

password = ""

for letra in range(1, ususarios_letras + 1):
    password += random.choice(letras)

for numero in range(1, ususarios_numeros + 1):
    password += random.choice(numeros)

for caracter in range(1, ususarios_caracteres_especiales + 1):
    password += random.choice(caracteres_especiales)


modificador = list(password)
random.shuffle(modificador)
sp_pass = "".join(modificador)
print(password)
print(sp_pass)
