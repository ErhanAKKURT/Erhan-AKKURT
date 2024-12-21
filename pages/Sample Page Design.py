import requests
import streamlit as st
import xml.etree.ElementTree as et

st.set_page_config(page_title="Kur ve Cripto Verileri", layout="wide")

st.sidebar.title("Menü")
sayfaSecimi = st.sidebar.radio("Sayfa Seçimi Yapınız.",("Ana Sayfa","Cripto Para","Hava Durumu","İletişim"))

#ANA SAYFA
if sayfaSecimi == "Ana Sayfa":

    st.title("ANA SAYFA")
    st.subheader("Hava Durumu ve Cripto Paralar Hakkında Bilgiler.")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit."
             " Curabitur vehicula elit lacinia, feugiat nisi et, porta quam."
             " Nam pharetra felis id scelerisque placerat. In risus dui, pharetra eu nulla in, porta commodo massa."
             " Nunc eget tempus justo, a mollis turpis. Donec hendrerit neque non porttitor dapibus.Lorem ipsum dolor sit amet, consectetur adipiscing elit."
             " Curabitur vehicula elit lacinia, feugiat nisi et, porta quam."
             " Nam pharetra felis id scelerisque placerat. In risus dui, pharetra eu nulla in, porta commodo massa."
             " Nunc eget tempus justo, a mollis turpis. Donec hendrerit neque non porttitor dapibus.")

    col1, col2, col3 = st.columns (3)
    with col2:
        st.subheader("- HAVA DURUMU -")
    st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
        " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
        " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
        " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor.")

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://habereksprescomtr.teimg.com/crop/1280x720/haberekspres-com-tr/uploads/2024/10/hava-durumu-7.jpg", caption="Hava Durumu Görsel")
    #havadurumu
    with col2:
        st.subheader("Hava Durumu Grafik")
        st.bar_chart({"Açık Hava": ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"],
                      "Kapalı Hava": ["Cuma", "Perşembe", "Çarşamba", "Salı", "Pazartesi"],"Yağmurlu Hava": ["Cuma", "Perşembe", "Çarşamba", "Salı", "Pazartesi"]})

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hava Durumu Hakkında Bilgiler")
        with st.expander("Hava Durumu Hakkında Bilgi Almak İçin Tıklayınız."):
            gunSecim = st.selectbox("Hangi Gün İçin Bilgi Almak İstiyorsanız Seçiniz:",
                                ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Hafta Sonu"))
            if gunSecim == "Pazartesi":
                st.write("---")
                st.write(gunSecim)
                st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                         " Curabitur vehicula elit lacinia, feugiat nisi et, porta quam. Nam pharetra felis id scelerisque placerat.")
            elif gunSecim == "Salı":
                st.write("---")
                st.write(gunSecim)
                st.write("In risus dui, pharetra eu nulla in, porta commodo massa."
                         " Nunc eget tempus justo, a mollis turpis. Donec hendrerit neque non porttitor dapibus.")
            elif gunSecim == "Çarşamba":
                st.write("---")
                st.write(gunSecim)
                st.write("Nulla sollicitudin, tellus id lacinia molestie, sapien diam hendrerit quam, eget eleifend ex turpis nec lorem."
                         " Phasellus diam eros, vulputate vel velit a, lacinia feugiat nisi.")
            elif gunSecim == "Perşembe":
                st.write("---")
                st.write(gunSecim)
                st.write("Aenean ultrices mattis purus ut dictum. Etiam tincidunt iaculis sem non suscipit.")
            elif gunSecim == "Cuma":
                st.write("---")
                st.write(gunSecim)
                st.write("Nullam mattis lorem vitae malesuada sagittis. Duis quis massa quam. Quisque imperdiet eros ut eleifend tempus.")
            elif gunSecim == "Hafta Sonu":
                st.write("---")
                st.write(gunSecim)
                st.write("Suspendisse suscipit odio pharetra tellus cursus, eu interdum magna consequat."
                         " Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Duis fermentum dictum auctor."
                         " Phasellus at blandit neque.")

    with col2:
        st.subheader("Bilgilendirme !")
        st.write("Yandaki bölümden belirttiğiniz güne dair hava durumu verilerini görüntüleyebilirsiniz. Veriler saatlik olarak otomatik güncellenmektedir.")
    #criptopara

    col1, col2, col3 = st.columns(3)
    with col2:
        st.subheader("- CRİPTO PARA -")
    st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
        " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
        " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
        " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor.")

    col1, col2 = st.columns(2)
    with  col1:
        st.image(
            "https://www.ekoturk.com/wp-content/uploads/2021/04/kripto-para-piyasasi-2-trilyon-dolara-yukseldi.jpeg",
            caption="Cripto Paralar")

    with col2:
        st.subheader("Cripto Para Grafik")
        st.line_chart({"Cripto1": ["Bitcoin", "Etherium", "Tether", "BNB", "USDC"], "Cripto2": ["USDC", "BNB", "Tether", "Etherium", "Bitcoin"]})

    st.subheader("Cripto Para Hakkında Bilgiler")
    with st.expander("Cripto Para Hakkında Bilgi Almak İçin Tıklayınız."):
        st.write("Cripto Para Nedir ?")
        col1,col2 = st.columns(2)
        with col1:
            st.write(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
                " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
                " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
                " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
                " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue."
                " Quisque id urna vitae nibh maximus consequat. Duis lacinia, elit ut lacinia placerat, tellus quam tincidunt dolor,"
                " sed varius ex ipsum in quam. Suspendisse vehicula magna in sem volutpat, sit amet euismod sapien hendrerit. Vivamus vitae porttitor nulla.")
        with col2:
            st.image("https://www.innova.com.tr/medias/kripto-para-nedir-firsatlari-ve-dezavantajlari-nelerdir.jpg")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
            " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
            " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
            " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
            " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue."
            " Quisque id urna vitae nibh maximus consequat. Duis lacinia, elit ut lacinia placerat, tellus quam tincidunt dolor,"
            " sed varius ex ipsum in quam. Suspendisse vehicula magna in sem volutpat, sit amet euismod sapien hendrerit. Vivamus vitae porttitor nulla.")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
            " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
            " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
            " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
            " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue."
            " Quisque id urna vitae nibh maximus consequat. Duis lacinia, elit ut lacinia placerat, tellus quam tincidunt dolor,"
            " sed varius ex ipsum in quam. Suspendisse vehicula magna in sem volutpat, sit amet euismod sapien hendrerit. Vivamus vitae porttitor nulla.")


#HAVA DURUMU SAYFASI
elif sayfaSecimi == "Hava Durumu":

    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("HAVA DURUMU")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
            " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
            " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
            " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
            " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue.")

    hava = requests.get("https://www.mgm.gov.tr/FTPDATA/analiz/SonDurumlarTumu.xml")
    havalar = hava.content
    root = et.fromstring(havalar)
    HavaDurumuil = {}
    HavaDurumuilce = {}
    col1, col2 = st.columns(2)
    with col1:
        sehir = st.text_input("Şehir Adı Giriniz: ", "İstanbul")
        btn = st.button("Hava Durumunu Getir")
        if btn == True:
            servis = f"https://api.weatherapi.com/v1/current.json?key=ab2bbf96d105451e8b991408242610&q={sehir}&aqi=no"
            response = requests.get(servis)
            veri = response.json()
            veri = veri.get('current')

            temp = veri.get('temp_c')
            durum = veri.get('condition').get('text')
            gorsel = veri.get('condition').get('icon')

            with st.expander("Sonuç"):
                st.header(str(durum))
                st.header(str(temp))
                st.image("https:" + gorsel)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hava Durumu Görsel")
        st.image(
            "https://habereksprescomtr.teimg.com/crop/1280x720/haberekspres-com-tr/uploads/2024/10/hava-durumu-7.jpg",
            caption="Hava Durumu Görsel")

    with col2:
        st.subheader("Hava Durumu Grafik")
        st.bar_chart({"Kapalı Hava": ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"],
                      "Açık Hava": ["Cuma", "Perşembe", "Çarşamba", "Salı", "Pazartesi"]})

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hava Durumu Hakkında Bilgiler")
        with st.expander("Hava Durumu Hakkında Bilgi Almak İçin Tıklayınız."):
            gunSecim = st.selectbox("Hangi Gün İçin Bilgi Almak İstiyorsanız Seçiniz:",
                                    ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Hafta Sonu"))
            if gunSecim == "Pazartesi":
                st.write("---")
                st.write(gunSecim)
                st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                         " Curabitur vehicula elit lacinia, feugiat nisi et, porta quam. Nam pharetra felis id scelerisque placerat.")
            elif gunSecim == "Salı":
                st.write("---")
                st.write(gunSecim)
                st.write("In risus dui, pharetra eu nulla in, porta commodo massa."
                         " Nunc eget tempus justo, a mollis turpis. Donec hendrerit neque non porttitor dapibus.")
            elif gunSecim == "Çarşamba":
                st.write("---")
                st.write(gunSecim)
                st.write(
                    "Nulla sollicitudin, tellus id lacinia molestie, sapien diam hendrerit quam, eget eleifend ex turpis nec lorem."
                    " Phasellus diam eros, vulputate vel velit a, lacinia feugiat nisi.")
            elif gunSecim == "Perşembe":
                st.write("---")
                st.write(gunSecim)
                st.write("Aenean ultrices mattis purus ut dictum. Etiam tincidunt iaculis sem non suscipit.")
            elif gunSecim == "Cuma":
                st.write("---")
                st.write(gunSecim)
                st.write(
                    "Nullam mattis lorem vitae malesuada sagittis. Duis quis massa quam. Quisque imperdiet eros ut eleifend tempus.")
            elif gunSecim == "Hafta Sonu":
                st.write("---")
                st.write(gunSecim)
                st.write("Suspendisse suscipit odio pharetra tellus cursus, eu interdum magna consequat."
                         " Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Duis fermentum dictum auctor."
                         " Phasellus at blandit neque.")

    with col2:
        st.subheader("Bilgilendirme !")
        st.write("Yandaki bölümden belirttiğiniz güne dair hava durumu verilerini görüntüleyebilirsiniz. Veriler saatlik olarak otomatik güncellenmektedir.")


#CRİPTO PARA SAYFASI
elif sayfaSecimi == "Cripto Para":

    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("CRİPTO PARA")

    st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
        " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
        " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
        " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
        " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue.")

    col1, col2 = st.columns(2)
    with  col1:
        st.subheader("Cripto Paralar Görsel")
        st.image(
            "https://www.ekoturk.com/wp-content/uploads/2021/04/kripto-para-piyasasi-2-trilyon-dolara-yukseldi.jpeg",
            caption="Cripto Paralar")

    with col2:
        st.subheader("Cripto Para Grafik")
        st.line_chart({"Cripto1": ["Bitcoin", "Etherium", "Tether", "BNB", "USDC"],
                      "Cripto2": ["USDC", "BNB", "Tether", "Etherium", "Bitcoin"]})

    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Cripto Para Hakkında Bilgiler")
        with st.expander("Cripto Para Hakkında Bilgi Almak İçin Tıklayınız."):
            st.write("Cripto Para Nedir ?")
            col3, col4 = st.columns(2)
            with col3:
                st.write(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
                    " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
                    " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
                    " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
                    " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue."
                    " Quisque id urna vitae nibh maximus consequat. Duis lacinia, elit ut lacinia placerat, tellus quam tincidunt dolor,"
                    " sed varius ex ipsum in quam. Suspendisse vehicula magna in sem volutpat, sit amet euismod sapien hendrerit. Vivamus vitae porttitor nulla.")
            with col4:
                st.image("https://www.innova.com.tr/medias/kripto-para-nedir-firsatlari-ve-dezavantajlari-nelerdir.jpg")
                st.image("https://www.cybermagonline.com/img/sayfa/1523883141-gorsel-1.jpg")
                st.image("https://geoim.bloomberght.com/2021/01/04/ver1609767461/2271922_620x349.jpg")
                st.image("https://www.coinkolik.com/wp-content/uploads/2018/09/Kripto-Para-Nedir-Kripto-Paralar.jpg")
            st.write(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
                " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
                " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
                " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
                " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue."
                " Quisque id urna vitae nibh maximus consequat. Duis lacinia, elit ut lacinia placerat, tellus quam tincidunt dolor,"
                " sed varius ex ipsum in quam. Suspendisse vehicula magna in sem volutpat, sit amet euismod sapien hendrerit. Vivamus vitae porttitor nulla.")

    with col2:
        st.subheader("Güncel Kur ve Cripto Verileri")
        # Kur Xml Dosyası Verileri
        r = requests.get("https://tcmb.gov.tr/kurlar/today.xml")
        veri = r.content
        root = et.fromstring(veri)

        # Coin API URL'si
        url = "https://api.coinlore.net/api/tickers/"
        # API'den veri çekme
        response = requests.get(url)
        data = response.json()  # JSON verisini al
        coins = data['data']  # 'data' kısmını al

        coinAndKur = {}
        for coin in root.findall('Currency'):
            isim = coin.find('Isim').text
            fiyat = coin.find('ForexBuying').text
            coinAndKur[isim] = (fiyat)

        for x in coins:
            coinAndKur.update({x.get('name'): float(x.get('price_usd'))})

        secim = st.selectbox("Kur veya Cripto Seçimi Yapınız:", (coinAndKur))
        if secim:
            for don in coinAndKur:
                donsec = coinAndKur.get(don)
                if don == secim:
                    st.write(f"1 {secim}: {donsec}")


#İLETİŞİM SAYFASI
elif sayfaSecimi == "İletişim":

    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("İLETİŞİM")
    st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
        " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
        " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
        " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
        " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue.")
    st.write("Bizimle İletişime Geçebilirsiniz.")

    #Form Tasarımı
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Adınız: ")
        with col2:
            st.text_input("E-Posta Adresiniz: ")
        st.text_area("Mesajınız: ")
        st.form_submit_button("Gönder: ")

#FOOTER

st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("Hakkımızda")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pulvinar odio turpis, id rhoncus orci tincidunt eget."
             " Aenean eu convallis nibh. Ut sed malesuada diam.")
with col2:
    st.subheader("Sosyal Medya")
    st.write("www.facebook.com")
    st.write("www.instagram.com")
    st.write("www.whatsapp.com")
with col3:
    st.subheader("İletişim")
    st.write("Tel : 0555 555 55 55")
    st.write("E-Posta : .......@gmail.com")
    st.write("Adres : Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pulvinar odio turpis,")
with col4:
    st.subheader("Konum")
    st.write("Lorem ipsum dolor sit amet MAH. consectetur adipiscing elit CAD. NO:845794545945875")
st.write("---")
st.write("© 2024 Tüm Hakları Saklıdır...")

kod='''
import requests
import streamlit as st
import xml.etree.ElementTree as et

st.set_page_config(page_title="Kur ve Cripto Verileri", layout="wide")

st.sidebar.title("Menü")
sayfaSecimi = st.sidebar.radio("Sayfa Seçimi Yapınız.",("Ana Sayfa","Cripto Para","Hava Durumu","İletişim"))

#ANA SAYFA
if sayfaSecimi == "Ana Sayfa":

    st.title("ANA SAYFA")
    st.subheader("Hava Durumu ve Cripto Paralar Hakkında Bilgiler.")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit."
             " Curabitur vehicula elit lacinia, feugiat nisi et, porta quam."
             " Nam pharetra felis id scelerisque placerat. In risus dui, pharetra eu nulla in, porta commodo massa."
             " Nunc eget tempus justo, a mollis turpis. Donec hendrerit neque non porttitor dapibus.Lorem ipsum dolor sit amet, consectetur adipiscing elit."
             " Curabitur vehicula elit lacinia, feugiat nisi et, porta quam."
             " Nam pharetra felis id scelerisque placerat. In risus dui, pharetra eu nulla in, porta commodo massa."
             " Nunc eget tempus justo, a mollis turpis. Donec hendrerit neque non porttitor dapibus.")

    col1, col2, col3 = st.columns (3)
    with col2:
        st.subheader("- HAVA DURUMU -")
    st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
        " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
        " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
        " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor.")

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://habereksprescomtr.teimg.com/crop/1280x720/haberekspres-com-tr/uploads/2024/10/hava-durumu-7.jpg", caption="Hava Durumu Görsel")
    #havadurumu
    with col2:
        st.subheader("Hava Durumu Grafik")
        st.bar_chart({"Açık Hava": ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"],
                      "Kapalı Hava": ["Cuma", "Perşembe", "Çarşamba", "Salı", "Pazartesi"],"Yağmurlu Hava": ["Cuma", "Perşembe", "Çarşamba", "Salı", "Pazartesi"]})

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hava Durumu Hakkında Bilgiler")
        with st.expander("Hava Durumu Hakkında Bilgi Almak İçin Tıklayınız."):
            gunSecim = st.selectbox("Hangi Gün İçin Bilgi Almak İstiyorsanız Seçiniz:",
                                ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Hafta Sonu"))
            if gunSecim == "Pazartesi":
                st.write("---")
                st.write(gunSecim)
                st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                         " Curabitur vehicula elit lacinia, feugiat nisi et, porta quam. Nam pharetra felis id scelerisque placerat.")
            elif gunSecim == "Salı":
                st.write("---")
                st.write(gunSecim)
                st.write("In risus dui, pharetra eu nulla in, porta commodo massa."
                         " Nunc eget tempus justo, a mollis turpis. Donec hendrerit neque non porttitor dapibus.")
            elif gunSecim == "Çarşamba":
                st.write("---")
                st.write(gunSecim)
                st.write("Nulla sollicitudin, tellus id lacinia molestie, sapien diam hendrerit quam, eget eleifend ex turpis nec lorem."
                         " Phasellus diam eros, vulputate vel velit a, lacinia feugiat nisi.")
            elif gunSecim == "Perşembe":
                st.write("---")
                st.write(gunSecim)
                st.write("Aenean ultrices mattis purus ut dictum. Etiam tincidunt iaculis sem non suscipit.")
            elif gunSecim == "Cuma":
                st.write("---")
                st.write(gunSecim)
                st.write("Nullam mattis lorem vitae malesuada sagittis. Duis quis massa quam. Quisque imperdiet eros ut eleifend tempus.")
            elif gunSecim == "Hafta Sonu":
                st.write("---")
                st.write(gunSecim)
                st.write("Suspendisse suscipit odio pharetra tellus cursus, eu interdum magna consequat."
                         " Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Duis fermentum dictum auctor."
                         " Phasellus at blandit neque.")

    with col2:
        st.subheader("Bilgilendirme !")
        st.write("Yandaki bölümden belirttiğiniz güne dair hava durumu verilerini görüntüleyebilirsiniz. Veriler saatlik olarak otomatik güncellenmektedir.")
    #criptopara

    col1, col2, col3 = st.columns(3)
    with col2:
        st.subheader("- CRİPTO PARA -")
    st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
        " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
        " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
        " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor.")

    col1, col2 = st.columns(2)
    with  col1:
        st.image(
            "https://www.ekoturk.com/wp-content/uploads/2021/04/kripto-para-piyasasi-2-trilyon-dolara-yukseldi.jpeg",
            caption="Cripto Paralar")

    with col2:
        st.subheader("Cripto Para Grafik")
        st.line_chart({"Cripto1": ["Bitcoin", "Etherium", "Tether", "BNB", "USDC"], "Cripto2": ["USDC", "BNB", "Tether", "Etherium", "Bitcoin"]})

    st.subheader("Cripto Para Hakkında Bilgiler")
    with st.expander("Cripto Para Hakkında Bilgi Almak İçin Tıklayınız."):
        st.write("Cripto Para Nedir ?")
        col1,col2 = st.columns(2)
        with col1:
            st.write(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
                " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
                " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
                " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
                " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue."
                " Quisque id urna vitae nibh maximus consequat. Duis lacinia, elit ut lacinia placerat, tellus quam tincidunt dolor,"
                " sed varius ex ipsum in quam. Suspendisse vehicula magna in sem volutpat, sit amet euismod sapien hendrerit. Vivamus vitae porttitor nulla.")
        with col2:
            st.image("https://www.innova.com.tr/medias/kripto-para-nedir-firsatlari-ve-dezavantajlari-nelerdir.jpg")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
            " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
            " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
            " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
            " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue."
            " Quisque id urna vitae nibh maximus consequat. Duis lacinia, elit ut lacinia placerat, tellus quam tincidunt dolor,"
            " sed varius ex ipsum in quam. Suspendisse vehicula magna in sem volutpat, sit amet euismod sapien hendrerit. Vivamus vitae porttitor nulla.")
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
            " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
            " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
            " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
            " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue."
            " Quisque id urna vitae nibh maximus consequat. Duis lacinia, elit ut lacinia placerat, tellus quam tincidunt dolor,"
            " sed varius ex ipsum in quam. Suspendisse vehicula magna in sem volutpat, sit amet euismod sapien hendrerit. Vivamus vitae porttitor nulla.")


#HAVA DURUMU SAYFASI
elif sayfaSecimi == "Hava Durumu":

    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("HAVA DURUMU")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
            " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
            " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
            " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
            " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue.")

    hava = requests.get("https://www.mgm.gov.tr/FTPDATA/analiz/SonDurumlarTumu.xml")
    havalar = hava.content
    root = et.fromstring(havalar)
    HavaDurumuil = {}
    HavaDurumuilce = {}
    col1, col2 = st.columns(2)
    with col1:
        sehir = st.text_input("Şehir Adı Giriniz: ", "İstanbul")
        btn = st.button("Hava Durumunu Getir")
        if btn == True:
            servis = f"https://api.weatherapi.com/v1/current.json?key=ab2bbf96d105451e8b991408242610&q={sehir}&aqi=no"
            response = requests.get(servis)
            veri = response.json()
            veri = veri.get('current')

            temp = veri.get('temp_c')
            durum = veri.get('condition').get('text')
            gorsel = veri.get('condition').get('icon')

            with st.expander("Sonuç"):
                st.header(str(durum))
                st.header(str(temp))
                st.image("https:" + gorsel)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hava Durumu Görsel")
        st.image(
            "https://habereksprescomtr.teimg.com/crop/1280x720/haberekspres-com-tr/uploads/2024/10/hava-durumu-7.jpg",
            caption="Hava Durumu Görsel")

    with col2:
        st.subheader("Hava Durumu Grafik")
        st.bar_chart({"Kapalı Hava": ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"],
                      "Açık Hava": ["Cuma", "Perşembe", "Çarşamba", "Salı", "Pazartesi"]})

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Hava Durumu Hakkında Bilgiler")
        with st.expander("Hava Durumu Hakkında Bilgi Almak İçin Tıklayınız."):
            gunSecim = st.selectbox("Hangi Gün İçin Bilgi Almak İstiyorsanız Seçiniz:",
                                    ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Hafta Sonu"))
            if gunSecim == "Pazartesi":
                st.write("---")
                st.write(gunSecim)
                st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                         " Curabitur vehicula elit lacinia, feugiat nisi et, porta quam. Nam pharetra felis id scelerisque placerat.")
            elif gunSecim == "Salı":
                st.write("---")
                st.write(gunSecim)
                st.write("In risus dui, pharetra eu nulla in, porta commodo massa."
                         " Nunc eget tempus justo, a mollis turpis. Donec hendrerit neque non porttitor dapibus.")
            elif gunSecim == "Çarşamba":
                st.write("---")
                st.write(gunSecim)
                st.write(
                    "Nulla sollicitudin, tellus id lacinia molestie, sapien diam hendrerit quam, eget eleifend ex turpis nec lorem."
                    " Phasellus diam eros, vulputate vel velit a, lacinia feugiat nisi.")
            elif gunSecim == "Perşembe":
                st.write("---")
                st.write(gunSecim)
                st.write("Aenean ultrices mattis purus ut dictum. Etiam tincidunt iaculis sem non suscipit.")
            elif gunSecim == "Cuma":
                st.write("---")
                st.write(gunSecim)
                st.write(
                    "Nullam mattis lorem vitae malesuada sagittis. Duis quis massa quam. Quisque imperdiet eros ut eleifend tempus.")
            elif gunSecim == "Hafta Sonu":
                st.write("---")
                st.write(gunSecim)
                st.write("Suspendisse suscipit odio pharetra tellus cursus, eu interdum magna consequat."
                         " Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Duis fermentum dictum auctor."
                         " Phasellus at blandit neque.")

    with col2:
        st.subheader("Bilgilendirme !")
        st.write("Yandaki bölümden belirttiğiniz güne dair hava durumu verilerini görüntüleyebilirsiniz. Veriler saatlik olarak otomatik güncellenmektedir.")


#CRİPTO PARA SAYFASI
elif sayfaSecimi == "Cripto Para":

    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("CRİPTO PARA")

    st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
        " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
        " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
        " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
        " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue.")

    col1, col2 = st.columns(2)
    with  col1:
        st.subheader("Cripto Paralar Görsel")
        st.image(
            "https://www.ekoturk.com/wp-content/uploads/2021/04/kripto-para-piyasasi-2-trilyon-dolara-yukseldi.jpeg",
            caption="Cripto Paralar")

    with col2:
        st.subheader("Cripto Para Grafik")
        st.line_chart({"Cripto1": ["Bitcoin", "Etherium", "Tether", "BNB", "USDC"],
                      "Cripto2": ["USDC", "BNB", "Tether", "Etherium", "Bitcoin"]})

    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Cripto Para Hakkında Bilgiler")
        with st.expander("Cripto Para Hakkında Bilgi Almak İçin Tıklayınız."):
            st.write("Cripto Para Nedir ?")
            col3, col4 = st.columns(2)
            with col3:
                st.write(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
                    " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
                    " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
                    " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
                    " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue."
                    " Quisque id urna vitae nibh maximus consequat. Duis lacinia, elit ut lacinia placerat, tellus quam tincidunt dolor,"
                    " sed varius ex ipsum in quam. Suspendisse vehicula magna in sem volutpat, sit amet euismod sapien hendrerit. Vivamus vitae porttitor nulla.")
            with col4:
                st.image("https://www.innova.com.tr/medias/kripto-para-nedir-firsatlari-ve-dezavantajlari-nelerdir.jpg")
                st.image("https://www.cybermagonline.com/img/sayfa/1523883141-gorsel-1.jpg")
                st.image("https://geoim.bloomberght.com/2021/01/04/ver1609767461/2271922_620x349.jpg")
                st.image("https://www.coinkolik.com/wp-content/uploads/2018/09/Kripto-Para-Nedir-Kripto-Paralar.jpg")
            st.write(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
                " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
                " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
                " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
                " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue."
                " Quisque id urna vitae nibh maximus consequat. Duis lacinia, elit ut lacinia placerat, tellus quam tincidunt dolor,"
                " sed varius ex ipsum in quam. Suspendisse vehicula magna in sem volutpat, sit amet euismod sapien hendrerit. Vivamus vitae porttitor nulla.")

    with col2:
        st.subheader("Güncel Kur ve Cripto Verileri")
        # Kur Xml Dosyası Verileri
        r = requests.get("https://tcmb.gov.tr/kurlar/today.xml")
        veri = r.content
        root = et.fromstring(veri)

        # Coin API URL'si
        url = "https://api.coinlore.net/api/tickers/"
        # API'den veri çekme
        response = requests.get(url)
        data = response.json()  # JSON verisini al
        coins = data['data']  # 'data' kısmını al

        coinAndKur = {}
        for coin in root.findall('Currency'):
            isim = coin.find('Isim').text
            fiyat = coin.find('ForexBuying').text
            coinAndKur[isim] = (fiyat)

        for x in coins:
            coinAndKur.update({x.get('name'): float(x.get('price_usd'))})

        secim = st.selectbox("Kur veya Cripto Seçimi Yapınız:", (coinAndKur))
        if secim:
            for don in coinAndKur:
                donsec = coinAndKur.get(don)
                if don == secim:
                    st.write(f"1 {secim}: {donsec}")


#İLETİŞİM SAYFASI
elif sayfaSecimi == "İletişim":

    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("İLETİŞİM")
    st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tincidunt odio in consequat consectetur."
        " Vestibulum cursus et nunc ut eleifend. Donec ac facilisis urna, in bibendum dolor. Nulla cursus metus quis interdum sollicitudin."
        " Suspendisse id pretium ligula. Aliquam quis scelerisque nibh, eu placerat tellus."
        " Sed pretium nibh ut pellentesque condimentum. Donec tristique felis fermentum sapien sagittis auctor."
        " Curabitur sed semper augue. Nam quis turpis quis lorem gravida ultrices eu vel augue.")
    st.write("Bizimle İletişime Geçebilirsiniz.")

    #Form Tasarımı
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Adınız: ")
        with col2:
            st.text_input("E-Posta Adresiniz: ")
        st.text_area("Mesajınız: ")
        st.form_submit_button("Gönder: ")

#FOOTER

st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("Hakkımızda")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pulvinar odio turpis, id rhoncus orci tincidunt eget."
             " Aenean eu convallis nibh. Ut sed malesuada diam.")
with col2:
    st.subheader("Sosyal Medya")
    st.write("www.facebook.com")
    st.write("www.instagram.com")
    st.write("www.whatsapp.com")
with col3:
    st.subheader("İletişim")
    st.write("Tel : 0555 555 55 55")
    st.write("E-Posta : .......@gmail.com")
    st.write("Adres : Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pulvinar odio turpis,")
with col4:
    st.subheader("Konum")
    st.write("Lorem ipsum dolor sit amet MAH. consectetur adipiscing elit CAD. NO:845794545945875")
st.write("---")
st.write("© 2024 Tüm Hakları Saklıdır...")
'''

st.header('Kaynak Kodları')
st.code(kod,language='python')
