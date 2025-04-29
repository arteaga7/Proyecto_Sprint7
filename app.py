import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Slider')
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

st.write('Esta aplicación aún no es funcional. En construcción.')

st.header('Grafica de linea (line_chart)')

df = pd.DataFrame(
    {
        'x': [0,1,2,3,4,5],
        'y': [1,2,4,8,16,32],
        'z': [0,1,4,9,16,25]
    }
)

st.line_chart(data=df, x='x', y='y', x_label='None',
              y_label='None', color=None, width=70,
              height=400, use_container_width=True)

st.header('Imprimir DataFrame')
st.write(df)
st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
st.header('Histogram')
#df = pd.read_csv('vehicles_us.csv') # leer los datos
fig = px.histogram(df, x="y") # crear un histograma
#fig.show() #To display in a new window

st.plotly_chart(fig, use_container_width=True)  #To display in the same window

st.header('Crea plot al dar clic')
hist_button = st.button('Construir histograma')
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Cches')
            
            # crear un histograma
            fig2 = px.histogram(df, x="x", width=50, height=200)
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig2, use_container_width=True)


button2 = st.button('Boton2')

if button2:
    st.write(f'Presionaste boton2')
    
fig_scatter = px.scatter(df, x='x',y='y') # crear un histograma
#fig.show() #To display in a new window

st.plotly_chart(fig_scatter, use_container_width=True)  #To display in the same window

fig_bar = px.bar(df, x='x',y='y') # crear un histograma
#fig.show() #To display in a new window

st.plotly_chart(fig_bar, use_container_width=True)  #To display in the same window