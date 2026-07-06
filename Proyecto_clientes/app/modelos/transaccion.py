from pydantic import BaseModel
from typing import Optional


class TransaccionCreate(BaseModel):
    """Modelo para crear una transacción"""
    factura_id: int
    valor_unitario: float
    cantidad: int
    descripcion: str


class TransaccionUpdate(BaseModel):
    """Modelo para actualizar una transacción"""
    valor_unitario: Optional[float] = None
    cantidad: Optional[int] = None
    descripcion: Optional[str] = None


class TransaccionDB(BaseModel):
    """Modelo para devolver una transacción desde la base de datos"""
    id: int
    valor_unitario: float
    cantidad: int
    descripcion: str
    factura_id: int
    subtotal: float = 0.0

    class Config:
        from_attributes = True
