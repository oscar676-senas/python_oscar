# ============================================================
# ARCHIVO PRINCIPAL: main.py
# PROPÓSITO: Punto de entrada de la aplicación.
# En cualquier proyecto Python, main.py es el archivo que
# se ejecuta primero. Contiene el menú principal y coordina
# los demás módulos.
# ============================================================

# ------------------------------------------------------------
# IMPORTACIONES DE MÓDULOS PROPIOS
# Importamos las funciones que definimos en notas.py e historial.py.
# 'from modulo import función' trae solo lo que necesitamos.
# Esto es modularidad: cada archivo tiene una responsabilidad.
# ------------------------------------------------------------
from notas     import crear_nota, ver_notas
from historial import guardar_en_historial, ver_historial, limpiar_historial


def mostrar_menu():
    """
    Función que imprime el menú de opciones en pantalla.
    Se define como función separada para no repetir el mismo
    bloque de print() cada vez que queramos mostrar el menú.
    Principio DRY: Don't Repeat Yourself (No te repitas).
    """
    print("\n")
    print("  ╔════════════════════════════════════╗")
    print("  ║     📓  AGENDA DE NOTAS  📓        ║")
    print("  ╠════════════════════════════════════╣")
    print("  ║  1. ✏️  Crear nota                 ║")
    print("  ║  2. 👁️  Ver notas                  ║")
    print("  ║  3. 📋  Ver historial de notas     ║")
    print("  ║  4. 🗑️  Limpiar historial          ║")
    print("  ║  5. 🚪  Salir                      ║")
    print("  ╚════════════════════════════════════╝")
    print("  Elige una opción: ", end="")
    # end="" evita que print() haga salto de línea al final,
    # así el cursor queda en la misma línea esperando input.


def main():
    """
    Función principal que contiene el ciclo del programa.
    
    Usamos un bucle 'while True' (bucle infinito) porque la
    agenda debe seguir mostrando el menú después de cada acción,
    hasta que el usuario decida salir con la opción 5.
    
    'break' rompe el bucle y termina el programa cuando se elige
    la opción de salir.
    """

    print("\n  Bienvenido/a a tu Agenda de Notas 📓")
    print("  Desarrollado con Python — SENA Teleinformática")

    # ---------------------------------------------------------
    # BUCLE PRINCIPAL: se repite indefinidamente hasta que el
    # usuario elija "Salir". Esto es el corazón del programa.
    # ---------------------------------------------------------
    while True:

        mostrar_menu()           # Mostramos las opciones
        opcion = input().strip() # Leemos la opción del usuario

        # -----------------------------------------------------
        # OPCIÓN 1: Crear nota
        # Llamamos a crear_nota() del módulo notas.py.
        # Esta función retorna la nota creada (un diccionario)
        # o None si el usuario canceló (título vacío).
        # Luego llamamos a guardar_en_historial() para que
        # quede registrada en el archivo .txt.
        # -----------------------------------------------------
        if opcion == "1":
            nota_nueva = crear_nota()

            # Solo guardamos en historial si se creó correctamente
            # (si no fue cancelada, es decir, si no es None)
            if nota_nueva is not None:
                guardar_en_historial(nota_nueva)

        # -----------------------------------------------------
        # OPCIÓN 2: Ver notas
        # Llama a ver_notas() del módulo notas.py que lee
        # la lista en memoria y la muestra formateada.
        # -----------------------------------------------------
        elif opcion == "2":
            ver_notas()

        # -----------------------------------------------------
        # OPCIÓN 3: Ver historial
        # Llama a ver_historial() del módulo historial.py que
        # lee y muestra el archivo historial_notas.txt.
        # -----------------------------------------------------
        elif opcion == "3":
            ver_historial()

        # -----------------------------------------------------
        # OPCIÓN 4: Limpiar historial (función extra)
        # Permite borrar el archivo .txt para empezar de cero.
        # Pide confirmación dentro de la función antes de borrar.
        # -----------------------------------------------------
        elif opcion == "4":
            limpiar_historial()

        # -----------------------------------------------------
        # OPCIÓN 5: Salir
        # 'break' interrumpe el while True y el programa termina.
        # -----------------------------------------------------
        elif opcion == "5":
            print("\n  👋 ¡Hasta luego! Tu agenda se ha cerrado.")
            print("  (Tus notas del historial siguen guardadas en el .txt)\n")
            break  # Salimos del bucle while True → fin del programa

        # -----------------------------------------------------
        # OPCIÓN INVÁLIDA: cualquier cosa diferente a 1-5
        # En lugar de crashear, informamos al usuario.
        # -----------------------------------------------------
        else:
            print(f"\n  ⚠️  Opción '{opcion}' no válida. Elige entre 1 y 5.")


# ------------------------------------------------------------
# BLOQUE ESPECIAL: if __name__ == "__main__"
#
# Esta es una convención fundamental de Python.
# __name__ es una variable especial que Python asigna a cada
# archivo automáticamente:
#   - Si el archivo se EJECUTA directamente → __name__ == "__main__"
#   - Si el archivo es IMPORTADO por otro → __name__ == "main"
#
# Esto permite que main() solo se ejecute cuando corremos
# este archivo directamente (python main.py), pero NO cuando
# otro archivo lo importa como módulo.
# Es buena práctica siempre incluirlo en el archivo principal.
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
