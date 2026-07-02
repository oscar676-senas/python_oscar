from pydantic import BaseModel
from typing import Optional


class TransaccionCreate(BaseModel):
    """Modelo para crear una transacción"""
    valor_unitario: float
    cantidad: int


class TransaccionUpdate(BaseModel):
    """Modelo para actualizar una transacción"""
    valor_unitario: Optional[float] = None
    cantidad: Optional[int] = None


class TransaccionDB(BaseModel):
    """Modelo para devolver una transacción desde la base de datos"""
    id: int
    valor_unitario: float
    cantidad: int
    factura_id: int

    class Config:
        from_attributes = True