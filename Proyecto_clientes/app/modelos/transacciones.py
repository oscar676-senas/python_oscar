from pydantic import BaseModel

class Transaccion(BaseModel):
    id: int
    valor_unitario: float
    cantidad: int
    factura_id: int