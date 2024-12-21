import streamlit as st
import requests

st.title("Soru Cevap")

response = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode')
veri=response.json()
soru=veri.get('setup')
st.write(soru)

cevap=veri.get('delivery')
btn = st.button("Cevabı Göster")
if btn:
    st.write(cevap)
    
kod='''
import streamlit as st
import requests

st.title("Soru Cevap")

response = requests.get('https://v2.jokeapi.dev/joke/Any?safe-mode')
veri=response.json()
soru=veri.get('setup')
st.write(soru)

cevap=veri.get('delivery')
btn = st.button("Cevabı Göster")
if btn:
    st.write(cevap)
'''

st.header('Kaynak Kodları')
st.code(kod,language='python')
