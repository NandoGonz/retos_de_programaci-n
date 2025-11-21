"""2 Entrada de usuario no válida
Pide un número al usuario con input() y usa try/except
para manejar el error si escribe letras en vez de números.
"""

try:
    num_usuario = int(input("Ingrse un número cualquiera: "))

except ValueError:
    print("⚠️ Debe ingresar un valor numerico")
else:
    print(f"🔢 El número digitado por el usuario es {num_usuario}")
finally:
    print("✅ manejo de exepción realizado de forma correcta")
