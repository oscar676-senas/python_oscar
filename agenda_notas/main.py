from tareas import crear_nota, ver_notas, ver_historial

def menu():
    while True:
        print("\n--- AGENDA DE NOTAS ---")
        print("1. Crear nota")
        print("2. Ver notas")
        print("3. Ver historial")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_nota()
        elif opcion == "2":
            ver_notas()
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

menu()
