import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parametros")
st.write("Elaborado por: Farid Estefano Garibay Fabian")

valor_inicial: st.number_input("Ingrese el valor inicial")
valor_final: st.number_input("Ingrese el valor final")

lista_números = list(range(valor_inicial, valor_final))

st.write(lista_números)
