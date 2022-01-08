# streamlit_app.py
import streamlit as st
import psycopg2

# Initialize connection.
# Uses st.cache to only run once.
@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

tablas = run_query("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
lista = []
for table in tablas:
    lista.append(str(table)[2:-3])

df_tables = pd.DataFrame(lista)
df_tables.columns=['Tablas']

if lista != []: st.dataframe(df_tables)
