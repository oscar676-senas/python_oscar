from fastapi import FastAPI, HTTPException
from clientes import (
    Cliente,
    ClienteCrear,
    Factura,
    FacturaCrear,
    Transaccion,
    TransaccionCrear
)


app = FastAPI()


lista_clientes = []
lista_facturas = []
lista_transacciones = []


@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}


# CLIENTES


# VER CLIENTES
@app.get("/clientes")
def listar_clientes():
    return lista_clientes


# VER UN CLIENTE
@app.get("/clientes/{id}")
def obtener_cliente(id: int):

    for cliente in lista_clientes:

        if cliente.id == id:
            return cliente
            


    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )


# CREAR CLIENTE
@app.post("/clientes")
def crear_cliente(cliente: Cliente):

    lista_clientes.append(cliente)

    return {
        "mensaje": "Cliente creado correctamente",
        "cliente": cliente
    }


# EDITAR CLIENTE
@app.put("/clientes/{id}")
def editar_cliente(id: int, datos_actualizados: ClienteCrear):

    for index, cliente in enumerate(lista_clientes):

        if cliente.id == id:

            cliente_actualizado = Cliente(
                id=id,
                nombre=datos_actualizados.nombre,
                edad=datos_actualizados.edad,
                descripcion=datos_actualizados.descripcion
            )

            lista_clientes[index] = cliente_actualizado

            return {
                "mensaje": "Cliente actualizado",
                "cliente": cliente_actualizado
            }

    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )


# ELIMINAR CLIENTE
@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):

    for index, cliente in enumerate(lista_clientes):

        if cliente.id == id:

            lista_clientes.pop(index)

            return {
                "mensaje": "Cliente eliminado"
            }

    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )

# VER FACTURAS
@app.get("/facturas")
def listar_facturas():
    return lista_facturas


# CREAR FACTURA
@app.post("/facturas")
def crear_factura(factura: Factura):

    lista_facturas.append(factura)

    return {
        "mensaje": "Factura creada",
        "factura": factura
    }


# VER TRANSACCIONES
@app.get("/transacciones")
def listar_transacciones():
    return lista_transacciones


# CREAR TRANSACCION
@app.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):


    lista_transacciones.append(transaccion)


    return {
        "mensaje": "Transacción creada",
        "transaccion": transaccion
    }
    
    
@app.get("/facturas/{id}")
def obtener_factura(id: int):

    for factura in lista_facturas:

        if factura.id == id:
            return factura

    raise HTTPException(
        status_code=404,
        detail="Factura no encontrada"
    )
    
    
@app.put("/facturas/{id}")
def editar_factura(id: int, datos_actualizados: FacturaCrear):

    for index, factura in enumerate(lista_facturas):

        if factura.id == id:

            factura_actualizada = Factura(
                id=id,
                fecha=datos_actualizados.fecha,
                cliente=datos_actualizados.cliente,
                valortotal=datos_actualizados.valortotal
            )

            lista_facturas[index] = factura_actualizada

            return {
                "mensaje": "Factura actualizada",
                "factura": factura_actualizada
            }

    raise HTTPException(
        status_code=404,
        detail="Factura no encontrada"
    )
    

@app.delete("/facturas/{id}")
def eliminar_factura(id: int):

    for index, factura in enumerate(lista_facturas):

        if factura.id == id:

            lista_facturas.pop(index)

            return {
                "mensaje": "Factura eliminada"
            }

    raise HTTPException(
        status_code=404,
        detail="Factura no encontrada"
    )
    
    