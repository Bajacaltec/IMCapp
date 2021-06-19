
import streamlit as st
st.image("logo.jpeg")

st.title("IMCapp ")
st.text("Bievenido utiliza nuestra APP para saber")
st.text("tu Indice de masa corporal (IMC)")

nombre=st.text_input("Nombre del usuario")

st.subheader("Bienvenido " + nombre)
edad=st.number_input("Edad")
peso=st.number_input("Peso")
talla=st.number_input("Talla en metros")
butace=st.button("Registrar datos")
if butace==True:
    st.subheader("Resultados de tus parámetros antropometricos")
    imc=peso/talla**2
    st.subheader(imc)


#Agregar un if para el IMC mayor a 35 con comorbilidades
#If para un IMC mayor a 40 sin comorbilidades
#valorar edad
#si tiene ERGE o Barret no se debe hacer la Gastrectomia en manga
#Trastorno psiquiatrico no controlado es otra contraindicacion
