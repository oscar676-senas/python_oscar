from fastapi import FastAPI
from pydantic import BaseModel
from modelos.clientes import Cliente

app = FastAPI()

# --- MODELOS ---

class Factura(BaseModel):
    id: int
    cliente_id: int
    monto: float

class Transaccion(BaseModel):
    id: int
    factura_id: int
    metodo: str # Ejemplo: "Efectivo" o "Tarjeta"

# --- BASES DE DATOS TEMPORALES (LISTAS) ---

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

# --- ENDPOINTS DE CLIENTES ---

@app.get("/")
def inicio():
    return {"mensaje": "Aprendiendo fastapi"}

@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}

@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return {"mensaje": "Cliente creado con éxito", "cliente": datos_cliente}

@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            return {"Cliente encontrado": cliente}
    return {"error": "No se encontró un cliente con ese ID"}

@app.put("/cliente/{id}")
def editar_cliente(id: int, datos_cliente: Cliente):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            lista_clientes[i] = datos_cliente
            lista_clientes[i].id = id 
            return {"mensaje": "Actualizado", "cliente": lista_clientes[i]}
    return {"error": "No encontrado"}

@app.delete("/cliente/{id}")
def eliminar_cliente(id: int):
    for c in lista_clientes:
        if c.id == id:
            lista_clientes.remove(c)
            return {"mensaje": "Eliminado", "cliente_eliminado": c}
    return {"error": "No encontrado"}

# --- ENDPOINTS DE FACTURAS ---

@app.post("/factura")
def crear_factura(nueva_factura: Factura):
    lista_facturas.append(nueva_factura)
    return {
        "mensaje": "Factura creada correctamente",
        "factura": nueva_factura
    }

# --- ENDPOINTS DE TRANSACCIONES */

@app.post("/transacciones")
def crear_transaccion(nueva_transaccion: Transaccion):
    lista_transacciones.append(nueva_transaccion)
    return {
        "mensaje": "Transacción creada correctamente",
        "transaccion": nueva_transaccion
    }