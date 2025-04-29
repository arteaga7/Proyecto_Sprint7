import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')
df2 = pd.DataFrame(
    {
        'x': [0, 1, 2, 3, 4, 5],
        'y': [1, 2, 4, 8, 16, 32],
        'z': [0, 1, 4, 9, 16, 25]
    }
)

st.header('Project of Sprint 7')
st.write('This application is part of an exercise.')

st.header('Slider')
number = st.slider('Select a number', 1, 100, 10)
start_button = st.button('Display number')
if start_button:
    st.write(f'You selected number {number}.')

st.header('Line plot')
st.write('The (line_chart) plot below is a line chart.')
# line_chart does not have title
st.line_chart(data=df2, x='x', y='y', x_label='Index',
              y_label='Values', color=None, width=70,
              height=400, use_container_width=True)

st.header('DataFrame')
st.write('The first rows of the DataFrame are shown below.')
st.write(df.head(20))  # Display the first 10 rows of the DataFrame

st.header('Histogram')
st.write('A histogram is shown below.')
fig_histogram = px.histogram(df, x="price", title='Price vs count')
# fig_histogram.show() #To display in a new window
# To display in the same window
st.plotly_chart(fig_histogram, use_container_width=True)

st.header('Create plot by clicking')
st.write('Click the botton below to display the plot.')
hist_button = st.button('Display')
if hist_button:  # if botton is pressed
    st.write('Histogram button was pressed')
    fig_histogram2 = px.histogram(
        df, x="model_year", title='Model year vs count')
    st.plotly_chart(fig_histogram2, use_container_width=True)

st.header('Simple botton')
st.write('Click on botton2.')
button2 = st.button('Boton2')
if button2:
    st.write(f'Botton2 was pressed')

st.header('Scatter plot')
st.write('A scatter plot is shown below.')
# Scatter and bar plots do not have x_label and y_label
fig_scatter = px.scatter(df, x='price', y='model_year',
                         title='Price vs Model year')
# To display in the same window
st.plotly_chart(fig_scatter, use_container_width=True)

st.header('Bar plot')
st.write('A bar plot is shown below.')
# Scatter and bar plots do not have x_label and y_label
fig_bar = px.bar(df2, x='x', y='y', title='X vs Y')
# To display in the same window
st.plotly_chart(fig_bar, use_container_width=True)

st.header('Checkbox')
build_histogram = st.checkbox('Histogram')
if build_histogram:
    st.write('Histogram built')
build_scatter = st.checkbox('Scatter plot')
if build_scatter:
    st.write('Scatter plot built')
