# RESUMEN COMPLETO DEL PROYECTO FASTAPI

## Introducción General

Este proyecto consiste en una API REST creada con FastAPI y Pydantic en Python.

El sistema permite gestionar:

- Clientes
- Facturas
- Transacciones

El proyecto funciona como un pequeño sistema comercial backend.

---

# ¿Qué es una API?

API significa:

```text
Application Programming Interface
```

Una API permite que diferentes programas se comuniquen entre sí.

Por ejemplo:

- una app móvil
- una página web
- un sistema de escritorio

pueden enviar solicitudes a esta API para:

- consultar información
- guardar datos
- modificar registros
- eliminar información

---

# Estructura General del Proyecto

El proyecto está dividido en dos archivos principales:

```text
main.py
clientes.py
```

---

# ARCHIVO: clientes.py

Este archivo contiene los MODELOS de datos.

Los modelos definen:

- qué información existe
- qué tipos de datos se permiten
- cómo deben estructurarse los datos

---

# IMPORTACIONES

```python
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
```

---

# ¿Qué hace cada importación?

## BaseModel

Proviene de Pydantic.

Sirve para:

- validar datos
- convertir datos automáticamente
- crear modelos estructurados

---

## Optional

Permite que un atributo sea opcional.

Ejemplo:

```python
descripcion: Optional[str] = None
```

Significa:

- el campo puede contener texto
- o puede ser None

---

## datetime

Sirve para manejar fechas y horas.

---

# MODELOS DE CLIENTE

## Clase ClienteCrear

```python
class ClienteCrear(BaseModel):
```

Esta clase representa la estructura necesaria para crear clientes.

---

## Atributos

### nombre

```python
nombre: str
```

Debe ser texto.

---

### edad

```python
edad: int
```

Debe ser un número entero.

---

### descripcion

```python
descripcion: Optional[str] = None
```

Campo opcional.

---

# ¿Por qué existe ClienteCrear?

Porque al crear clientes normalmente NO se envía el ID.

El ID suele generarse automáticamente.

---

# Clase Cliente

```python
class Cliente(ClienteCrear):
    id: int
```

Esta clase hereda todo de ClienteCrear y agrega:

```python
id: int
```

---

# ¿Qué significa herencia?

Herencia significa reutilizar características de otra clase.

Cliente hereda:

- nombre
- edad
- descripcion

y agrega:

- id

---

# MODELOS DE FACTURA

## Clase FacturaCrear

```python
class FacturaCrear(BaseModel):
```

Representa una factura sin ID.

---

## fecha

```python
fecha: datetime = datetime.now()
```

Asigna automáticamente la fecha actual.

---

## cliente

```python
cliente: Cliente
```

La factura contiene un objeto Cliente completo.

Esto crea una relación entre entidades.

---

## valortotal

```python
valortotal: float
```

Número decimal.

---

# Clase Factura

```python
class Factura(FacturaCrear):
    id: int
```

Hereda todos los campos y agrega ID.

---

# MODELOS DE TRANSACCIÓN

## Clase TransaccionCrear

```python
class TransaccionCrear(BaseModel):
```

Representa una transacción sin ID.

---

## descripcion

```python
descripcion: str
```

Texto descriptivo.

---

## factura

```python
factura: Factura
```

La transacción contiene una factura completa.

---

# Relación completa del sistema

```text
Transacción
    └── Factura
            └── Cliente
```

---

# Clase Transaccion

```python
class Transaccion(TransaccionCrear):
    id: int
```

Agrega ID a la transacción.

---

# ARCHIVO: main.py

Este archivo contiene:

- la lógica de la API
- los endpoints
- las operaciones CRUD

---

# IMPORTACIONES

```python
from fastapi import FastAPI, HTTPException
```

---

# FastAPI

FastAPI es un framework backend moderno para Python.

Permite crear APIs rápidamente.

---

# HTTPException

Sirve para devolver errores HTTP.

Ejemplo:

```python
raise HTTPException(
    status_code=404,
    detail="Cliente no encontrado"
)
```

---

# IMPORTACIÓN DE MODELOS

```python
from clientes import (
    Cliente,
    ClienteCrear,
    Factura,
    FacturaCrear,
    Transaccion,
    TransaccionCrear
)
```

Importa todas las clases definidas en clientes.py.

---

# CREACIÓN DE LA APP

```python
app = FastAPI()
```

Aquí se crea la aplicación principal.

---

# LISTAS EN MEMORIA

```python
lista_clientes = []
lista_facturas = []
lista_transacciones = []
```

Funcionan como bases de datos temporales.

---

# Problema importante

Los datos NO son permanentes.

Si el servidor se reinicia:

- todo se pierde

---

# ENDPOINTS

## ¿Qué es un endpoint?

Es una ruta accesible mediante HTTP.

Ejemplo:

```python
@app.get("/clientes")
```

---

# Endpoint raíz

```python
@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}
```

---

# CRUD DE CLIENTES

CRUD significa:

- Create
- Read
- Update
- Delete

---

# VER CLIENTES

```python
@app.get("/clientes")
def listar_clientes():
    return lista_clientes
```

Devuelve toda la lista.

---

# VER CLIENTE POR ID

```python
@app.get("/clientes/{id}")
def obtener_cliente(id: int):
```

Busca cliente específico.

---

# ¿Cómo funciona?

## Loop for

```python
for cliente in lista_clientes:
```

Recorre cada cliente.

---

## Condicional

```python
if cliente.id == id:
```

Compara IDs.

---

## Si encuentra coincidencia

Retorna el cliente.

---

## Si no encuentra

Lanza error 404.

---

# CREAR CLIENTE

```python
@app.post("/clientes")
def crear_cliente(cliente: Cliente):
```

---

# Flujo interno

1. FastAPI recibe JSON
2. Pydantic valida datos
3. Se crea objeto Cliente
4. append() lo agrega a la lista
5. se devuelve respuesta

---

# append()

```python
lista_clientes.append(cliente)
```

Agrega elemento al final de la lista.

---

# EDITAR CLIENTE

```python
@app.put("/clientes/{id}")
```

Actualiza cliente existente.

---

# enumerate()

```python
for index, cliente in enumerate(lista_clientes):
```

Devuelve:

- índice
- objeto

---

# Cliente actualizado

```python
cliente_actualizado = Cliente(
    id=id,
    nombre=datos_actualizados.nombre,
    edad=datos_actualizados.edad,
    descripcion=datos_actualizados.descripcion
)
```

---

# Reemplazo

```python
lista_clientes[index] = cliente_actualizado
```

Sobrescribe el cliente viejo.

---

# ELIMINAR CLIENTE

```python
@app.delete("/clientes/{id}")
```

---

# pop()

```python
lista_clientes.pop(index)
```

Elimina elemento por posición.

---

# FACTURAS

Funcionan exactamente igual que clientes.

---

# CREAR FACTURA

```python
@app.post("/facturas")
```

Guarda factura en:

```python
lista_facturas
```

---

# TRANSACCIONES

También funcionan igual.

---

# Relación completa

```text
Cliente
   ↓
Factura
   ↓
Transacción
```

---

# CONCEPTOS FUNDAMENTALES APRENDIDOS

Este proyecto utiliza MUCHOS conceptos importantes:

- Variables
- Funciones
- Clases
- Objetos
- Herencia
- Loops
- Condicionales
- APIs REST
- JSON
- Validación
- HTTP
- CRUD

---

# Métodos HTTP utilizados

## GET

Obtener información.

---

## POST

Crear información.

---

## PUT

Actualizar información.

---

## DELETE

Eliminar información.

---

# ¿Por qué funciona el proyecto?

El proyecto funciona porque:

1. FastAPI recibe solicitudes HTTP
2. Pydantic valida datos
3. Las funciones procesan información
4. Las listas almacenan objetos
5. FastAPI devuelve respuestas JSON

---

# Flujo completo de una petición

Ejemplo:

```http
POST /clientes
```

---

# Flujo interno

1. Cliente envía JSON
2. FastAPI recibe datos
3. Pydantic valida
4. Se crea objeto Cliente
5. append() guarda objeto
6. Se devuelve respuesta

---

# Ejemplo real

## Entrada

```json
{
  "id": 1,
  "nombre": "Oscar",
  "edad": 20
}
```

---

# Transformación

```text
JSON → Objeto Python → Lista → JSON
```

---

# Problemas actuales del proyecto

## 1. No usa base de datos real

Actualmente usa listas.

---

## 2. IDs manuales

No hay autoincremento automático.

---

## 3. No hay autenticación

Cualquier persona podría usar la API.

---

## 4. No hay persistencia

Los datos se pierden al reiniciar.

---

# Mejoras futuras recomendadas

- SQLite
- PostgreSQL
- SQLAlchemy
- JWT
- Relaciones reales
- Validaciones avanzadas

---

# Resumen Final

Este proyecto es un backend CRUD construido con FastAPI y Pydantic.

Permite:

- gestionar clientes
- crear facturas
- registrar transacciones

Además enseña conceptos fundamentales de backend moderno:

- APIs REST
- validación de datos
- programación orientada a objetos
- CRUD
- loops
- condicionales
- listas
- relaciones entre entidades
- manejo de errores HTTP

