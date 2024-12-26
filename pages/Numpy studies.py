import streamlit as st
import numpy as np

st.title("Nump Çalışmaları")

st.header("Mağaza zinciri satış analizi")
st.write("-3 farklı şube var.")
st.write("-Her şube için 4 ayrı satış verileri var.")

st.header("Yapılacak Analizler")
st.write("-Her şubenin toplam ve ortalama satışlarını hesaplama.")
st.write("-Her ayın toplam satışı.")
st.write("-Şirket genelindeki en yüksek ve en düşük aylık satışlar.")
st.write("-%20 artış yapılması.")
st.write("-Şirketin genel toplam satışı.")

satislar=np.array([[10000,15000,20000,17000],[17500,18000,15000,18000],[20000,10000,15000,19000]])
st.write(satislar)

st.header("Yapılan İşlemler")
#ŞUBELERİN ORTALAMA SATIŞLARI
subeSatisOrt = np.mean(satislar,axis=1)
st.write(f"Şubelerin Ortalama Satışları: {subeSatisOrt}")

#ŞUBELERİN TOPLAM SATIŞLARI
subeSatisToplam = np.sum(satislar,axis=1)
st.write(f"Şubelerin Toplam Satışları: {subeSatisToplam}")

#ŞUBELERİN AYLIK SATIŞLARININ TOPLAMI
aylikToplam = np.sum(satislar,axis=0)
st.write(f"Şubelerin Aylık Toplam Satışları: {aylikToplam}")

#ŞİRKET GENELİNDE AYLIK EN YÜKSEK ve EN DÜŞÜK SATIŞLARI
enYuksekSatis = np.max(satislar)
st.write(f"Şirket Genelinde En Yüksek Maaş: {enYuksekSatis}")

enDusukSatis = np.min(satislar)
st.write(f"Şirket Genelinde En Düşük Maaş: {enDusukSatis}")

#%20 FİYAT ARTIŞI
artisFiyat = satislar*1.20
st.write(f"%20 Artışlı Satış Fiyatları:")
st.write(artisFiyat)

#ŞİRKETİN GENEL TOPLAM SATIŞI
genelToplam = np.sum(satislar)
st.write(f"Genel Toplam: {genelToplam}")

kod="""
import streamlit as st
import numpy as np

st.title("Nump Çalışmaları")

st.header("Mağaza zinciri satış analizi")
st.write("-3 farklı şube var.")
st.write("-Her şube için 4 ayrı satış verileri var.")

st.header("Yapılacak Analizler")
st.write("-Her şubenin toplam ve ortalama satışlarını hesaplama.")
st.write("-Her ayın toplam satışı.")
st.write("-Şirket genelindeki en yüksek ve en düşük aylık satışlar.")
st.write("-%20 artış yapılması.")
st.write("-Şirketin genel toplam satışı.")

satislar=np.array([[10000,15000,20000,17000],[17500,18000,15000,18000],[20000,10000,15000,19000]])
st.write(satislar)

st.header("Yapılan İşlemler")
#ŞUBELERİN ORTALAMA SATIŞLARI
subeSatisOrt = np.mean(satislar,axis=1)
st.write(f"Şubelerin Ortalama Satışları: {subeSatisOrt}")

#ŞUBELERİN TOPLAM SATIŞLARI
subeSatisToplam = np.sum(satislar,axis=1)
st.write(f"Şubelerin Toplam Satışları: {subeSatisToplam}")

#ŞUBELERİN AYLIK SATIŞLARININ TOPLAMI
aylikToplam = np.sum(satislar,axis=0)
st.write(f"Şubelerin Aylık Toplam Satışları: {aylikToplam}")

#ŞİRKET GENELİNDE AYLIK EN YÜKSEK ve EN DÜŞÜK SATIŞLARI
enYuksekSatis = np.max(satislar)
st.write(f"Şirket Genelinde En Yüksek Maaş: {enYuksekSatis}")

enDusukSatis = np.min(satislar)
st.write(f"Şirket Genelinde En Düşük Maaş: {enDusukSatis}")

#%20 FİYAT ARTIŞI
artisFiyat = satislar*1.20
st.write(f"%20 Artışlı Satış Fiyatları:")
st.write(artisFiyat)

#ŞİRKETİN GENEL TOPLAM SATIŞI
genelToplam = np.sum(satislar)
st.write(f"Genel Toplam: {genelToplam}")
"""

st.header('Kaynak Kodları')
st.code(kod,language='python')
