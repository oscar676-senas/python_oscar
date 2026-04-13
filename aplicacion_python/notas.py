# ============================================================
# MÓDULO: notas.py
# PROPÓSITO: Contiene todas las funciones relacionadas con
# crear y ver las notas de la agenda.
# Se importa desde main.py para mantener el código organizado.
# ============================================================

# Importamos 'datetime' para registrar la fecha y hora exacta
# en que se crea cada nota. Es parte de la librería estándar
# de Python, no necesitas instalarla.
from datetime import datetime

# ------------------------------------------------------------
# LISTA GLOBAL DE NOTAS
# Una lista vacía que actúa como "base de datos en memoria".
# Mientras el programa esté corriendo, las notas se guardan aquí.
# Cuando el programa termina, esta lista se pierde (por eso
# también guardamos en archivo .txt en historial.py).
# ------------------------------------------------------------
lista_notas = []


def crear_nota():
    """
    Función para crear una nueva nota/tarea.
    
    Pide al usuario:
      - Título de la tarea
      - Fecha de inicio (formato DD/MM/AAAA)
      - Fecha final (formato DD/MM/AAAA)
      - Estado inicial (realizado / pendiente)
    
    Luego construye un diccionario con esos datos y lo agrega
    a 'lista_notas'. También retorna la nota para que
    historial.py pueda guardarla en el archivo .txt.
    """

    print("\n╔══════════════════════════════╗")
    print("║        CREAR NUEVA NOTA      ║")
    print("╚══════════════════════════════╝")

    # ---------------------------------------------------------
    # INPUT: pedimos el título.
    # .strip() elimina espacios en blanco al inicio y al final
    # por si el usuario escribe " tarea " en vez de "tarea".
    # ---------------------------------------------------------
    titulo = input("  📝 Título de la tarea : ").strip()

    # Validamos que el título no esté vacío
    if not titulo:
        print("  ⚠️  El título no puede estar vacío. Operación cancelada.")
        return None  # Salimos de la función sin crear nada

    # ---------------------------------------------------------
    # INPUT: fechas. Pedimos en formato DD/MM/AAAA porque es
    # el formato más común en Colombia y Latinoamérica.
    # ---------------------------------------------------------
    fecha_inicio = input("  📅 Fecha de inicio (DD/MM/AAAA): ").strip()
    fecha_final  = input("  📅 Fecha final     (DD/MM/AAAA): ").strip()

    # ---------------------------------------------------------
    # INPUT: estado de la tarea.
    # Usamos .lower() para aceptar "Pendiente", "PENDIENTE", etc.
    # ---------------------------------------------------------
    print("  Estado: [1] Pendiente  [2] Realizado")
    opcion_estado = input("  Elige una opción: ").strip()

    # Convertimos el número a texto descriptivo
    if opcion_estado == "2":
        estado = "Realizado"
    else:
        # Si escribe cualquier otra cosa, por defecto es Pendiente
        estado = "Pendiente"

    # ---------------------------------------------------------
    # DICCIONARIO: estructura de datos que agrupa toda la info
    # de la nota. Cada 'clave': 'valor' describe un atributo.
    # datetime.now() captura el momento exacto de creación.
    # ---------------------------------------------------------
    nota = {
        "titulo"       : titulo,
        "fecha_inicio" : fecha_inicio,
        "fecha_final"  : fecha_final,
        "estado"       : estado,
        "creada_en"    : datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # strftime formatea la fecha como texto legible:
        # %d = día, %m = mes, %Y = año, %H:%M:%S = hora
    }

    # Agregamos el diccionario a la lista global
    lista_notas.append(nota)

    print(f"\n  ✅ Nota '{titulo}' creada correctamente.")
    
    # Retornamos la nota para que historial.py la guarde en .txt
    return nota


def ver_notas():
    """
    Función para mostrar todas las notas guardadas en lista_notas.
    
    Recorre la lista con enumerate() para mostrar un número
    de ítem junto a cada nota. Si la lista está vacía, avisa
    al usuario en lugar de mostrar nada.
    """

    print("\n╔══════════════════════════════╗")
    print("║         VER MIS NOTAS        ║")
    print("╚══════════════════════════════╝")

    # Verificamos si la lista está vacía antes de recorrerla
    if not lista_notas:
        print("  📭 No hay notas registradas aún.")
        return  # Salimos de la función, no hay nada que mostrar

    # ---------------------------------------------------------
    # enumerate(lista_notas, start=1) nos da dos valores en cada
    # vuelta del for: el índice (número) y el elemento (nota).
    # start=1 hace que empiece a contar desde 1, no desde 0.
    # ---------------------------------------------------------
    for numero, nota in enumerate(lista_notas, start=1):
        print(f"\n  ── Nota #{numero} ──────────────────────")
        print(f"  📝 Título     : {nota['titulo']}")
        print(f"  📅 Inicio     : {nota['fecha_inicio']}")
        print(f"  📅 Final      : {nota['fecha_final']}")

        # Emoji dinámico según el estado de la tarea
        emoji_estado = "✅" if nota["estado"] == "Realizado" else "⏳"
        print(f"  {emoji_estado} Estado      : {nota['estado']}")
        print(f"  🕐 Creada el  : {nota['creada_en']}")

    print(f"\n  Total de notas: {len(lista_notas)}")
    # len() retorna el número de elementos en la lista
