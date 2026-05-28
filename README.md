# proyecto_clientes — API REST con FastAPI

**Estudiante:** Oscar Andrés Navarro Ochoa  
**Ficha:** 3407184  
**Programa:** Teleinformática y Bases de Datos — SENA

---

## Estructura de carpetas

```
proyecto_clientes/
├── app/
│   ├── __init__.py         # Archivo vacío para que Python reconozca el módulo
│   ├── main.py             # Punto de entrada de la API
│   ├── database.py         # Configuración de la conexión a la base de datos
│   ├── models/
│   │   ├── __init__.py
│   │   ├── clientes.py     # Modelos de Cliente (Pydantic)
│   │   └── facturas.py     # Modelos de Factura y Transacción (Pydantic)
│   └── routers/
│       ├── __init__.py
│       └── clientes.py     # Endpoints o rutas (APIRouter)
├── .venv                   # Entorno virtual
├── requirements.txt        # Dependencias del proyecto
└── README.md
```

---

## ¿Qué se desarrolló?

Se construyó una API REST usando **FastAPI** y **Python** con los siguientes recursos y operaciones:

### Clientes
- `GET /clientes` — Lista todos los clientes
- `GET /clientes/{id}` — Obtiene un cliente por su id
- `POST /clientes` — Crea un nuevo cliente
- `PUT /clientes/{id}` — Edita un cliente existente
- `DELETE /clientes/{id}` — Elimina un cliente

### Facturas
- `GET /facturas` — Lista todas las facturas
- `GET /facturas/{id}` — Obtiene una factura por su id
- `POST /facturas` — Crea una nueva factura
- `PUT /facturas/{id}` — Edita una factura existente
- `DELETE /facturas/{id}` — Elimina una factura

### Transacciones
- `GET /transacciones` — Lista todas las transacciones
- `GET /transacciones/{id}` — Obtiene una transacción por su id
- `POST /transacciones` — Crea una nueva transacción
- `PUT /transacciones/{id}` — Edita una transacción existente
- `DELETE /transacciones/{id}` — Elimina una transacción

### Modelos creados (`clientes.py`)

| Modelo | Atributos |
|---|---|
| `ClienteCrear` | nombre, edad, descripcion |
| `Cliente` | id, nombre, edad, descripcion |
| `FacturaCrear` | fecha, cliente, lista_transacciones + método valor_total() |
| `Factura` | id, fecha, cliente, lista_transacciones |
| `TransaccionCrear` | factura_id, valor_unitario, cantidad |
| `Transaccion` | id, factura_id, valor_unitario, cantidad |

---

## Cómo descargar y activar el entorno virtual

### 1. Clonar o descargar el proyecto

Si tienes Git instalado:
```bash
git clone <url-del-repositorio>
cd proyecto_clientes
```

O simplemente descarga el ZIP y descomprímelo.

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

**En Windows:**
```bash
.venv\Scripts\activate
```


Sabrás que está activo porque verás `(.venv)` al inicio de tu terminal.

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la API

```bash
uvicorn app.main:app --reload
```

