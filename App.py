import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles.csv') # lendo os dados
st.header('Anúncios de vendas de Carros')

# Garantindo que as colunas 'odometer' e 'price' sejam numéricas
car_data['odometer'] = pd.to_numeric(car_data['odometer'], errors='coerce')
car_data['price'] = pd.to_numeric(car_data['price'], errors='coerce')

# Criando o gráfico de dispersão
fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Preço vs. Quilometragem do Carro", 
                         labels={'odometer': 'Quilometragem (milhas)', 'price': 'Preço (USD)'})

# Criando o histograma de preços
fig_histogram = px.histogram(car_data, x="price", nbins=30, title="Distribuição de Preços dos Carros", 
                              labels={'price': 'Preço (USD)'})

# Exibindo os gráficos
fig_scatter.show()
fig_histogram.show()
