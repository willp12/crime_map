import pandas as pd
import folium
import streamlit as st
import duckdb
from streamlit.components.v1 import html
from folium.plugins import MarkerCluster

# Abrir a conexão com duck

conn = duckdb.connect('data/celulares.duckdb')

# Capturar o lat long de celulares subtraídos

df = pd.read_sql('select * from minha_tabela_v2', conn) # transforma a tabela em dataframe
df['LATITUDE'] = pd.to_numeric(df['LATITUDE'], errors='coerce') # transforma a latitude no tipo numerico
clean_df = df[df['LATITUDE'] < 0] # considera apenas latitudes menores que 0
clean_df_sp = clean_df[clean_df['NOME_MUNICIPIO'] == 'S.PAULO'] # considera apenas municipio de são paulo
cluster_data = clean_df_sp[['LATITUDE', 'LONGITUDE']].values.tolist() # transforma os valores de cluster em lista

# Gerar o objeto mapa de folium e gravar seu HTML

m = folium.Map(location=(-23.533773, -46.625290), zoom_start=12) # gera um mapa com inicio em sao paulo
MarkerCluster(cluster_data).add_to(m) # adiciona os icones de lat long
mapa_html = m._repr_html_()

# Renderizar o mapa como HTML e exibir no Streamlit

st.title("Mapa de São Paulo com Celulares Subtraídos")
st.write("Aqui está o mapa interativo com clusters:")
html(mapa_html, height=600)
