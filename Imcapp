
import streamlit as st
st.image("logo.jpeg")

st.title("IMCapp ")
st.text("Bievenido utiliza nuestra APP para saber tu Indice de masa corporal (IMC)")
st.text("")

st.sidebar.subheader("Bienvenido al MEDPOST")
st.sidebar.text("Ingresa los datos solicitados")
nombre=st.sidebar.text_input("Nombre del usuario")

st.sidebar.subheader("Bienvenido " + nombre)
edad=st.sidebar.number_input("Edad")
peso=st.sidebar.number_input("Peso")
talla=st.sidebar.number_input("Talla en metros")
butace=st.sidebar.button("Registrar datos")
if butace==True:
    st.subheader("Resultados de tus parámetros antropometricos")
    imc=peso/talla**2
    st.subheader(imc)

