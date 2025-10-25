import pandas as pd

# Leer CSV
df = pd.read_csv("datasets/empleados.csv")

# 1️⃣ Primeras filas
print("🔹 Primeras filas:")
print(df.head(), "\n")

# 2️⃣ Información general
print("🔹 Información general:")
print(df.info(), "\n")

# 3️⃣ Estadísticas básicas
print("🔹 Estadísticas descriptivas:")
print(df.describe(), "\n")

# 4️⃣ Agrupaciones
print("🔹 Promedio de ingresos por ciudad:")
print(df.groupby("ciudad")["ingresos"].mean(), "\n")

# 5️⃣ Conteo de empleados por ciudad
print("🔹 Conteo de empleados por ciudad:")
print(df["ciudad"].value_counts(), "\n")

# 6️⃣ Correlación entre edad e ingresos
print("🔹 Correlación entre edad e ingresos:")
print(df[["edad","ingresos"]].corr())
