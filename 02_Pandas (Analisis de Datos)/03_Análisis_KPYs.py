import pandas as pd
import os

def analizar_kpis():

    # GENERAR DATOS 

    datos = {
        'Fecha': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03'],
        'Vendedor': ['Ana', 'Carlos', 'Ana', 'Carlos', 'Beatriz', 'Ana'],
        'Region': ['Norte', 'Sur', 'Norte', 'Sur', 'Este', 'Norte'],
        'Categoria': ['Software', 'Hardware', 'Software', 'Formacion', 'Software', 'Hardware'],
        'Ventas': [1000, 1500, 1200, 800, 2000, 500]
    }

    df=pd.DataFrame(datos)

    print("DATOS BRUTOS: ")
    print(df)
    print("-"*40)

    # ANÁLISIS 1: RANKING DE VENDEDORES (suma simple)
    
    print("\n1. Ranking de Vendedores:")

    # A. Agrupar por vendedor y sumar ventas
    ranking=df.groupby('Vendedor')['Ventas'].sum()

    # B. reset_index() -> permite pasar del índice a columna plana
    ranking=ranking.reset_index()

    # C. Ordenar de mayor a menor
    ranking=ranking.sort_values(by='Ventas',ascending=False)

    print(ranking)

    # ANÁLISIS 2: INFORME REGIONAL (agrupación múltiple)
    informe_region = df.groupby('Region')['Ventas'].agg(['sum', 'mean', 'count'])

    informe_region = informe_region.rename(columns={
        'sum': 'Facturacion_Total',
        'mean': 'Ticket_Medio',
        'count': 'Num_Operaciones'
    }).reset_index()

    print(informe_region)

    # EXPORTACIÓN RESULTADOS
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_reporte = os.path.join(ruta_base, 'reporte_ejecutivo.csv')

    informe_region.to_csv(ruta_reporte, index=False)
    print(f"\n Reporte guardado en: {ruta_reporte}")

if __name__=="__main__":
    analizar_kpis()
