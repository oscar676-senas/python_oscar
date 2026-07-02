from pydantic import BaseModel
from typing import Optional


class FacturaCreate(BaseModel):
    """Modelo para crear una factura"""
    cliente: int
    numero: str
    fecha: str


class FacturaUpdate(BaseModel):
    """Modelo para actualizar una factura"""
    cliente: Optional[int] = None
    numero: Optional[str] = None
    fecha: Optional[str] = None


class FacturaDB(BaseModel):
    """Modelo para devolver una factura desde la base de datos"""
    id: int
    numero: str
    fecha: str
    cliente_id: int

    class Config:
        from_attributes = True

    @classmethod
    def from_orm_factura(cls, factura_orm):
        """Crea un FacturaDB desde un FacturaORM"""
        return cls(
            id=factura_orm.id,
            numero=factura_orm.numero,
            fecha=factura_orm.fecha,
            cliente_id=factura_orm.cliente_id,
        )

    def valor_total(self):
        """Calcula el valor total (este método se usa en los endpoints)"""
        # Nota: El valor total se calcula en el endpoint con las transacciones
        return 0.0