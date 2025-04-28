import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Lanzar una moneda')

st.write('Esta aplicación aún no es funcional. En construcción.')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
fig = px.histogram(car_data, x="odometer") # crear un histograma
fig.show() # crear gráfico de dispersión



print("Hola1")