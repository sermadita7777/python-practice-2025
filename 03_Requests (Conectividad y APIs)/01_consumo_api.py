import requests
import pandas as pd
import os

def obetenerUsuarios():

    # 1. DEFINIR EL OBJETIVO
    # Lista de 10 usuarios en formato JSON
    urlApi="https://jsonplaceholder.typicode.com/users"

    print(f"Conectando a {urlApi}...")

    try:
        # 2. HACER LA PETICIÓN
        response=requests.get(urlApi,timeout=10)

        # 3. VERIFICAR LA CONEXIÓN
        if response.status_code == 200:
            print("Conexión exitosa (Status 200)")

            # 4. PARSEAR LA RESPUESTA
            # .json() convierte el string que llega a una lista de diccionarios
            datosJson=response.json()

            print(f"Se han descargado {len(datosJson)} registros")

            # --- Integración con Pandas ---
            df=pd.DataFrame(datosJson)

            # Limpieza rápida de diccionarios anidados
            df['ciudad_real'] = df['address'].apply(lambda x: x.get('city'))

            # Seleccionar columnas útiles
            dfFinal=df[['id', 'name', 'email', 'phone', 'ciudad_real', 'website']]

            print("\n--- VISTA PREVIA DE DATOS IMPORTADOS ---")
            print(dfFinal.head(3))

            # 5. GUARDAR EN LOCAL
            ruta_base = os.path.dirname(os.path.abspath(__file__))
            ruta_csv = os.path.join(ruta_base, 'usuarios_importados.csv')

            dfFinal.to_csv(ruta_csv,index=False)
            print(f"\nDatos guardados en: {ruta_csv}")

        else:
            print(f"Error en la petición. Código: {response.status_code}")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error Crítico: No tienes internet o el servidor no existe.")
    except Exception as e:
        print(f"❌ Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    obetenerUsuarios()