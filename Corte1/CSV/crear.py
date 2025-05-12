import csv

# Definir los datos a escribir
encabezados = ["Nombre", "Edad", "Ciudad"]
registros = [
    ["Ana", 25, "Lima"],
    ["Luis", 30, "Bogotá"],
    ["María", 28, "Ciudad de México"]
]

# Nombre del archivo CSV
nombre_archivo = "personas.csv"

# Escribir los datos en el archivo
with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(encabezados)  # Escribir encabezados
    escritor_csv.writerows(registros)   # Escribir filas de datos

print(f"Archivo '{nombre_archivo}' creado y datos guardados con éxito.")
