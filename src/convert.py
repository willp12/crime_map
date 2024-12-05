import pandas as pd
import duckdb

conn = duckdb.connect('data/celulares.duckdb')
cursor = conn.cursor()
excel_path = 'data/CelularesSubtraidos_2024.xlsx'

#excel = pd.read_excel('data/CelularesSubtraidos_2024.xlsx', sheet_name='CELULAR_2024')
conn.execute("INSTALL spatial;")
conn.execute("LOAD spatial;")

conn.execute(f"""
CREATE TABLE minha_tabela_v2 AS
SELECT * FROM st_read('{excel_path}', layer='CELULAR_2024', open_options = ['HEADERS=FORCE', 'FIELD_TYPES=AUTO']);
""")

print("Tabela 'minha_tabela' criada a partir do arquivo Excel!")