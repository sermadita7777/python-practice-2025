import pandas as pd
import numpy as np
import os

def limpiar_datos():
    
    # 1. CONFIGURACIÓN DE RUTAS

    rutaBase=os.path.dirname(os.path.abspath(__file__))
    rutaSucia=os.path.join(rutaBase,'ventas_sucias.csv')
    rutaLimpia=os.path.join(rutaBase,'ventas_limpias.csv')

    # 2. GENERAR DATOS SUCIOS (MOCK)

    datos = {
        'fecha': ['2024-01-01', '02/01/2024', None, '2024-01-05', '2024-01-05'],
        'cliente': ['Imprex', '  IMPREX  ', 'Logista', 'Amazon', 'Amazon'], # Duplicado y espacios
        'importe': ['1000', '250.50', None, 'ERROR', '1500'], # Mezcla texto y números
        'estado': ['Confirmado', 'Confirmado', 'Pendiente', 'Cancelado', 'Cancelado']
    }

    df=pd.DataFrame(datos)

    df.to_csv(rutaSucia, index=False)
    print("Archivo sucio generado. Procediendo a limpieza...")

    print("--- 1. ESTADO INICIAL ---")
    print(df)
    print("\n")

    # 3. PROCESO DE LIMPIEZA

    # A. Quitar duplicados
    df=df.drop_duplicates()
    print(f"Duplicados eliminados. Filas restantes: {len(df)}")

    # B. Limpieza de texto
    df['cliente'] = df['cliente'].fillna('DESCONOCIDO').str.strip().str.upper()
    print("Nombres de clientes normalizados (IMPREX)")

    # C. Limpieza numérica 
    df['importe_num'] = pd.to_numeric(df['importe'], errors='coerce')

    # Rellenar nulos con 0.0
    df['importe_num'] = df['importe_num'].fillna(0.0)
    print("Importes convertidos a números reales")

    # D. Limpieza de fechas
    df['fecha_corr'] = pd.to_datetime(df['fecha'], errors='coerce')
    df['fecha_corr'] = df['fecha_corr'].fillna(pd.Timestamp.today())
    print("Fechas estandarizadas")

    # 4. SELECCIÓN FINAL 
    dfFinal = df[['fecha_corr', 'cliente', 'importe_num', 'estado']]

    print("\n--- RESULTADO FINAL ---")
    print(dfFinal)
    print(dfFinal.info())

    # 5. GUARDAR
    dfFinal.to_csv(rutaLimpia,index=False)
    print(f"Datos limpios guardados en: {rutaLimpia}")

if __name__ == "__main__":
    limpiar_datos()