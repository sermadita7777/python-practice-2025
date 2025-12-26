import os
from dotenv import load_dotenv

load_dotenv()

def iniciarSistema():
    print("Iniciando el sistema... ")

    usuario=os.getenv("DB_USER")
    clave=os.getenv("DB_PASSWORD")
    entorno=os.getenv("ENTORNO")

    if not usuario or not clave:
        print("ERROR: No se han encontrado las credenciales en el .env")
        return
    
    print(f"Cargando conrfiguración para el entorno: {entorno}")
    print(f"Usuario: {usuario}")
    print(f"Clave cargada correctamente")

    if entorno == "DESARROLLO":
        print("Modo debug activado")
    
if __name__ == "__main__":
    iniciarSistema()