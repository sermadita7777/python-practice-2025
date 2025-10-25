import pandas as pd

# Leer CSV
df = pd.read_csv("datasets/ventas.csv")

# Primeras filas e info
print("Primeras filas:")
print(df.head(), "\n")
print("Información general:")
print(df.info(), "\n")

# Valor total por producto
df["total_venta"] = df["precio"] * df["cantidad"]
print("Valor total por producto:")
print(df[["producto", "total_venta"]], "\n")

# Promedio de precio por categoría
print("Promedio de precio por categoría:")
print(df.groupby("categoria")["precio"].mean(), "\n")

# Producto más caro
producto_mas_caro = df.loc[df["precio"].idxmax(), "producto"]
print("Producto más caro:", producto_mas_caro, "\n")

# Categoría con más productos vendidos
categoria_mas_vendida = df.groupby("categoria")["cantidad"].sum().idxmax()
print("Categoría con más productos vendidos:", categoria_mas_vendida, "\n")

# Correlación precio-cantidad
print("Correlación precio-cantidad:")
print(df[["precio","cantidad"]].corr(), "\n")

# Ordenar por valor total de venta
df_ordenado = df.sort_values("total_venta", ascending=False)
print("Productos ordenados por total de venta:")
print(df_ordenado[["producto","total_venta"]])
