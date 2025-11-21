""" "Usa un diccionario donde la clave sea el nombre y el valor sea el número de teléfono.

Permite agregar, eliminar y buscar contactos dentro de un bucle while.

Muestra todos los contactos al salir"""

from prettytable import PrettyTable

contactos = {}

while True:
    print("#" * 50)
    print("1. Agregar contacto")
    print("2. ELiminar contacto")
    print("3. Buscar contacto")
    print("4. Mostrar Agenda")
    print("")
    print("#" * 50)

    try:
        opcion = int(input("Ingrese una opción: "))
        match opcion:
            case 1:
                nombre = input("Ingrese el nombre del contacto: ").title()
                numero = int(input("Ingrese el número del contacto: "))
                if nombre not in contactos:
                    contactos[nombre] = numero
                    print("✅ Contacto agregado con exito")
                else:
                    print(f"⚠️ Ya exiate un contacto con ese nombre '{nombre.title()}' ")
            case 2:
                nombre = input("Ingrese el nombre del contacto: ").title()
                if nombre in contactos:
                    del contactos[nombre]
                    print("✅ Contacto eliminado correctamente")
                else:
                    print("⚠️ Ese contacoto no existe en la agenda")
            case 3:
                nombre = input("Ingrese el nombre del contacto: ").title()
                if nombre not in contactos:
                    print(f"⚠️ El contacto {nombre} no está registrado")
                else:
                    print(
                        f"✅ el contacot {nombre} esta registrado con el número {contactos[nombre]}"
                    )
            case 4:
                table = PrettyTable()
                table.field_names = ["Contacto", "Número"]
                if contactos:
                    for k, v in contactos.items():
                        table.add_row([k, v])
                        table.add_divider()
                    print(table)
                else:
                    print("La agenda está vacia")

            case 0:
                print("📤 Saliendo de la agenda de contactos")
                break
    except ValueError:
        print("Ingrese el núemro en las opciones mostradas para editar")
