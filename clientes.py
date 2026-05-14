from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# --- MODELOS DE CLIENTE (Tus modelos actuales) ---
class ClienteCrear(BaseModel): 
    nombre: str
    edad: int
    descripcion: Optional[str] = None

class Cliente(ClienteCrear):
    id: int  

# --- NUEVOS MODELOS: FACTURA ---
class FacturaCrear(BaseModel):
    fecha: datetime = datetime.now() # Se asigna la fecha y hora actual automáticamente
    cliente: Cliente                 # Enlazamos el cliente completo
    valortotal: float

class Factura(FacturaCrear):
    id: int                          # ID autogenerado para la factura

# --- NUEVOS MODELOS: TRANSACCIONES ---
class TransaccionCrear(BaseModel):
    descripcion: str
    factura: Factura                 # Enlazamos la factura completa

class Transaccion(TransaccionCrear):
    id: int                          # ID autogenerado para la transacción
