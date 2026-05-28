from pydantic import BaseModel

class Factura(BaseModel):

    id:int
    fecha:str
    cliente:int

    lista_transacciones:list[int]=[]

    def valor_total(self):

        return 0