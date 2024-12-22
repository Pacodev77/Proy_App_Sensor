#Creación de App proyecto pacodev77 (Tutor: Jhonatan Rivero)

#Parte I (Pruebas)

''' 
#Importar archivo JSON
import json

def cargar_datos_json(archivo):
    with open(archivo, 'r') as f:
        datos = json.load(f)
    return datos

# Ejemplo de uso
if __name__ == "__main__":
    archivo_json = "index.json"  # Archivo json (dentro de la carpeta: Proy_App_Sensor)
    datos = cargar_datos_json(archivo_json)
    print(datos)  # Esto imprimirá los datos en la consola
    '''

#Cargar librerias
import json
import pandas as pd


#Parte I (Pruebas)

#Función que recibe los datos y los retorna (archivo JSON)
def cargar_datos_json(archivo):
    with open(archivo, 'r') as f:
        datos = json.load(f)
    return datos


#función que procesa los datos (archivo JSON)
def procesar_datos(datos):
    df = pd.DataFrame(datos)
    df['tiempo'] = pd.to_datetime(df['tiempo'])
    return df

#Parte II

#Condicional que recibe al archivo JSON
if __name__ == "__main__":
    archivo_json = "index.json"
    datos = cargar_datos_json(archivo_json)
    df = procesar_datos(datos)
    print(df)  # La consola imprimirá un DataFrame de Pandas

    import matplotlib.pyplot as plt


#Parte III

#Función que grafica los datos del archivo (JSON)
def graficar_datos(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['tiempo'], df['velocidad'], marker='o', label='Velocidad (km/h)')
    plt.title('Velocidad Estimada en el tiempo')
    plt.xlabel('Tiempo')
    plt.ylabel('Velocidad (km/h)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    archivo_json = "index.json"
    datos = cargar_datos_json(archivo_json)
    df = procesar_datos(datos)
    graficar_datos(df)

