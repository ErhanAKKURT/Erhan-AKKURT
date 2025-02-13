import streamlit as st
import pandas as pd

st.markdown('<h1 style="color:#274866;">Konut Yatırım Projesi</h1>', unsafe_allow_html=True)

with st.sidebar:
    st.caption("Form'da belirtecek olduğunuz değerler arasında Daire alma ve Borç süreçlerinizi inceleyebilirsiniz.")
    belirtilenYas = st.slider("Yaş Aralığını Belirtiniz:", 0, 130, (25, 65))
    st.caption(f":blue[Belirtmiş olduğunuz yaş ' {belirtilenYas[0]}-{belirtilenYas[1]} ' yaş aralığıdır.]")
    toplamAy = int((belirtilenYas[1] - belirtilenYas[0]) * 12)
    mevcutAy = 1

    anaPara = st.number_input("Sermayeniz(₺):", value=0, step=100000)
    if anaPara > 0:
        st.caption(f"Sermayeniz {anaPara} olarak belirlenmiştir.")
    aylikGelir = st.number_input("Aylık Geliriniz(₺):", value=3000, step=1000)
    kiraGelir = st.number_input("Daireniz için Kira Geliri(₺):", value=8000, step=1000)
    evFiyat = st.number_input("Daire Fiyatını Belirtiniz:(₺):", value=1250000, step=50000)
    pesinatYuzde = st.slider("Peşinat Yüzdesini Belirtiniz:", 0, 100, 20)
    pesinat = evFiyat * pesinatYuzde / 100
    krediSure = st.number_input("Kredi süresini seçiniz (Yıl):", value=15)
    krediAy = krediSure * 12
    krediyil = krediSure
    krediOdeme = (evFiyat - pesinat) / krediAy
    st.caption(f":blue[Alacak olduğunuz bir daire için {str(krediyil)} yıl ({krediAy} ay), aylık kredi ödemeniz {round(krediOdeme)} ₺'dir.]")

with st.container():
    with st.container(border=True):
        st.write("Form'da Doldurduğunuz Bilgiler:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.caption(f"Sermayeniz: :blue[{anaPara} ₺]")
        with col2:
            st.caption(f"Aylık Geliriniz: :blue[{aylikGelir} ₺]")
        with col3:
            st.caption(f"Dire Fiyatı: :blue[{evFiyat} ₺]")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.caption(f"Kira Gelir Beklentisi: :blue[{kiraGelir} ₺]")
        with col2:
            st.caption(f"Kredi Süresi: :blue[{krediSure} yıl - ({krediAy}) ay]")
        with col3:
            st.caption(f"Belirtmiş Olduğunuz Yaş: :blue[{belirtilenYas[0]}-{belirtilenYas[1]} yaş]")
        st.caption(f"Ödenecek Peşinat: Seçmiş olduğunuz Peşinat Yüzdesi :blue[%{pesinatYuzde}]'dir. "
                    f"Buna göre, :blue[{format(int(evFiyat),',')} ₺] değerindeki daire için, :blue[{round(krediOdeme)} ₺] ödemeniz çıkmaktadır.")

st.caption(':blue[NOT: Butona tıkladığınız an da yukarıda belirtmiş olduğunuz değerler çerçevesinde hesaplama yapılacaktır!]')

mevcutEv=0
aylikKrediList=[]
ilkGelir=aylikGelir
toplamKrediBorcu=0 #toplam kredi borcumuz
aylikNetGelirList=[]
anaParaList=[]
krediborcls=[]
dateList=[]
krediAdetList=[]
mevcutEvList=[]

for i in range(mevcutAy,toplamAy+1):
    krediAdet = 0
    for j in aylikKrediList:
        if j > 0:
            krediAdet += 1
    anaPara -= krediAdet * krediOdeme
    anaPara+=aylikGelir
    toplamKrediBorcu-=krediAdet*krediOdeme #aylık toplam kredi borcumuz
    aylikNetGelir=aylikGelir-(krediAdet*krediOdeme) #aylık net gelirimiz
    krediBorcSure=[]
    for kredi in aylikKrediList:
        krediBorcSure.append(kredi-1)
    aylikKrediList=krediBorcSure
    if anaPara>=pesinat:
        anaPara-=pesinat
        mevcutEv+=1
        aylikKrediList.append(krediAy)
        aylikGelir=aylikGelir+kiraGelir
        toplamKrediBorcu+=(evFiyat-pesinat)
    aktifKredi=0 #aylık net aktif kredi sayımız için ekledik, gider sayısından farklı orada ödeme yapılıyor, burada borç olarak ekleniyor.
    for k in aylikKrediList:
        if k > 0:
            aktifKredi += 1
    yilBelirle=i//12 #anlıkyıl, i anlık ay.
    ayBelirle=i%12
    if ayBelirle==0: #ay ve yıl gösteriminde düzeltmeler
        ayBelirle=12
        yilBelirle-=1
    ayBelirle = "{:02d}".format(ayBelirle)
    mevcutYas = belirtilenYas[0] + yilBelirle
    dateList.append(f"{mevcutYas}.yaş - {ayBelirle}.Ay")
    aylikNetGelirList.append(aylikNetGelir)
    anaParaList.append(anaPara)
    krediborcls.append(toplamKrediBorcu)
    krediAdetList.append(aktifKredi)
    mevcutEvList.append(mevcutEv)
    mevcutAy+=1

mevcutAy-=1
toplamKredi = krediAdet * krediOdeme
mevcutYil = mevcutAy//12
toplamKiraGelir = mevcutEv * kiraGelir
veriler={
    "Yaş / Ay":dateList,
    "Aylık Net gelir":aylikNetGelirList,
    "Ana Para":anaParaList,
    "Mevcut Daire":mevcutEvList,
    "Toplam Kredi Borç":krediborcls,
    "Aktif Kredi Adet":krediAdetList,

    }
df=pd.DataFrame(veriler)
df=df.sort_values("Yaş / Ay")

btn = st.button("Hesaplamak İçin Tıklayınız")
if btn:
    with st.container():
        with st.container(border=True):
            st.caption(f":blue[Belirtmiş olduğunuz bilgiler dahilinde {belirtilenYas[0]} - {belirtilenYas[1]} Yaş aralığı Yatırım Durumu]")
            st.dataframe(df)
    with st.container():
            st.markdown("""
                <style>
                    .custom-container {
                        border: 2px solid #315d85;
                        padding: 20px;
                        border-radius: 10px;
                        color: #315d85;
                    }
                </style>
            """, unsafe_allow_html=True)

            # Container kullanımı
            with st.container():
                st.markdown('<div class="custom-container">'
                            '<p style="text-align:center">- PROJE İSTENİLEN İÇİN ÖZET -</p>'
                            '<small>- 25 - 65 Yaş aralığı baz alınmıştır.</small><br>'
                            '<small>- Aylık Net Gelir Daire alımı ve Kredi Borcu ödemesine göre orantılıdır.</small><br>'
                            '<small>- Aylık Net Gelir düzenli olarak her ay Ana Paraya eklenmektedir.</small><br>'
                            '<small>- Daire satın alımı gerçekleştiyse buna orantılı olarak Mevcut Daire artış göstermektedir.</small><br>'
                            '<small>- Daire satın alımına duyarlı olarak Peşinat ödenerek kalan borç Toplam Kredi Borcuna dahil edilmiştir.</small><br>'
                            '<small>- Daire satın alımına duyarlı olarak Aktif Kredi Adeti artmakta ve biten Kredi Borçları silinmektedir.</small><br>'
                            '</div>', unsafe_allow_html=True)
    # st.caption(f"Sermaye: ***{format(round(anaPara))}₺***")
    # st.caption(f"Aylık gelir: ***{str(round(aylikGelir))}₺***(Kira getirisi: {str(round(aylikGelir-ilkGelir))}₺) - Aylık gider: ***{str(round(toplamKredi))}₺*** = Net gelir: ***{str(round(aylikGelir-toplamKredi))}₺***")
    # st.caption(f"Aktif kredi sayısı: ***{str(krediAdet)}***")
    # st.caption(f"Daire sayısı: ***{str(mevcutEv)}***")

