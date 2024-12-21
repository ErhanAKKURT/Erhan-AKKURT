import streamlit as st
import requests

st.title("Kripto Para Çevirici")

response=requests.get('https://api.coincap.io/v2/assets') #Api adresi
veri=response.json() #json veriyi python a çevirme
veri=veri.get('data') #data isimli key çekiliyor. veri değişkenine

#kur alma çalışması
responseKur=requests.get('https://open.er-api.com/v6/latest/USD')
veriKur=responseKur.json()
veriKur=veriKur.get('rates')


coinler={} # coinler isimli bir dictionary oluşturuldu. içi boş

for c in veri:
    coinler.update({c.get("name"):float(c.get("priceUsd"))})
    #coinler isimli dict içerisini key ve value ile dolduruyoruz

coin1=st.sidebar.selectbox("Coin Seç",coinler.keys())
#sidebar tarafında bir selectbox açıp coin keyleri alıyoruz.
adet=st.sidebar.number_input("Adet",step=1)
coin2=st.sidebar.selectbox("Hedef Coin Seç",coinler.keys())
kursecim = st.sidebar.selectbox("Çevirmek İstediğiniz Kuru Seçiniz: ",(veriKur))
tryVerisi=veriKur.get(kursecim)

fiyat1=coinler.get(coin1)
fiyat2=coinler.get(coin2)
sonuc=fiyat1/fiyat2*adet*tryVerisi
sonuc1=fiyat1/fiyat2*adet
st.write(f"{adet} {coin1} = {sonuc1} {coin2}")
st.write(f"{sonuc1} {coin2} = {sonuc} {kursecim}")

kod='''
import streamlit as st
import requests

st.title("Kripto Para Çevirici")

response=requests.get('https://api.coincap.io/v2/assets') #Api adresi
veri=response.json() #json veriyi python a çevirme
veri=veri.get('data') #data isimli key çekiliyor. veri değişkenine

#kur alma çalışması
responseKur=requests.get('https://open.er-api.com/v6/latest/USD')
veriKur=responseKur.json()
veriKur=veriKur.get('rates')


coinler={} # coinler isimli bir dictionary oluşturuldu. içi boş

for c in veri:
    coinler.update({c.get("name"):float(c.get("priceUsd"))})
    #coinler isimli dict içerisini key ve value ile dolduruyoruz

coin1=st.sidebar.selectbox("Coin Seç",coinler.keys())
#sidebar tarafında bir selectbox açıp coin keyleri alıyoruz.
adet=st.sidebar.number_input("Adet",step=1)
coin2=st.sidebar.selectbox("Hedef Coin Seç",coinler.keys())
kursecim = st.sidebar.selectbox("Çevirmek İstediğiniz Kuru Seçiniz: ",(veriKur))
tryVerisi=veriKur.get(kursecim)

fiyat1=coinler.get(coin1)
fiyat2=coinler.get(coin2)
sonuc=fiyat1/fiyat2*adet*tryVerisi
sonuc1=fiyat1/fiyat2*adet
st.write(f"{adet} {coin1} = {sonuc1} {coin2}")
st.write(f"{sonuc1} {coin2} = {sonuc} {kursecim}")
'''

st.header('Kaynak Kodları')
st.code(kod,language='python')
