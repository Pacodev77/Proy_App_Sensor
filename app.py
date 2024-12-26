#Creación de App proyecto pacodev77 (Tutor: Jhonatan Rivero)

#Parte I (Pruebas)
import json

# Ruta del archivo JSON
ruta_archivo = "index.json"

# Cargar el archivo JSON
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

# Mostrar los datos cargados
print("Datos cargados:")
print(json.dumps(datos, indent=4, ensure_ascii=False))
