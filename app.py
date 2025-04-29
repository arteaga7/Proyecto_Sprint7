import pandas as pd
import plotly.express as px
import streamlit as st

#df = pd.read_csv('vehicles_us.csv')
df = pd.DataFrame(
    {
        'x': [0,1,2,3,4,5],
        'y': [1,2,4,8,16,32],
        'z': [0,1,4,9,16,25]
    }
)

st.header('Slider')
number_of_trials = st.slider('Number of tries?', 1, 100, 10)
start_button = st.button('Run test')
if start_button:
    st.write(f'Test with {number_of_trials} tries.')

st.write('Simple text as paragraph.')

st.header('Line plot (line_chart)')
st.line_chart(data=df, x='x', y='y', x_label='x_label',
              y_label='y_label', color=None, width=70,
              height=400, use_container_width=True)

st.header('DataFrame')
st.write(df)

st.write('Simple text as paragraph.')

st.header('Histogram')
fig_histogram = px.histogram(df, x="y")
#fig_histogram.show() #To display in a new window
st.plotly_chart(fig_histogram, use_container_width=True)  #To display in the same window

st.header('Create plot by clicking')
hist_button = st.button('Create histogram')
if hist_button: #if botton is pressed
            st.write('Histogram button was pressed')
            fig2 = px.histogram(df, x="z", width=50, height=200)
            st.plotly_chart(fig2, use_container_width=True)

st.header('Simple botton')
st.write('Lets create a simple botton.')
button2 = st.button('Boton2')
if button2:
    st.write(f'Botton2 was pressed')

st.header('Scatter plot') 
fig_scatter = px.scatter(df, x='x',y='y')
st.plotly_chart(fig_scatter, use_container_width=True)  #To display in the same window

st.header('Bar plot') 
fig_bar = px.bar(df, x='x',y='y')
st.plotly_chart(fig_bar, use_container_width=True)  #To display in the same window

st.header('Checkbox') 
build_histogram = st.checkbox('Histogram')
if build_histogram:
    st.write('Histogram built')
build_scatter = st.checkbox('Scatter plot')
if build_scatter:
    st.write('Scatter plot built')