import os
import shutil

def limpiar_archivos_temporales_mac():
    # Carpetas comunes de archivos temporales en macOS
    rutas_a_limpiar = [
        "/tmp",  # Carpeta temporal del sistema
        os.path.expanduser("~/Library/Caches")  # Carpeta de cachés del usuario
    ]

    # Eliminar archivos en las rutas especificadas
    for ruta in rutas_a_limpiar:
        if os.path.exists(ruta):
            print(f"Limpiando: {ruta}")
            for archivo in os.listdir(ruta):
                archivo_completo = os.path.join(ruta, archivo)
                try:
                    if os.path.isfile(archivo_completo) or os.path.islink(archivo_completo):
                        os.unlink(archivo_completo)  # Eliminar archivos
                    elif os.path.isdir(archivo_completo):
                        shutil.rmtree(archivo_completo)  # Eliminar directorios
                except Exception as e:
                    print(f"No se pudo eliminar {archivo_completo}: {e}")
        else:
            print(f"La ruta no existe: {ruta}")

    print("Limpieza completada.")

if __name__ == "__main__":
    limpiar_archivos_temporales_mac()
