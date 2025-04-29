import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Lanzar una moneda')
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

st.write('Esta aplicación aún no es funcional. En construcción.')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
#fig = px.histogram(car_data, x="odometer") # crear un histograma
#fig.show() # crear gráfico de dispersión

st.line_chart(data=car_data, *, x=cylinders, y=days_listed, x_label=None,
              y_label=None, color=None, width=None, height=None, use_container_width=True)

print("Hola1")