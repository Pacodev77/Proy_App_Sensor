# Crear la ventana principal
root = Tk()
root.title("Aplicación de Graficación de Datos")
root.geometry("400x200")

# Añadir un botón para cargar el archivo
btn_cargar = Button(root, text="Cargar Archivo JSON", command=cargar_archivo)
btn_cargar.pack(pady=20)

# Etiqueta para mostrar instrucciones
label_instrucciones = Label(root, text="Seleccione un archivo JSON para graficar los datos.")
label_instrucciones.pack()

# Iniciar el bucle de eventos
root.mainloop()