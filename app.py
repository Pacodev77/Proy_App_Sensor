import json
import pandas as pd
from tkinter import Button, Tk, Label, filedialog, Checkbutton, BooleanVar, Frame
import matplotlib.pyplot as plt

# Variables y Constantes
ancho_v = 600
alto_v = 300
Type_File = [("Archivos JSON", "*.json")]

# Cargar el archivo JSON
def cargar_archivo(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise ValueError(f"Archivo '{archivo}' No encontrado")
    except json.JSONDecodeError:
        raise ValueError(f"El archivo '{archivo}' esta dañado")
    except Exception as error:
        raise ValueError(f"Error inesperado '{archivo}': {error}")

# Función para seleccionar archivos
def select_file():
    archivo = filedialog.askopenfile(filetypes=Type_File)
    if archivo:
        return archivo
    else:
        raise ValueError("No se seleccionó un archivo")

# Funcion para procesar el archivo
def process_file():
    try:
        archivo = select_file()
        datos = cargar_archivo(archivo.name)
        label_message['text'] = "Archivo cargado correctamente"
        crear_opciones_graficar(datos)
    except ValueError as error:
        label_message['text'] = str(error)

def crear_opciones_graficar(datos):
    global opciones_graficar
    opciones_graficar = []
    sensores = datos['sensores']
    frame = Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor='center')
    
    for i, sensor in enumerate(sensores):
        tipo = sensor['tipo']
        opciones_graficar.append(BooleanVar())
        checkbutton = Checkbutton(frame, text=tipo, variable=opciones_graficar[-1])
        checkbutton.pack()

    boton_graficar = Button(frame, text="Graficar", command=lambda: graficar_datos(datos))
    boton_graficar.pack()

def graficar_datos(datos):
    try:
        sensores = datos['sensores']
        
        for i, sensor in enumerate(sensores):
            tipo = sensor['tipo']
            valores = sensor['valores']
            
            if opciones_graficar[i].get():
                if tipo == 'coordenadas':
                    df = pd.DataFrame(valores)
                    df.plot(x='lat', y='lon', kind='scatter')
                    plt.title(tipo)
                    plt.xlabel('Latitud')
                    plt.ylabel('Longitud')
                    plt.show()
                else:
                    df = pd.DataFrame(valores, columns=['Valor'])
                    df.plot(kind='line')
                    plt.title(tipo)
                    plt.xlabel('Tiempo')
                    plt.ylabel('Valor')
                    plt.show()
    except Exception as error:
        label_message['text'] = f"Error al graficar los datos: {error}"

# Crear ventana
root = Tk()
root.title("Gestor Gráfico Lot")

frame = Frame(root)
frame.pack(padx=10, pady=10)

ancho_p = root.winfo_screenwidth()
alto_p = root.winfo_screenheight()
x = (ancho_p -ancho_v) // 2
y = (alto_p - alto_v) // 2
root.geometry(f"{ancho_v}x{alto_v}+{x}+{y}") 

boton_cargar = Button(frame, text="Seleccione un Archivo", command=process_file)
boton_cargar.pack(pady=10)

label_message = Label(frame, text="")
label_message.pack()

root.mainloop()