import json
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import Tk, Button, filedialog, Checkbutton, BooleanVar, Frame

# Variables
type_file = [('Archivo JSON', '*.json')]
ancho_v = 600
alto_v = 300

# Funciones 
def cargar_archivo(archivo):
    try:
        with open(archivo, 'r') as file:
            datos = json.load(file)
        return datos
    except FileNotFoundError:
        print(f'Archivo no Encontrado "{archivo}"')
    except json.JSONDecodeError:
        print(f'Error del archivo "{archivo}"')
    except Exception as error:
        print(f'Error Inesperado "{archivo}": {error}')
    return None

def select_file():
    archivo = filedialog.askopenfile(filetypes=type_file)
    if archivo:
       return archivo
    else:
      label_message['text'] = "El archivo no se h seleccionado"
      return None

def process_file():
    archivo = select_file()
    if archivo:
        datos = cargar_archivo(archivo.name)
        if datos:
            label_message['text'] = "Arhcivo cargado Correctamente"
            crear_opciones_graficas(datos)

def crear_opciones_graficas(datos):
    global opciones_graficar
    opciones_graficar = []
    sensores = datos['sensores']




         
   
