import streamlit as st
import string

st.title("Güvenli Şifre Kontrol Uygulaması")
bh = string.ascii_uppercase
kh = string.ascii_lowercase
rk = string.digits
sy = string.punctuation

sifre = st.text_input("Bir Şifre Oluşturunuz: ")

khsayac = 0
bhsayac = 0
rksayac = 0
sysayac = 0

for x in sifre:
    if x in kh:
        khsayac =+1
        continue
    if x in bh:
        bhsayac =+1
        continue
    if x in rk:
        rksayac =+1
        continue
    if x in sy:
        sysayac =+1

if khsayac == 1 and bhsayac == 1 and rksayac == 1 and sysayac == 1 and len(sifre) >= 8:
    st.write("Şifre Güvenli.")
else:
    st.write("Şifre Güvenli Değil. Yeni Şifre Oluşturunuz.")

kod='''
import streamlit as st
import string

st.title("Güvenli Şifre Kontrol Uygulaması")
bh = string.ascii_uppercase
kh = string.ascii_lowercase
rk = string.digits
sy = string.punctuation

sifre = st.text_input("Bir Şifre Oluşturunuz: ")

khsayac = 0
bhsayac = 0
rksayac = 0
sysayac = 0

for x in sifre:
    if x in kh:
        khsayac =+1
        continue
    if x in bh:
        bhsayac =+1
        continue
    if x in rk:
        rksayac =+1
        continue
    if x in sy:
        sysayac =+1

if khsayac == 1 and bhsayac == 1 and rksayac == 1 and sysayac == 1 and len(sifre) >= 8:
    st.write("Şifre Güvenli.")
else:
    st.write("Şifre Güvenli Değil. Yeni Şifre Oluşturunuz.")
'''

st.header('Kaynak Kodları')
st.code(kod,language='python')
