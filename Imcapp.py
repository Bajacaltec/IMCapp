
from typing import Text
import streamlit as st
#streamlit.text_input(label, value='', max_chars=None, key=None, type='default', help=None)
#streamlit.number_input(label, min_value=None, max_value=None, value=<streamlit.widgets.NoValue object>, step=None, format=None, key=None, help=None)
st.image("logo.jpeg")

st.subheader("IMCapp ")
st.subheader("Bievenido utiliza nuestra APP para saber tu indice de masa corporal")
st.subheader("Ingresa los datos solicitados para saber tu IMC y las recomendaciones actuales")

nombre=st.text_input("Nombre del usuario")
if not nombre:
    st.warning("Ingresa tu nombre")
    st.stop()
st.success("Gracias por ingresar tu nombre "+nombre)
edad=st.number_input("Edad",1,99)
peso=st.number_input("Peso",1,400)
talla=st.number_input("Talla en metros",1.0,2.5)
butace=st.button("Registrar datos")
if butace==True:
    imc=peso/talla**2
    imce=float(imc)
    imc2=round(imc,2)
    col1,col2,col3=st.beta_columns(3)
    with col1:
        st.title("Tu IMC es:")
    with col2:
        st.info(imc2)
    if imc2 < 18.5:
        col1,col2=st.beta_columns(2)
        with col1:
            st.warning("Bajo peso")
            st.write("")
        with col2:
            st.info("Requieres aumentar tu ingesta calórica")
            st.success(" RECOMENDACIÓN: utilizar suplementos alimenticios")
    elif imc2 > 18.5 and imc2 <= 24.9:
        col1, col2=st.beta_columns(2)
        with col1:
            st.success("Peso normal")
        with col2:
            st.info("No requieres intervención quirúrgica")
            st.info("Felicidades por mantener un peso adecuado")
        st.balloons()
        
    elif imc2 > 25 and imc2 < 29.9:
        col1,col2=st.beta_columns(2)
        with col1:
            st.warning("Sobrepeso")
        with col2:
            st.warning("Requieres disminuir tu peso para disminuir el riesgo de enfermedades metabolicas")
    elif imc2 > 29.9 and imc2 < 34.9:
        st.info("Obesidad grado I")
        st.warning ("No eres candidato a cirugía bariátrica, Recomendacion: dieta y aumento de actividad física")
        # no funciona correctamentecomorb=st.selectbox("Tienes alguna enfermedad como Diabetes mellitus, hipertensión arterial, dislipidemias",("si","no"))
        #if comorb=="si":
           # st.subheader("Eres candidato a cirugía bariátrica")
        #else:
            #st.subheader ("No eres candidato a cirugía bariátrica, se recomenda la reducción de peso con dieta y ejercicio físico")
    elif imc2 >35 and imc2 <39.9:
        st.info("Obesidad grado II")
        st.warning("Requieres manejo médico, nutricional y de hábitos, tambien eres candidato a cirugía batriátrica como la Manga gástrica (gastrectomia vertical")
    elif imc2 >40:
        st.info("Obesidad grado III")
        st.error("Estas en alto riesgo de enfermedades metabolicas, y tu riesgo de muerte es mayor al de una persona sin obesidad, se sugiere que seas valorado por un cirujano bariatra y un equipo médico")
#st.form("Registra tus datos"):

#col1,col2,col3=st.beta_columns(3)
#with col1:
    #st.write("blablablabla")
    
#st.error da un cuadro rojo
#st.info da un cuadro azul claro
#st.warning da un cuadro amarillo

#Agregar un if para el IMC mayor a 35 con comorbilidades
#If para un IMC mayor a 40 sin comorbilidades
#valorar edad
#si tiene ERGE o Barret no se debe hacer la Gastrectomia en manga
#Trastorno psiquiatrico no controlado es otra contraindicacion
