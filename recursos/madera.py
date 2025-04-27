from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
engine = create_engine('sqlite:///recursos.db')
Base = declarative_base()

# Definición del modelo
class Madera(Base):
    __tablename__ = 'madera'
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False)

# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Datos iniciales de madera
maderas = [
    {"tipo": "madera", "cantidad": 50}
]

# Insertar los datos en la base de datos
for madera in maderas:
    nueva_madera = Madera(tipo=madera["tipo"], cantidad=madera["cantidad"])
    session.add(nueva_madera)

# Confirmar los cambios
session.commit()
session.close()