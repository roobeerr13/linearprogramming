from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
engine = create_engine('sqlite:///recursos.db')
Base = declarative_base()

# Definición del modelo
class Comida(Base):
    __tablename__ = 'comida'
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False)

# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Datos iniciales de comida
comidas = [
    {"tipo": "comida", "cantidad": 100}
]

# Insertar los datos en la base de datos
for comida in comidas:
    nueva_comida = Comida(tipo=comida["tipo"], cantidad=comida["cantidad"])
    session.add(nueva_comida)

# Confirmar los cambios
session.commit()
session.close()