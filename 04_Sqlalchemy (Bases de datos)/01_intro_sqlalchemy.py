from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
import os

print("--- 🗄️ SESIÓN 7: BASES DE DATOS CON SQLALCHEMY ---")

# --- 1. CONFIGURACIÓN ---

ruta_base = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(ruta_base, 'inventario.db')

# Connection String: La dirección de la BBDD.
# Para SQLite es: sqlite:///ruta_al_archivo
# Para Oracle sería: oracle+cx_oracle://user:pass@host:port/sid
engine = create_engine(f'sqlite:///{ruta_db}', echo=False) 

Base = declarative_base()
Session = sessionmaker(bind=engine)


# --- 2. Definir la Tabla ---
class Producto(Base):
    __tablename__ = 'productos' 

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Float)
    stock = Column(Integer)

    def __repr__(self):
        return f"<Producto(nombre='{self.nombre}', precio={self.precio})>"


# --- 3. INICIALIZACIÓN ---

Base.metadata.create_all(engine)
print(f"✅ Base de datos conectada en: {ruta_db}")


# --- 4. OPERACIONES ---

def ejecutar_db():

    session = Session()

    print("\n--- A. INSERTAR DATOS ---")
    cantidad_actual = session.query(Producto).count()
    
    if cantidad_actual == 0:
        # Creamos OBJETOS Python
        prod1 = Producto(nombre="Curso Python", precio=150.00, stock=10)
        prod2 = Producto(nombre="Teclado Mecánico", precio=45.50, stock=5)
        prod3 = Producto(nombre="Ratón Gaming", precio=25.00, stock=0) 

        # Se añade a la sesión
        session.add_all([prod1, prod2, prod3])
        
        session.commit()
        print("Datos insertados correctamente.")
    else:
        print(f"La tabla ya tiene {cantidad_actual} productos. Saltando inserción.")


    print("\n--- B. CONSULTAR (SELECT) ---")
    # SQL Mental: SELECT * FROM productos WHERE precio > 40
    resultados = session.query(Producto).filter(Producto.precio > 40).all()
    
    for p in resultados:
        print(f"   -> Encontrado: {p.nombre} (ID: {p.id}) - Precio: {p.precio}€")


    print("\n--- C. ACTUALIZAR (UPDATE) ---")
    # 1. Buscr (SELECT)
    raton = session.query(Producto).filter_by(nombre="Ratón Gaming").first()
    
    if raton:
        print(f"   Precio anterior: {raton.precio}")
        # 2. Modificar el objeto
        raton.precio = 19.99
        # 3. Confirmar (Commit)
        session.commit()
        print(f"Precio actualizado a: {raton.precio}")


    session.close()

if __name__ == "__main__":
    ejecutar_db()