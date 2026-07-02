from pydantic import BaseModel, EmailStr
from typing import Optional


class ClienteCreate(BaseModel):
    """Modelo para crear un cliente"""
    nombre: str
    email: EmailStr


class ClienteUpdate(BaseModel):
    """Modelo para actualizar un cliente (todos los campos opcionales)"""
    nombre: Optional[str] = None
    email: Optional[EmailStr] = None


class ClienteDB(BaseModel):
    """Modelo para devolver un cliente desde la base de datos"""
    id: int
    nombre: str
    email: str

    class Config:
        from_attributes = True