import streamlit as st
import random
import string
st.title("Şifre Belirleme Uygulaması")

kh = string.ascii_lowercase
bh = string.ascii_uppercase
rk = string.digits
sy = string.punctuation

khsec =random.choices(kh, k=2)
bhsec =random.choices(bh, k=2)
rksec = random.choices(rk, k=2)
sysec =random.choices(sy, k=2)
sifre = khsec+bhsec+rksec+sysec
random.shuffle(sifre)
sifre = "".join(sifre)
st.write("Şifre Üretmek İçin Butona Tıklayınız.")
btn = st.button("Şifre Üret")
if btn:
    st.write(sifre)

kod='''
import streamlit as st
import random
import string
st.title("Şifre Belirleme Uygulaması")

kh = string.ascii_lowercase
bh = string.ascii_uppercase
rk = string.digits
sy = string.punctuation

khsec =random.choices(kh, k=2)
bhsec =random.choices(bh, k=2)
rksec = random.choices(rk, k=2)
sysec =random.choices(sy, k=2)
sifre = khsec+bhsec+rksec+sysec
random.shuffle(sifre)
sifre = "".join(sifre)
st.write("Şifre Üretmek İçin Butona Tıklayınız.")
btn = st.button("Şifre")
if btn:
    st.write(sifre)
'''
st.header('Kaynak Kodları')
st.code(kod,language='python')
