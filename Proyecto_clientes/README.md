# Sistema de Gestión de Clientes, Facturas y Transacciones

API REST desarrollada con FastAPI y SQLite para gestionar clientes, facturas y transacciones.

## 🚀 Inicio Rápido

El servidor ya está corriendo en: **http://localhost:8000**

Documentación interactiva: **http://localhost:8000/docs**

---

## 📊 Estructura de la Base de Datos

### Tablas y Conexiones

```
CLIENTES (id, nombre, email)
    ↓ (1:N)
FACTURAS (id, numero, fecha, cliente_id)
    ↓ (1:N)
TRANSACCIONES (id, valor_unitario, cantidad, factura_id)
```

**Conexiones:**
- Un **Cliente** puede tener muchas **Facturas**
- Una **Factura** pertenece a un solo **Cliente**
- Una **Factura** puede tener muchas **Transacciones**
- Una **Transacción** pertenece a una sola **Factura**

---

## 🔗 Cómo Funcionan las Conexiones

### 1. CLIENTES
**Tabla:** `clientes`
- `id` (PRIMARY KEY) - Identificador único
- `nombre` - Nombre del cliente
- `email` - Correo electrónico (único)

**Flujo:**
1. Crea un cliente → Obtienes un `id` (ej: id=1)
2. Ese `id` se usa en facturas como `cliente_id`

### 2. FACTURAS
**Tabla:** `facturas`
- `id` (PRIMARY KEY) - Identificador único
- `numero` - Número de factura
- `fecha` - Fecha de la factura
- `cliente_id` (FOREIGN KEY) → Conecta con `clientes.id`

**Flujo:**
1. Crea una factura con `cliente_id=1` (del cliente que creaste)
2. Esa factura pertenece al cliente con id=1
3. Obtienes un `id` de factura (ej: id=1)
4. Ese `id` se usa en transacciones como `factura_id`

### 3. TRANSACCIONES
**Tabla:** `transacciones`
- `id` (PRIMARY KEY) - Identificador único
- `valor_unitario` - Precio por unidad
- `cantidad` - Cantidad de items
- `factura_id` (FOREIGN KEY) → Conecta con `facturas.id`

**Flujo:**
1. Crea una transacción con `factura_id=1` (de la factura que creaste)
2. Esa transacción pertenece a la factura con id=1

---

## 📝 Flujo Completo de Uso

### Ejemplo Práctico:

```javascript
// PASO 1: Crear un cliente
POST /clientes
{
  "id": 1,
  "nombre": "Juan Pérez",
  "email": "juan@example.com"
}
// Respuesta: Cliente creado con id=1

// PASO 2: Crear una factura para ese cliente
POST /facturas
{
  "id": 1,
  "numero": "FAC-001",
  "fecha": "2024-01-15",
  "cliente_id": 1  // ← ID del cliente del paso 1
}
// Respuesta: Factura creada con id=1

// PASO 3: Crear transacciones para esa factura
POST /transacciones
{
  "id": 1,
  "valor_unitario": 100.00,
  "cantidad": 2,
  "factura_id": 1  // ← ID de la factura del paso 2
}
// Respuesta: Transacción creada con id=1
```

---

## 🛠️ Endpoints Disponibles

### CLIENTES
- `GET /clientes` - Listar todos los clientes
- `POST /clientes` - Crear nuevo cliente
- `GET /clientes/{id}` - Obtener cliente por ID
- `PUT /clientes/{id}` - Actualizar cliente
- `DELETE /clientes/{id}` - Eliminar cliente (y sus facturas/transacciones en cascada)

### FACTURAS
- `GET /facturas` - Listar todas las facturas
- `POST /facturas` - Crear nueva factura
- `GET /facturas/{id}` - Obtener factura por ID
- `PUT /facturas/{id}` - Actualizar factura
- `DELETE /facturas/{id}` - Eliminar factura (y sus transacciones en cascada)

### TRANSACCIONES
- `GET /transacciones` - Listar todas las transacciones
- `POST /transacciones` - Crear nueva transacción
- `GET /transacciones/{id}` - Obtener transacción por ID
- `PUT /transacciones/{id}` - Actualizar transacción
- `DELETE /transacciones/{id}` - Eliminar transacción

---

## ⚙️ Características

- ✅ **Auto-inicialización**: La base de datos se crea automáticamente al iniciar
- ✅ **Llaves foráneas**: Las relaciones entre tablas están activas
- ✅ **CASCADE DELETE**: Al eliminar un cliente se eliminan sus facturas y transacciones
- ✅ **Validación**: Los IDs deben ser únicos y las relaciones válidas
- ✅ **Documentación automática**: Swagger UI en /docs
- ✅ **Organización**: Endpoints agrupados por categorías en la documentación

---

## 🔍 Reglas de Negocio

1. **IDs únicos**: Cada cliente, factura y transacción debe tener un ID único
2. **Emails únicos**: No se pueden repetir emails de clientes
3. **Relaciones válidas**: 
   - No puedes crear una factura con un `cliente_id` que no existe
   - No puedes crear una transacción con un `factura_id` que no existe
4. **Eliminación en cascada**:
   - Al eliminar un cliente → se eliminan todas sus facturas
   - Al eliminar una factura → se eliminan todas sus transacciones

---

## 📦 Estructura del Proyecto

```
Proyecto_clientes/
├── app/
│   ├── main.py              # API endpoints
│   ├── database.py          # Configuración de base de datos
│   └── modelos/
│       ├── clientes.py      # Modelo Cliente
│       ├── facturas.py      # Modelo Factura
│       └── transacciones.py # Modelo Transaccion
├── sena_proyecto.db         # Base de datos SQLite
└── requirements.txt         # Dependencias
```

---

## 🎯 Todo Está Listo

El sistema está completamente funcional:
- ✅ Base de datos creada con 3 tablas relacionadas
- ✅ 15 endpoints funcionando (5 por cada entidad)
- ✅ Servidor corriendo en puerto 8000
- ✅ Documentación interactiva disponible
- ✅ Conexiones entre tablas configuradas
- ✅ Validaciones implementadas

**Accede a http://localhost:8000/docs para comenzar a usar la API**