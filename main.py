from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "Hola mundo"}

#APLICACIÓN DE CLIENTES
lista_clientes = [] # datos de la base de datos

#model - modelos
class Cliente(BaseModel):
        id : int
        nombre : str
        edad : int
        descripcion : str | None=None

@app.get("/clientes")
def listar_clientes():
        return {"Clientes": lista_clientes}

@app.post("/clientes")
def crear_clientes(datos_clientes: Cliente):
        lista_clientes.append(datos_clientes)
        return {"mensaje": "Cliente creado"}

#RETO: Crear un nuevo endpoint y que me retorne un solo cliente

@app.get("/clientes, {id}")
def obtener(id : int):

        for cliente in listar_clientes:
               
               if cliente.id == id:
                     return {"cliente" : cliente}