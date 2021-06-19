
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
    st.subheader("Resultados de tus parámetros antropometricos")
    imc=peso/talla**2
    imc2=int(imc)
    st.subheader(imc2)
    if imc2 <18.5:
        st.subheader("Estas en bajo peso")
    elif imc2 >18.5 and <24.9:
        st.subheader("Peso normal, no requieres intervención quirúrgica")
    elif imc2 >25 and <29.9:
        st.subheader("Sobrepeso, se requiere manejo médico y control de habitos dieteticos")
    elif imc2 >29.9 and <34.9:
        st.subheader("Obesidad grado I")
        comorb=st.checkbox("Tienes alguna enfermedad como Diabetes mellitus, hipertensión arterial, dislipidemias")
        if comorb==True:
            st.subheader("Eres candidato a cirugía bariátrica")
        else:
            st.subheader("Debes mantener un estilo de vida saludable, con dieta para reducción de peso y aumentar ejercicio físico")
    elif imc2 >35 and <39.9:
        st.subheader("Obesidad grado II")
        st.write("Requieres manejo médico, nutricional y de hábitos, tambien eres candidato a cirugía batriátrica como la Manga gástrica (gastrectomia vertical")
    elif imc2 >40:
        st.subheader("Obesidad grado III")
        st.write("Estas en alto riesgo de enfermedades metabolicas, y tu riesgo de muerte es mayor al de una persona sin obesidad, se sugiere que seas valorado por un cirujano bariatra y un equimo médico")


#Agregar un if para el IMC mayor a 35 con comorbilidades
#If para un IMC mayor a 40 sin comorbilidades
#valorar edad
#si tiene ERGE o Barret no se debe hacer la Gastrectomia en manga
#Trastorno psiquiatrico no controlado es otra contraindicacion
