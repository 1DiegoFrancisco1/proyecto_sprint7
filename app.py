import pandas as pd
import plotly.express as px
import streamlit as st

st.header('📊 Anuncios de venta de vehículos en EE.UU.')

car_data = pd.read_csv('./notebooks/vehicles_us.csv')  # leer los datos

if st.checkbox('Mostrar vista previa del dataset'):
    st.write(car_data.head(10))

# Checkbox para construir histograma de kilometraje
if st.checkbox('Construir un histograma'):
    st.write('🔍 Histograma para la columna odómetro (odometer)')
    fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar el histograma creado con Plotly dentro de la aplicación Streamlit,
    # adaptando el gráfico al ancho del contenedor
    st.plotly_chart(fig_hist, use_container_width=True)

    # Explicación del gráfico
    st.write("""
    Este gráfico muestra cómo se distribuyen los kilometrajes de los coches en venta.
    El eje X representa el kilometraje, y el eje Y la cantidad de vehículos que caen en cada rango.
    """)

# Checkbox para construir gráfico de dispersión
if st.checkbox('Construir un gráfico de dispersión'):
    st.write('🔍 Diagrama de dispersión: precio vs. año del modelo')
    fig_scatter = px.scatter(car_data, x="model_year",
                             y="price", color="condition")
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Explicación del gráfico
    st.write("""
    Este gráfico compara el precio de los vehículos según su año de fabricación.
    Cada punto es un vehículo. El eje X muestra el año del modelo, el eje Y el precio, 
    y el color representa la condición del vehículo (por ejemplo, 'excellent', 'good', etc.).
    """)

# Crear una columna 'manufacturer' extrayendo la primera palabra del modelo
car_data['manufacturer'] = car_data['model'].str.split().str[0].str.lower()

if st.checkbox('Gráfico: Tipos de vehículo por fabricante'):
    st.write("🚗 Tipos de vehículos por fabricante")

    # Crear un gráfico de barras apiladas
    fig_bar = px.histogram(
        car_data,
        x="manufacturer",
        color="type",
        barmode="stack",
        title="Distribución de tipos de vehículos por fabricante"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

    st.write("""
    Este gráfico de barras apiladas muestra cuántos vehículos vende cada fabricante, separados por tipo.
    Permite analizar qué tipo de vehículos predominan según el fabricante (por ejemplo, pickups en Ford).
    """)

if st.checkbox('Gráfico: Condición de vehículos por año del modelo'):
    st.write("📅 Condición de los vehículos según el año del modelo")

    # Histograma apilado por condición
    fig_condition = px.histogram(
        car_data,
        x="model_year",
        color="condition",
        barmode="stack",  # <-- CAMBIO IMPORTANTE AQUÍ
        title="Condición de vehículos según el año del modelo"
    )

    st.plotly_chart(fig_condition, use_container_width=True)

    st.write("""
    Este gráfico muestra cuántos vehículos de cada año están en ciertas condiciones (excellent, good, fair...).
    Al estar apiladas, las barras permiten comparar rápidamente la cantidad total de autos por año y cómo se distribuyen por condición.
    """)
