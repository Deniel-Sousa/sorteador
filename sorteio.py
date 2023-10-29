from random import choice
import streamlit as st
from time import sleep

st.title('FESTIVAL DE PRÊMIOS MARANATHA')

inicial = st.sidebar.text_input('Número incial', value='1')
final = st.sidebar.text_input('Número final', value='100')

numeros = list(range(int(inicial), int(final)+1))

def sorteio():
    sorteado = choice(numeros)
    return sorteado

if st.button('Sortear'):
    st.balloons()
    sleep(1)
    sorteado = sorteio()
    #st.header(f'número {sorteado}') 
    st.write(f'<div style="text-align: center; font-size: {250}px;">{sorteado}</div>', unsafe_allow_html=True)
