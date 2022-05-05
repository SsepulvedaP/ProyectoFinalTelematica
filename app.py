#Se llaman las librerias
from dash import Dash, html, dcc #Esta es la libreria para el servidor web del data science
import pandas as pd              #Esta libreria es para procesar los datos

#Declarar objetos principales
app = Dash(__name__)
#Cargar la base de datos
df = pd.read_excel('datanoticias.xlsx')
#Configuracion del sitio web
app.layout = html.Div([html.H1('Bienvenido a la seccion de noticias Barquituma'),
                       html.Div('Noticia 1:')
                       html.Div('Noticia 2:')])
#funcion principal
if __name__ == '__main__':
  #Cargar el objeto principal a todas las interfaces de red en el puerto 80
  app.run_server(host='0.0.0.0',port=80)
