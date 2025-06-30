# proyecto_sprint7
Repositorio de el proyecto del sprint 7, donde se explora un dataset con ventas de diferentes modelos de autos

# Aplicación web de anuncios de vehículos

Esta aplicación fue desarrollada como parte del Sprint 7 del bootcamp de ciencia de datos en TripleTen. Utiliza Streamlit para desplegar un dashboard interactivo que permite visualizar un conjunto de datos sobre anuncios de venta de vehículos en EE.UU.

## Funcionalidad

- Mostrar una vista previa del dataset.
- Construir un histograma de la columna `odometer`.
- Construir un gráfico de dispersión para analizar la relación entre el precio y el año del modelo del vehículo, agrupado por condición.

## Extras
 
### 📦 Gráfico de barras apiladas: Tipos de vehículo por fabricante
Visualiza cuántos vehículos tiene cada fabricante, divididos por tipo de vehículo (SUV, sedan, pickup, etc.).  
Útil para comparar el enfoque de cada marca respecto a su catálogo de productos.

### 📅 Histograma agrupado: Condición de vehículos por año del modelo
Muestra la cantidad de vehículos por año y su condición.  
Permite observar tendencias como que los vehículos más nuevos tienen mejor condición (e.g. "excellent", "like new") y los más antiguos suelen estar en peores condiciones.

## Requisitos

- Python 3.9+
- streamlit
- pandas
- plotly

## Cómo ejecutar

```bash
streamlit run app.py
