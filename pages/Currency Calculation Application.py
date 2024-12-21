import streamlit as st
import requests

st.title("Kur Hesaplama Uygulaması")

url = f"https://open.er-api.com/v6/latest/USD"
response = requests.get(url)
data=response.json()
kur = data.get('rates')
kursec = st.selectbox("Çevirmek İstediğiniz Kuru Seçin: ", (kur))
miktar = st.number_input("Miktar Giriniz: ")
kursecim = st.selectbox("Çevirilecek İstediğiniz Kuru Seçin: ", (kur))

if kursec in kur:
    url = f"https://open.er-api.com/v6/latest/{kursec}"
    response = requests.get(url)
    data = response.json()
    kur = data.get('rates')

btn = st.button("Dönüştür")
if btn:
    for doviz in kur:
        dovizsec = kur.get(doviz)
        if doviz == kursecim:
            donusum = miktar * dovizsec
            st.write(f"{miktar} {kursec} = {donusum} {kursecim}")
            
kod='''
import streamlit as st
import requests

st.title("Kur Hesaplama Uygulaması")

url = f"https://open.er-api.com/v6/latest/USD"
response = requests.get(url)
data=response.json()
kur = data.get('rates')
kursec = st.selectbox("Çevirmek İstediğiniz Kuru Seçin: ", (kur))
miktar = st.number_input("Miktar Giriniz: ")
kursecim = st.selectbox("Çevirilecek İstediğiniz Kuru Seçin: ", (kur))

if kursec in kur:
    url = f"https://open.er-api.com/v6/latest/{kursec}"
    response = requests.get(url)
    data = response.json()
    kur = data.get('rates')

btn = st.button("Dönüştür")
if btn:
    for doviz in kur:
        dovizsec = kur.get(doviz)
        if doviz == kursecim:
            donusum = miktar * dovizsec
            st.write(f"{miktar} {kursec} = {donusum} {kursecim}")
'''
st.header('Kaynak Kodları')
st.code(kod,language='python')
