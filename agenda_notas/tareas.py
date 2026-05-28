notas = []

def crear_nota():
    tarea = input("Ingrese la tarea: ")
    fecha_inicio = input("Fecha inicio: ")
    fecha_final = input("Fecha final: ")
    estado = input("Estado (pendiente/realizado): ")

    nota = {
        "tarea": tarea,
        "inicio": fecha_inicio,
        "final": fecha_final,
        "estado": estado
    }

    notas.append(nota)

    # Guardar en archivo
    with open("historial.txt", "a") as archivo:
        archivo.write(f"{nota}\n")

    print("Nota guardada correctamente")


def ver_notas():
    if len(notas) == 0:
        print("No hay notas")
    else:
        for i, nota in enumerate(notas):
            print(f"{i+1}. {nota}")


def ver_historial():
    try:
        with open("historial.txt", "r") as archivo:
            contenido = archivo.read()
            print("\n--- HISTORIAL ---")
            print(contenido)
    except FileNotFoundError:
        print("No existe historial aún")
