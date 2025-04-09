import pandas as pd
import plotly.express as px
import streamlit as st
st.header('Anúncios de vendas de Carros')

car_data = pd.read_csv('vehicles.csv') # lendo os dados
fig = px.histogram(car_data, x="odometer") # criar um histograma
fig.show() # exibindo

# Garantindo que as colunas 'odometer' e 'price' sejam numéricas
car_data['odometer'] = pd.to_numeric(car_data['odometer'], errors='coerce')
car_data['price'] = pd.to_numeric(car_data['price'], errors='coerce')

# Criando o gráfico de dispersão
fig = px.scatter(car_data, x="odometer", y="price", title="Preço vs. Quilometragem do Carro", 
                 labels={'odometer': 'Quilometragem (milhas)', 'price': 'Preço (USD)'})

# Exibindo o gráfico
fig.show()


hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
            # escrever uma mensagem
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
            fig = px.histogram(car_data, x="odometer")
        
            # exibir um gráfico Plotly interativo
            st.plotly_chart(fig, use_container_width=True)


# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada
  st.write('Criando um histograma para a coluna odometer')
