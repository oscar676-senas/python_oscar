# ============================================================
# MÓDULO: historial.py
# PROPÓSITO: Maneja todo lo relacionado con el archivo .txt
# donde se guarda el historial permanente de notas.
# Al usar un archivo de texto, la información persiste aunque
# el programa se cierre (a diferencia de la lista en memoria).
# ============================================================

# 'os' nos permite verificar si un archivo ya existe en disco.
# También es parte de la librería estándar de Python.
import os

# ------------------------------------------------------------
# CONSTANTE: nombre del archivo donde se guarda el historial.
# Se define aquí arriba para que sea fácil cambiarlo si se
# necesita. Una constante en Python por convención se escribe
# en MAYÚSCULAS. El archivo se creará en la misma carpeta
# donde esté historial.py.
# ------------------------------------------------------------
ARCHIVO_HISTORIAL = "historial_notas.txt"


def guardar_en_historial(nota):
    """
    Guarda una nota en el archivo .txt de historial.
    
    Usa modo 'a' (append = agregar) al abrir el archivo,
    lo que significa que AGREGA al final sin borrar lo que
    ya había. Si el archivo no existe, Python lo crea
    automáticamente.
    
    Parámetro:
        nota (dict): el diccionario con los datos de la nota
                     que viene de notas.py → crear_nota()
    """

    # ---------------------------------------------------------
    # open(archivo, modo, encoding) abre el archivo.
    # Modos más usados:
    #   'r' = leer (read)
    #   'w' = escribir desde cero (write, borra todo lo anterior)
    #   'a' = agregar al final (append, no borra nada)
    # encoding='utf-8' es importante para soportar tildes (á, é)
    # y la ñ, que son comunes en español.
    #
    # El bloque 'with' cierra el archivo automáticamente al
    # terminar, aunque ocurra un error. Es la forma correcta
    # de manejar archivos en Python.
    # ---------------------------------------------------------
    with open(ARCHIVO_HISTORIAL, "a", encoding="utf-8") as archivo:

        # Escribimos una línea separadora para claridad visual
        archivo.write("=" * 45 + "\n")
        # \n es el salto de línea (Enter) dentro del archivo

        archivo.write(f"TAREA     : {nota['titulo']}\n")
        archivo.write(f"INICIO    : {nota['fecha_inicio']}\n")
        archivo.write(f"FINAL     : {nota['fecha_final']}\n")
        archivo.write(f"ESTADO    : {nota['estado']}\n")
        archivo.write(f"REGISTRADA: {nota['creada_en']}\n")
        # El bloque 'with' cierra el archivo aquí automáticamente

    print(f"  💾 Nota guardada en '{ARCHIVO_HISTORIAL}'.")


def ver_historial():
    """
    Lee y muestra todo el contenido del archivo historial_notas.txt.
    
    Primero verifica si el archivo existe. Si no existe todavía
    (nunca se ha creado una nota), avisa al usuario en lugar
    de lanzar un error.
    """

    print("\n╔══════════════════════════════╗")
    print("║      HISTORIAL DE NOTAS      ║")
    print("╚══════════════════════════════╝")

    # ---------------------------------------------------------
    # os.path.exists() retorna True si el archivo existe en
    # disco, False si no. Es buena práctica verificar antes de
    # intentar leerlo para evitar un FileNotFoundError.
    # ---------------------------------------------------------
    if not os.path.exists(ARCHIVO_HISTORIAL):
        print("  📭 Aún no hay historial guardado.")
        print(f"  (El archivo '{ARCHIVO_HISTORIAL}' no existe todavía.)")
        return

    # ---------------------------------------------------------
    # Abrimos en modo 'r' (lectura).
    # .read() lee TODO el contenido del archivo como un solo
    # string. Como el archivo puede ser largo, también podría
    # usarse .readlines() para leer línea por línea.
    # ---------------------------------------------------------
    with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    # Verificamos que el archivo no esté vacío
    if not contenido.strip():
        print("  📭 El historial está vacío.")
        return

    # Mostramos todo el contenido directamente
    print("\n" + contenido)


def limpiar_historial():
    """
    Función opcional: borra todo el historial del archivo .txt.
    Útil para hacer pruebas o reiniciar la agenda.
    Pide confirmación antes de borrar para evitar accidentes.
    """

    if not os.path.exists(ARCHIVO_HISTORIAL):
        print("  ⚠️  No hay historial que limpiar.")
        return

    confirmacion = input("  ⚠️  ¿Seguro que quieres borrar el historial? (s/n): ").lower()

    if confirmacion == "s":
        # Modo 'w' con write("") sobreescribe el archivo vacío,
        # lo que efectivamente borra todo el contenido.
        with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
            archivo.write("")
        print("  🗑️  Historial limpiado correctamente.")
    else:
        print("  ↩️  Operación cancelada.")
