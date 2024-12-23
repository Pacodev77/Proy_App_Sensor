


import json
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import plotly.graph_objs as go
import os
import base64  # Asegúrate de incluir esta línea

# Clase para manejar la carga y validación del archivo JSON
class CargadorJSON:
    @staticmethod
    def cargar_datos_json(archivo):
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return None, "El archivo no se encontró."
        except json.JSONDecodeError:
            return None, "El archivo no se pudo decodificar como JSON."

# Clase para el procesamiento de datos
class ProcesadorDatos:
    @staticmethod
    def procesar_datos(datos):
        df = pd.DataFrame(datos)
        df['tiempo'] = pd.to_datetime(df['tiempo'])
        
        if 'tiempo' not in df.columns or 'velocidad' not in df.columns:
            return None, "El archivo JSON no contiene las columnas necesarias."
        
        return df, None

# Crear la aplicación Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Aplicación de Graficación de Datos"),
    dcc.Upload(
        id='upload-data',
        children=html.Button('Cargar Archivo JSON'),
        multiple=False
    ),
    dcc.Graph(id='grafico-datos'),
    html.Div(id='mensaje')
])

@callback(
    Output('grafico-datos', 'figure'),
    Output('mensaje', 'children'),
    Input('upload-data', 'contents'),
)
def actualizar_grafico(contents):
    if contents is None:
        return {}, "Por favor, cargue un archivo JSON."

    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    with open('temp.json', 'wb') as f:
        f.write(decoded)

    datos, error = CargadorJSON.cargar_datos_json('temp.json')
    if error:
        return {}, error

    df, error = ProcesadorDatos.procesar_datos(datos)
    if error:
        return {}, error

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['tiempo'], y=df['velocidad'], mode='lines+markers', name='Velocidad'))
    fig.update_layout(title='Velocidad Estimada en el Tiempo',
                      xaxis_title='Tiempo',
                      yaxis_title='Velocidad (km/h)',
                      xaxis_tickformat='%Y-%m-%d %H:%M:%S')

    return fig, ""

if __name__ == '__main__':
    app.run_server(debug=True)





