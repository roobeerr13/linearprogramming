from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Madera(Base):
    __tablename__ = 'madera'

    id = Column(Integer, primary_key=True, autoincrement=True)
    unidad = Column(String, nullable=False)
    comida = Column(Integer, nullable=False)
    madera = Column(Integer, nullable=False)
    oro = Column(Integer, nullable=False)
    poder = Column(Integer, nullable=False)

    def __str__(self):
        return f"Unidad: {self.unidad}, 🌾Comida: {self.comida}, 🪵Madera: {self.madera}, 🪙Oro: {self.oro}, 💪Poder: {self.poder}"

# Ejemplo de configuración de la base de datos
# engine = create_engine('sqlite:///madera.db')
# Base.metadata.create_all(engine)