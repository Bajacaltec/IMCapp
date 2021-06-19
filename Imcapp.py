
from typing import Text
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
    imc=peso/talla**2
    imc2=float(imc)
    st.subheader("Resultados de tus parámetros antropometricos")
    st.subheader(imc2)
    if imc2 < 18.5:
        st.subheader("Bajo peso")
        st.write("")
        st.write("Requieres aumentar tu ingesta calórica, puedes utilizar suplementos alimenticios")
    elif imc2 > 18.5 and imc2 < 24.9:
        st.subheader("Peso normal, no requieres intervención quirúrgica")
    elif imc2 > 25 and imc2 < 29.9:
        st.subheader("Sobrepeso, se requiere manejo médico y control de habitos dieteticos")
    elif imc2 > 29.9 and imc2 < 34.9:
        st.subheader("Obesidad grado I")
        st.text ("No eres candidato a cirugía bariátrica, Recomendacion: dieta y aumento de actividad física")
        # no funciona correctamentecomorb=st.selectbox("Tienes alguna enfermedad como Diabetes mellitus, hipertensión arterial, dislipidemias",("si","no"))
        #if comorb=="si":
           # st.subheader("Eres candidato a cirugía bariátrica")
        #else:
            #st.subheader ("No eres candidato a cirugía bariátrica, se recomenda la reducción de peso con dieta y ejercicio físico")
    elif imc2 >35 and imc2 <39.9:
        st.subheader("Obesidad grado II")
        st.write("Requieres manejo médico, nutricional y de hábitos, tambien eres candidato a cirugía batriátrica como la Manga gástrica (gastrectomia vertical")
    elif imc2 >40:
        st.subheader("Obesidad grado III")
        st.write("Estas en alto riesgo de enfermedades metabolicas, y tu riesgo de muerte es mayor al de una persona sin obesidad, se sugiere que seas valorado por un cirujano bariatra y un equipo médico")
st.form("Registra tus datos"):

#col1,col2,col3=st.beta_columns(3)
#with col1:
    #st.write("blablablabla")
    

#Agregar un if para el IMC mayor a 35 con comorbilidades
#If para un IMC mayor a 40 sin comorbilidades
#valorar edad
#si tiene ERGE o Barret no se debe hacer la Gastrectomia en manga
#Trastorno psiquiatrico no controlado es otra contraindicacion
