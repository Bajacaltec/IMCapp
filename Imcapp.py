
import streamlit as st
st.image("logo.jpeg")

st.subheader("IMCapp ")
st.subheader("Bievenido utiliza nuestra APP para saber tu indice de masa corporal")
st.subheader("Ingresa los datos solicitados para saber tu IMC y las recomendaciones actuales")

nombre=st.text_input("Nombre del usuario")
if not nombre:
    st.warning("Ingresa tu nombre por favor")
    st.stop()
st.success("Gracias por ingresar tu nombre "+nombre)
edad=st.number_input("Edad")
peso=st.number_input("Peso")
talla=st.number_input("Talla en metros")
butace=st.button("Registrar datos")
if butace==True:
    st.subheader("Resultados de tus parámetros antropometricos")
    imc=peso/talla**2
    imc2=int(imc)
    st.subheader(imc2)
    if imc2 


#Agregar un if para el IMC mayor a 35 con comorbilidades
#If para un IMC mayor a 40 sin comorbilidades
#valorar edad
#si tiene ERGE o Barret no se debe hacer la Gastrectomia en manga
#Trastorno psiquiatrico no controlado es otra contraindicacion
