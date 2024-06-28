import pandas as pd
import streamlit as st
import plotly_express as px

# leemos nuestro csv
car_data = pd.read_csv(r"C:\Users\Christian\sprint5\vehicles_us.csv")

st.header('Comparativa de anuncios de ventas de coches')

hist_chbox = st.checkbox('Construir histograma')  # crear un botón

if hist_chbox:  # al seleccionar la casilla
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scat_chbox = st.checkbox(
    'Construir un diagrama de dispersión')  # Creamos otro checkbox

if scat_chbox:  # al seleccionar la casilla
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de ventas de coches')

    # crear un diagrama de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
