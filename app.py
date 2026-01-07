import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

# Separar la columna 'model' en 'marca' y 'modelo'
car_data_marca = car_data.copy()
car_data_marca[['marca', 'modelo']] = (
    car_data_marca['model']
    .str.strip()
    .str.split(' ', n=1, expand=True)
)

# Título y descripción de la app
st.header('Analisis de Precios de venta de vehículos usados en USA')
st.write('Desarrollado por José Manuel Sánchez')

# Botones para generar gráficos
start_button11 = st.button('Distribución precios Bines estrechos')
start_button12 = st.button('Distribución precios Bines amplios')
start_button21 = st.button('Precios por año')
start_button22 = st.button('Precios por año Toyota')
start_button23 = st.button('Precios por año Chevrolet')

if start_button11:
    # Crear un histograma para ver la distribción de precios de los vehículos
    fig1 = go.Figure(data=[go.Histogram(x=car_data['price'])])
    # añadir un título al gráfico si lo deseas
    fig1.update_layout(title_text='Distribución de precios de vehículos')
    fig1.update_layout(xaxis=dict(range=[0, 50000]))
    fig1.update_traces(nbinsx=500)
    # Mostrar el gráfico Plotly
    st.plotly_chart(fig1, use_container_width=True)

if start_button12:
    # Crear un histograma para ver la distribción de precios de los vehículos
    fig2 = go.Figure(data=[go.Histogram(x=car_data['price'])])
    # añadir un título al gráfico si lo deseas
    fig2.update_layout(title_text='Distribución de precios de vehículos')
    fig2.update_layout(xaxis=dict(range=[0, 50000]))
    fig2.update_traces(nbinsx=250)
    # Mostrar el gráfico Plotly
    st.plotly_chart(fig2, use_container_width=True)

if start_button21:
    # Crear un scatter plot del precio contra el año todas las marcas
    fig3 = go.Figure(data=[go.Scatter(
        x=car_data['model_year'], y=car_data['price'], mode='markers')])

    # Añadir un título al gráfico
    fig3.update_layout(title_text='Relación entre Año y Precio')

    # Mostrar el gráfico Plotly
    st.plotly_chart(fig3, use_container_width=True)

if start_button22:
    # Crear un scatter plot del precio contra el año - solo Toyota
    car_data_marca_toyota = car_data_marca[car_data_marca['marca'] == 'toyota']
    fig4 = go.Figure(data=[go.Scatter(
        x=car_data_marca_toyota['model_year'], y=car_data_marca_toyota['price'], mode='markers')])

    # Añadir un título al gráfico
    fig4.update_layout(title_text='Relación entre Año y Precio de Toyota')

    # fijar ejes para mejor comparación
    fig4.update_layout(xaxis=dict(range=[1908, 2019]))
    fig4.update_layout(yaxis=dict(range=[0, 400000]))
    # Mostrar el gráfico Plotly
    st.plotly_chart(fig4, use_container_width=True)

if start_button23:
    # Crear un scatter plot del precio contra el año - solo Chevrolet
    car_data_marca_chevrolet = car_data_marca[car_data_marca['marca'] == 'chevrolet']
    fig5 = go.Figure(data=[go.Scatter(
        x=car_data_marca_chevrolet['model_year'], y=car_data_marca_chevrolet['price'], mode='markers')])

    # Añadir un título al gráfico
    fig5.update_layout(title_text='Relación entre Año y Precio de Chevrolet')

    # fijar ejes para mejor comparación
    fig5.update_layout(xaxis=dict(range=[1908, 2019]))
    fig5.update_layout(yaxis=dict(range=[0, 400000]))
    # Mostrar el gráfico Plotly
    st.plotly_chart(fig5, use_container_width=True)
