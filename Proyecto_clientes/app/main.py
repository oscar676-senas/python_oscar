from fastapi import FastAPI
from pydantic import BaseModel

from Proyecto_clientes.app.modelos.clientes import Cliente
from Proyecto_clientes.app.modelos.facturas import Factura

app = FastAPI()

# MODELO TRANSACCIONES

class Transaccion(BaseModel):

    id:int

    valor_unitario:float

    cantidad:int

    factura_id:int

# LISTAS TEMPORALES

lista_clientes=[]

lista_facturas=[]

lista_transacciones=[]


# CLIENTES

@app.get("/")
def inicio():

    return {"mensaje":"Aprendiendo FastAPI"}


@app.get("/clientes")
def listar_clientes():

    return {"clientes":lista_clientes}


@app.post("/clientes")
def crear_cliente(datos_cliente:Cliente):

    lista_clientes.append(datos_cliente)

    return {

        "mensaje":"cliente creado",
        "cliente":datos_cliente

    }


@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id:int):

    for cliente in lista_clientes:

        if cliente.id == cliente_id:

            return {"cliente":cliente}

    return {"error":"cliente no encontrado"}


@app.put("/cliente/{id}")
def editar_cliente(id:int, datos_cliente:Cliente):

    for i, cliente in enumerate(lista_clientes):

        if cliente.id == id:

            lista_clientes[i]=datos_cliente

            lista_clientes[i].id=id

            return {

                "mensaje":"actualizado",
                "cliente":lista_clientes[i]

            }

    return {"error":"no encontrado"}


@app.delete("/cliente/{id}")
def eliminar_cliente(id:int):

    for cliente in lista_clientes:

        if cliente.id == id:

            lista_clientes.remove(cliente)

            return {

                "mensaje":"eliminado",
                "cliente":cliente

            }

    return {"error":"no encontrado"}


# FACTURAS

@app.get("/facturas")
def listar_facturas():

    return {

        "facturas":lista_facturas
    }

@app.post("/factura")
def crear_factura(factura:Factura):

    lista_facturas.append(factura)

    return {

        "mensaje":"factura creada",
        "factura":factura

    }


# TRANSACCIONES

@app.get("/transacciones")
def listar_transacciones():

    return {

        "transacciones":lista_transacciones
    }

@app.post("/transacciones")
def crear_transaccion(transaccion:Transaccion):

    lista_transacciones.append(transaccion)

    return {

        "mensaje":"transaccion creada",

        "transaccion":transaccion

    }
@app.put("/transacciones/{id}")
def editar_transaccion(id:int, datos:Transaccion):

    for i, transaccion in enumerate(lista_transacciones):

        if transaccion.id == id:

            lista_transacciones[i]=datos

            return {

                "mensaje":"transaccion actualizada",

                "transaccion":datos

            }

    return {

        "error":"no encontrada"

    }
@app.delete("/transacciones/{id}")
def eliminar_transaccion(id:int):

    for transaccion in lista_transacciones:

        if transaccion.id == id:

            lista_transacciones.remove(transaccion)

            return {

                "mensaje":"transaccion eliminada"

            }

    return {

        "error":"no encontrada"

    }

# EDITAR FACTURA
@app.put("/facturas/{id}")
def editar_factura(id: int, datos: Factura):
    for i, factura in enumerate(lista_facturas):
        if factura.id == id:
            lista_facturas[i] = datos
            return {"mensaje": "Editada", "factura": datos}
    return {"error": "No encontrada"}

# ELIMINAR FACTURA
@app.delete("/facturas/{id}")
def eliminar_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            lista_facturas.remove(factura)
            return {"mensaje": "Eliminada"}
    return {"error": "No encontrada"}