import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar o conjunto de dados
car_data = pd.read_csv('vehicles.csv')  # Altere o caminho do arquivo CSV conforme necessário

# Cabeçalho
st.header('Análise do Conjunto de Dados de Veículos')

# Criar o botão para histograma
hist_button = st.button('Criar histograma')

# Verificar se o botão foi clicado
if hist_button:
    # Escrever mensagem
    st.write('Criando um histograma para o conjunto de dados de veículos')

    # Criar o histograma com Plotly Express
    fig_hist = px.histogram(car_data, x="odometer", title="Distribuição do Odomêtro dos Veículos")
    
    # Exibir o gráfico interativo
    st.plotly_chart(fig_hist, use_container_width=True)

# Criar o botão para gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

# Verificar se o botão foi clicado
if scatter_button:
    # Escrever mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de veículos')

    # Criar o gráfico de dispersão com Plotly Express
    fig_scatter = px.scatter(car_data, x="year", y="price", title="Relação entre Ano e Preço dos Veículos")
    
    # Exibir o gráfico interativo
    st.plotly_chart(fig_scatter, use_container_width=True)

