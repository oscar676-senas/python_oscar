from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class ClienteORM(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Relaciones
    facturas = relationship("FacturaORM", back_populates="cliente", cascade="all, delete-orphan")


class FacturaORM(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, nullable=False)
    fecha = Column(String, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id", ondelete="CASCADE"), nullable=False)

    # Relaciones
    cliente = relationship("ClienteORM", back_populates="facturas")
    transacciones = relationship("TransaccionORM", back_populates="factura", cascade="all, delete-orphan")

    def valor_total(self):
        """Calcula el valor total de la factura sumando todas las transacciones"""
        return sum(t.valor_unitario * t.cantidad for t in self.transacciones)


class TransaccionORM(Base):
    __tablename__ = "transacciones"

    id = Column(Integer, primary_key=True, index=True)
    valor_unitario = Column(Float, nullable=False)
    cantidad = Column(Integer, nullable=False)
    descripcion = Column(String, nullable=False)
    factura_id = Column(Integer, ForeignKey("facturas.id", ondelete="CASCADE"), nullable=False)

    # Relaciones
    factura = relationship("FacturaORM", back_populates="transacciones")
