import streamlit as st
print("Hello")

print("Yıllık Gelir Hesaplama Sistemi")
st.title("Yıllık Gelir Hesaplama Uygulaması")
gelir = st.number_input("Yıllık Gelir Bilginizi Belirtiniz: ")
a = 0.15
b = 0.20
c = 0.27
d = 0.35
e = 0.40
if gelir <= 110000:
  vergi = gelir*a
  st.write(gelir, "TL'lik Yıllık Gelirinizin Vergisi: ",vergi, "TL")
  net = gelir - vergi
  st.write("Net Kalan Bütçe:",net, "TL")
elif gelir >=110001 and gelir <=230000:
    vergi = (gelir - 110000)*b
    vergi = vergi + (110000*a)
    st.write(gelir, "TL'lik Yıllık Gelirinizin Vergisi:",vergi, "TL")
    net = gelir - vergi
    st.write("Net Kalan Bütçe:",net, "TL")
elif gelir >=230001 and gelir <=580000:
    vergi = (gelir - 230000)*c
    vergi = vergi + (110000*a) + (230000-110000)*b
    st.write(gelir, "TL'lik Yıllık Gelirinizin Vergisi: ",vergi, "TL")
    net = gelir - vergi
    st.write("Net Kalan Bütçe:",net, "TL")
elif gelir >=580001 and gelir <= 3000000:
    vergi = (gelir - 580000)*d
    vergi = vergi + (110000*a) + ((230000-110000)*b) + (580000-230000)*c
    st.write(gelir, "TL'lik Yıllık Gelirinizin Vergisi: ",vergi, "TL")
    net = gelir - vergi
    st.write("Net Kalan Bütçe:",net, "TL")
elif gelir >=3000001:
    vergi = (gelir - 3000000)*e
    vergi = vergi + (110000*a) + ((230000-110000)*b) + ((580000-230000)*c) + (3000000-580000)*d
    st.write(gelir, "TL'lik Yıllık Gelirinizin Vergisi: ",vergi, "TL")
    net = gelir - vergi
    st.write("Net Kalan Bütçe:",net, "TL")

kod='''
import streamlit as st
print("Hello")

print("Yıllık Gelir Hesaplama Sistemi")
st.title("Yıllık Gelir Hesaplama Uygulaması")
gelir = st.number_input("Yıllık Gelir Bilginizi Belirtiniz: ")
a = 0.15
b = 0.20
c = 0.27
d = 0.35
e = 0.40
if gelir <= 110000:
  vergi = gelir*a
  st.write(gelir, "TL'lik Yıllık Gelirinizin Vergisi: ",vergi, "TL")
  net = gelir - vergi
  st.write("Net Kalan Bütçe:",net, "TL")
elif gelir >=110001 and gelir <=230000:
    vergi = (gelir - 110000)*b
    vergi = vergi + (110000*a)
    st.write(gelir, "TL'lik Yıllık Gelirinizin Vergisi:",vergi, "TL")
    net = gelir - vergi
    st.write("Net Kalan Bütçe:",net, "TL")
elif gelir >=230001 and gelir <=580000:
    vergi = (gelir - 230000)*c
    vergi = vergi + (110000*a) + (230000-110000)*b
    st.write(gelir, "TL'lik Yıllık Gelirinizin Vergisi: ",vergi, "TL")
    net = gelir - vergi
    st.write("Net Kalan Bütçe:",net, "TL")
elif gelir >=580001 and gelir <= 3000000:
    vergi = (gelir - 580000)*d
    vergi = vergi + (110000*a) + ((230000-110000)*b) + (580000-230000)*c
    st.write(gelir, "TL'lik Yıllık Gelirinizin Vergisi: ",vergi, "TL")
    net = gelir - vergi
    st.write("Net Kalan Bütçe:",net, "TL")
elif gelir >=3000001:
    vergi = (gelir - 3000000)*e
    vergi = vergi + (110000*a) + ((230000-110000)*b) + ((580000-230000)*c) + (3000000-580000)*d
    st.write(gelir, "TL'lik Yıllık Gelirinizin Vergisi: ",vergi, "TL")
    net = gelir - vergi
    st.write("Net Kalan Bütçe:",net, "TL")
'''

st.header('Kaynak Kodları')
st.code(kod,language='python')
