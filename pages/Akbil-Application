import streamlit as st
st.title("Akbil Uygulaması")

abonman=200
biletfiyat=20
bakiye = st.number_input("Bakiyenizi Belirtiniz: ")
kartdurum  = st.text_input("Abonman mı E veya H olarak değer belirtiniz: ")
bayramdurum = st.text_input("Bayram mı E veya H olarak değer belirtiniz: ")
if bayramdurum.upper()=="E":
  st.write("Ücretsiz Geçiş, İyi Bayramlar Dileriz.")
elif kartdurum.upper()=="E":
  abonman = abonman-1
  st.write("Kalan Abonman Kullanım: ",abonman, "Adet, İyi Günler Dileriz.")
elif bakiye < 20 :
  st.write("Yetersiz Bakiye.")
else:
  bakiye = bakiye-20
  st.write("Kalan Bakiyeniz:" ,bakiye, "TL, İyi Günler Dileriz.")

kod='''
import streamlit as st
st.title("Akbil Uygulaması")

abonman=146
biletfiyat=20
bakiye = st.number_input("Bakiyenizi Belirtiniz: ")
kartdurum  = st.text_input("Abonman mı E veya H olarak değer belirtiniz: ")
bayramdurum = st.text_input("Bayram mı E veya H olarak değer belirtiniz: ")
if bayramdurum.upper()=="E":
  st.write("Ücretsiz Geçiş, İyi Bayramlar Dileriz.")
elif kartdurum.upper()=="E":
  abonman = abonman-1
  st.write("Kalan Abonman Kullanım: ",abonman, "Adet, İyi Günler Dileriz.")
elif bakiye < 20 :
  st.write("Yetersiz Bakiye.")
else:
  bakiye = bakiye-20
  st.write("Kalan Bakiyeniz:" ,bakiye, "TL, İyi Günler Dileriz.")
'''

st.header('Kaynak Kodları')
st.code(kod,language='python')
