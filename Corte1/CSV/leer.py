import csv

nombre_archivo = "personas.csv"

# Leer y mostrar el contenido del archivo CSV
with open(nombre_archivo, mode="r", encoding="utf-8") as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    
    # Iterar sobre cada fila e imprimirla
    for linea in lector_csv:
        print(linea)
