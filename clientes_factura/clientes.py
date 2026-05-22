from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ClienteCrear(BaseModel):
    nombre: str
    edad: int
    descripcion: Optional[str] = None

class Cliente(ClienteCrear):
    id: int

# MODELOS FACTURA

class FacturaCrear(BaseModel):
    fecha: datetime = datetime.now()
    cliente: Cliente
    valortotal: float

class Factura(FacturaCrear):
    id: int

# MODELOS TRANSACCION

class TransaccionCrear(BaseModel):
    descripcion: str
    factura: Factura


class Transaccion(TransaccionCrear):
    id: int