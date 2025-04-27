from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
engine = create_engine('sqlite:///unidades.db')
Base = declarative_base()

# Definición del modelo
class Unidad(Base):
    __tablename__ = 'unidades'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    oro = Column(Integer, nullable=False)

# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Datos de las unidades
unidades = [
    {"nombre": "Espadachín", "oro": 70},
    {"nombre": "Bowman", "oro": 40},
    {"nombre": "Jinete", "oro": 100},
]

# Insertar los datos en la base de datos
for unidad in unidades:
    nueva_unidad = Unidad(nombre=unidad["nombre"], oro=unidad["oro"])
    session.add(nueva_unidad)

# Confirmar los cambios
session.commit()

# Cerrar la sesión
session.close()