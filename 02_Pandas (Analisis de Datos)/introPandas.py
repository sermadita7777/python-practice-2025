import pandas as pd
import os

def iniciar_analisis():

    # PASO 1: CONFIGURACIÓN DE RUTAS -> evitar fallos con rutas relativas
    
    directorio_actual=os.path.dirname(os.path.abspath(__file__))

    ruta_csv=os.path.join(directorio_actual,'inventario.csv')

    print(f"Trabajando en el directorio: {directorio_actual}")
    print(f"Archivo objetivo: {ruta_csv}")

    # PASO 2: CARGAR DATOS

    datos={
        'id': [1, 2, 3],
        'producto': ['Teclado', 'Ratón', 'Monitor'],
        'precio': [20.5, 10.0, 150.99]
    }

    df_inicial=pd.DataFrame(datos)

    # Se guardan en la ruta indicada
    df_inicial.to_csv(ruta_csv,index=False)
    print("Archivo CSV generado")

    # PASO 3: LEER DATOS
    print("Cargando el archivo...")

    if os.path.exists(ruta_csv):
        df=pd.read_csv(ruta_csv)

        print("\n--- RESULTADO ---")
        print(df.head())
        print("\n--- INFORMACIÓN ---")
        print(df.info())
    else:
        print("Error: El archivo no se ha encontrado")

if __name__ == "__main__":
    iniciar_analisis()