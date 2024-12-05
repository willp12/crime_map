import pandas as pd
import folium
import streamlit as st
import duckdb
from streamlit.components.v1 import html
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

#data_path = 'data/CelularesSubtraidos_2024.xlsx'

conn = duckdb.connect('data/celulares.duckdb')

df = pd.read_sql('select * from minha_tabela_v2', conn)
df['LATITUDE'] = pd.to_numeric(df['LATITUDE'], errors='coerce')
clean_df = df[df['LATITUDE'] < 0]
clean_df_sp = clean_df[clean_df['NOME_MUNICIPIO'] == 'S.PAULO']
cluster_data = clean_df_sp[['LATITUDE', 'LONGITUDE']].values.tolist()

m = folium.Map(location=(-23.533773, -46.625290), zoom_start=12)
MarkerCluster(cluster_data).add_to(m)
mapa_html = m._repr_html_()

# Renderizar o mapa como HTML e exibir no Streamlit
st.title("Mapa com Folium no Streamlit")
st.write("Aqui está o mapa interativo com clusters:")
html(mapa_html, height=600)



# Renderizar HTML do mapa
#st_map = st_folium(m, width=700, height=450)
