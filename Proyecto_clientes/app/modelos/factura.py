from pydantic import BaseModel
from typing import Optional


class FacturaCreate(BaseModel):
    """Modelo para crear una factura"""
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
    cliente_nombre: str
    transacciones: list[dict] = []
    valor_total: float = 0.0

    class Config:
        from_attributes = True

    @classmethod
    def from_orm_factura(cls, factura_orm):
        """Crea un FacturaDB desde un FacturaORM"""
        transacciones_list = []
        for t in factura_orm.transacciones:
            transacciones_list.append({
                "id": t.id,
                "descripcion": t.descripcion,
                "valor_unitario": t.valor_unitario,
                "cantidad": t.cantidad,
                "subtotal": t.valor_unitario * t.cantidad
            })
        
        return cls(
            id=factura_orm.id,
            numero=factura_orm.numero,
            fecha=factura_orm.fecha,
            cliente_id=factura_orm.cliente_id,
            cliente_nombre=factura_orm.cliente.nombre,
            transacciones=transacciones_list,
            valor_total=factura_orm.valor_total()
        )
