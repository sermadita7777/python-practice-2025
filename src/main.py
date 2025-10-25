import os

def analizar_archivo(nombre):
    if not os.path.exists(nombre):
        print("El archivo no existe.")
        return
    with open(nombre, 'r', encoding='utf-8') as f: #abrir el archivo en modo lectura, el with cierra el archivo automaticamente
        lineas = f.readlines()
    total_lineas = len(lineas)
    total_palabras = sum(len(l.split()) for l in lineas) #sumar la cantidad de palabras en cada linea separadas por espacios 
    print(f" {nombre}")
    print(f"→ Líneas: {total_lineas}")
    print(f"→ Palabras: {total_palabras}")

archivo = input("Nombre del archivo a analizar: ")
analizar_archivo(archivo)
