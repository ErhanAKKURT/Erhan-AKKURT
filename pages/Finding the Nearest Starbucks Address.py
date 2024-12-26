import streamlit as st
import pandas as pd
import folium
from folium import plugins

st.subheader("Konumunuza En Yakın Starbucks Adresini Bulma")

df=pd.read_json('https://raw.githubusercontent.com/mmcloughlin/starbucks/refs/heads/master/locations.json')

st.write("Json dosyası içerisindeki İlk 5 Veriyi Görelim")
st.write(df.head()) #Json dosyası içerisindeki İlk 5 Veriyi Görelim

#Bulunduğumuz yerin Enlem ve Boylam değerleri
#40.9891149, 28.9413237
me_lon=(29.0211496) #Boylam
me_lat=(40.9891482) #Enlem

lon=df['longitude']
lat=df['latitude']

df['Mesafe']=((me_lon-lon)**2 + (me_lat-lat)**2)**0.5 #İki nokta arasındaki uzaklık hesaplaması.

st.write("Hesapladığımız Mesafe Kolonunu Tabloda Görelim")
st.write(df.head())

st.write("Bulunduğumuz Konuma En Yakın Starbucks Şubelerini Görelim")
df=df.sort_values('Mesafe',ascending=True) #Bulunduğumuz noktaya en yakın 5 starbucks
st.write(df.head())

m = folium.Map(location=[me_lat, me_lon], zoom_start=12)
folium.Marker(location=[me_lat, me_lon], popup="Benim Konumum").add_to(m)
folium.Circle(location=[me_lat, me_lon], radius=5000, color='blue', fill=True).add_to(m)
m_html = m._repr_html_()
st.write("Konumumuza En Yakın Şubeyi Harita Üzerinde Görelim")
st.components.v1.html(m_html, width=700, height=500)

st.write("Harita Üzerinde Hangi İlçede Kaç adet Starbucks Adresi var Gruplandırma")
df['Mesafe'] = ((me_lon - df['longitude'])**2 + (me_lat - df['latitude'])**2)**0.5
n5 = df.head(5)
m = folium.Map(location=[me_lat, me_lon], zoom_start=12)
for i in range(5):
    folium.Marker(location=n5[['latitude', 'longitude']].iloc[i].values).add_to(m)
world = df[['latitude', 'longitude']]
plugins.MarkerCluster(locations=world.values.tolist()).add_to(m)
m_html = m._repr_html_()
st.components.v1.html(m_html, width=700, height=500)

kod='''
import streamlit as st
import pandas as pd
import folium
from folium import plugins

st.subheader("Konumunuza En Yakın Starbucks Adresini Bulma")

df=pd.read_json('https://raw.githubusercontent.com/mmcloughlin/starbucks/refs/heads/master/locations.json')

st.write("Json dosyası içerisindeki İlk 5 Veriyi Görelim")
st.write(df.head()) #Json dosyası içerisindeki İlk 5 Veriyi Görelim

#Bulunduğumuz yerin Enlem ve Boylam değerleri
#40.9891149, 28.9413237
me_lon=(29.0211496) #Boylam
me_lat=(40.9891482) #Enlem

lon=df['longitude']
lat=df['latitude']

df['Mesafe']=((me_lon-lon)**2 + (me_lat-lat)**2)**0.5 #İki nokta arasındaki uzaklık hesaplaması.

st.write("Hesapladığımız Mesafe Kolonunu Tabloda Görelim")
st.write(df.head())

st.write("Bulunduğumuz Konuma En Yakın Starbucks Şubelerini Görelim")
df=df.sort_values('Mesafe',ascending=True) #Bulunduğumuz noktaya en yakın 5 starbucks
st.write(df.head())

m = folium.Map(location=[me_lat, me_lon], zoom_start=12)
folium.Marker(location=[me_lat, me_lon], popup="Benim Konumum").add_to(m)
folium.Circle(location=[me_lat, me_lon], radius=5000, color='blue', fill=True).add_to(m)
m_html = m._repr_html_()
st.write("Konumumuza En Yakın Şubeyi Harita Üzerinde Görelim")
st.components.v1.html(m_html, width=700, height=500)

st.write("Harita Üzerinde Hangi İlçede Kaç adet Starbucks Adresi var Gruplandırma")
df['Mesafe'] = ((me_lon - df['longitude'])**2 + (me_lat - df['latitude'])**2)**0.5
n5 = df.head(5)
m = folium.Map(location=[me_lat, me_lon], zoom_start=12)
for i in range(5):
    folium.Marker(location=n5[['latitude', 'longitude']].iloc[i].values).add_to(m)
world = df[['latitude', 'longitude']]
plugins.MarkerCluster(locations=world.values.tolist()).add_to(m)
m_html = m._repr_html_()
st.components.v1.html(m_html, width=700, height=500)
'''

st.header('Kaynak Kodları')
st.code(kod,language='python')
