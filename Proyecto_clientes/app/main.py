from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.modelos.clientes import Cliente
from app.modelos.facturas import Factura
from app.modelos.transacciones import Transaccion

app = FastAPI()

# ==========================================
# 1. MODELOS DE DATOS (CONECTADOS POR ID)
# ==========================================

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str

class Factura(BaseModel):
    id: int
    numero: str
    cliente_id: int  # <-- Conecta la Factura con un Cliente existente

class Transaccion(BaseModel):
    id: int
    valor_unitario: float
    cantidad: int
    factura_id: int  # <-- Conecta la Transacción con una Factura existente


# ==========================================
# 2. ALMACENAMIENTO TEMPORAL (EN MEMORIA)
# ==========================================

lista_clientes: List[Cliente] = []
lista_facturas: List[Factura] = []
lista_transacciones: List[Transaccion] = []


# ==========================================
# 3. ENDPOINTS PARA CLIENTES
# ==========================================

@app.get("/")
def inicio():
    return {"mensaje": "Aprendiendo FastAPI - Sistema Conectado"}

@app.get("/clientes")
def listar_clientes():
    return {"clientes": lista_clientes}

@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):
    # Validar que el ID no esté duplicado
    if any(c.id == datos_cliente.id for c in lista_clientes):
        raise HTTPException(status_code=400, detail="El ID del cliente ya existe")
    
    lista_clientes.append(datos_cliente)
    return {"mensaje": "cliente creado", "cliente": datos_cliente}

@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            return {"cliente": cliente}
    raise HTTPException(status_code=404, detail="cliente no encontrado")

@app.put("/clientes/{id}")
def editar_cliente(id: int, datos_cliente: Cliente):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            datos_cliente.id = id
            lista_clientes[i] = datos_cliente
            return {"mensaje": "actualizado", "cliente": lista_clientes[i]}
    raise HTTPException(status_code=404, detail="no encontrado")

@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            lista_clientes.remove(cliente)
            # Opcional: Aquí podrías borrar también sus facturas en cascada
            return {"mensaje": "eliminado", "cliente": cliente}
    raise HTTPException(status_code=404, detail="no encontrado")


# ==========================================
# 4. ENDPOINTS PARA FACTURAS
# ==========================================

@app.get("/facturas")
def listar_facturas():
    return {"facturas": lista_facturas}

@app.post("/facturas")
def crear_factura(factura: Factura):
    # REQUISITO: El cliente_id debe existir en la lista de clientes
    if not any(c.id == factura.cliente_id for c in lista_clientes):
        raise HTTPException(status_code=400, detail=f"No existe un cliente con el ID {factura.cliente_id}")
    
    # Validar ID duplicado de factura
    if any(f.id == factura.id for f in lista_facturas):
        raise HTTPException(status_code=400, detail="El ID de la factura ya existe")

    lista_facturas.append(factura)
    return {"mensaje": "factura creada", "factura": factura}

@app.put("/facturas/{id}")
def editar_factura(id: int, datos: Factura):
    # Revalidar que el cliente exista si se cambia el cliente de la factura
    if not any(c.id == datos.cliente_id for c in lista_clientes):
        raise HTTPException(status_code=400, detail=f"No existe un cliente con el ID {datos.cliente_id}")

    for i, factura in enumerate(lista_facturas):
        if factura.id == id:
            datos.id = id
            lista_facturas[i] = datos
            return {"mensaje": "Editada", "factura": datos}
    raise HTTPException(status_code=404, detail="No encontrada")

@app.delete("/facturas/{id}")
def eliminar_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            lista_facturas.remove(factura)
            return {"mensaje": "Eliminada"}
    raise HTTPException(status_code=404, detail="No encontrada")


# ==========================================
# 5. ENDPOINTS PARA TRANSACCIONES
# ==========================================

@app.get("/transacciones")
def listar_transacciones():
    return {"transacciones": lista_transacciones}

@app.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):
    # REQUISITO: El factura_id debe existir en la lista de facturas
    if not any(f.id == transaccion.factura_id for f in lista_facturas):
        raise HTTPException(status_code=400, detail=f"No existe una factura con el ID {transaccion.factura_id}")

    lista_transacciones.append(transaccion)
    return {"mensaje": "transaccion creada", "transaccion": transaccion}

@app.put("/transacciones/{id}")
def editar_transaccion(id: int, datos: Transaccion):
    if not any(f.id == datos.factura_id for f in lista_facturas):
        raise HTTPException(status_code=400, detail=f"No existe una factura con el ID {datos.factura_id}")

    for i, transaccion in enumerate(lista_transacciones):
        if transaccion.id == id:
            datos.id = id
            lista_transacciones[i] = datos
            return {"mensaje": "transaccion actualizada", "transaccion": datos}
    raise HTTPException(status_code=404, detail="no encontrada")

@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            lista_transacciones.remove(transaccion)
            return {"mensaje": "transaccion eliminada"}
    raise HTTPException(status_code=404, detail="no encontrada")

@app.get("/facturas/{factura_id}")
def obtener_factura(factura_id: int):
    for factura in lista_facturas:
        if factura.id == factura_id:
            return {"factura": factura}
    raise HTTPException(status_code=404, detail="Factura no encontrada")

@app.get("/transacciones/{transaccion_id}")
def obtener_transaccion(transaccion_id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == transaccion_id:
            return {"transaccion": transaccion}
    raise HTTPException(status_code=404, detail="Transacción no encontrada")