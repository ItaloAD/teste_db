import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import pymysql

def conectar_db_spec (user,password,host,db):
    return create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")

def conectar_db(user,password,host):
    return create_engine(f"mysql+pymysql://{user}:{password}@{host}")

def fetch_data(engine, table_name):
    query = f"SELECT * FROM {table_name}"
    with engine.connect() as conn:
        data = pd.read_sql(query, conn)
    return data

st.title("Teste")

ip_publico = st.text_input("IP Público", "177.70.175.53")
porta = st.text_input("Porta", "3715")

user = "aws"
password = "123"
host = f"{ip_publico}:{porta}"
db_name = "ewma_spot"

engine = conectar_db_spec(user,password,host,db_name)

table_name = st.text_input("Nome da Tabela", "abev3").lower()

if table_name:
    data = fetch_data(engine, table_name)
    st.write(f"Exibindo dados da tabela: {table_name}")
    st.dataframe(data)
else:
    st.write("Por favor, insira o nome de uma tabela.")