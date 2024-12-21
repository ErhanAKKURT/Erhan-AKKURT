import streamlit as st
import sqlite3
import pandas as pd

def create_connection():
    conn=sqlite3.connect("Library.db")
    return conn

#OGRENCI TABLO
def add_ogrenci(ograd,ogrsoyad,cinsiyet,dtarih,sinif,puan):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO Ogrenci(ograd,ogrsoyad,cinsiyet,dtarih,sinif,puan) VALUES (?,?,?,?,?,?)",(ograd,ogrsoyad,cinsiyet,dtarih,sinif,puan))
    conn.commit()
    conn.close()

def get_ogrenci():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM Ogrenci")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_ogrenci(ogrenci_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM Ogrenci WHERE ogrno=?",(ogrenci_id,))
    conn.commit()
    conn.close()

def update_ogrenci(ogrenci_id):
    conn=create_connection()
    c=conn.cursor()
    ogrsec = st.selectbox("Güncellemek İstediğiniz Veriyi Seçiniz!", ('ograd', 'ogrsoyad', 'cinsiyet', 'dtarih','sinif','puan'),key=f"selectbox{ogrenci_id}")
    ogrguncel=st.text_input("Veriyi Giriniz: ", key=f"textbox{ogrenci_id}")

    if st.button("Güncelle", key=f"update{ogrenci_id}"):
        if ogrguncel:
            c.execute(f"UPDATE Ogrenci SET {ogrsec}='{ogrguncel}' WHERE ogrno=?", (ogrenci_id,))
            conn.commit()
            st.success("Güncelleme İşlemi Tamamlanmıştır.")
        else:
            st.error("Güncelleme İşlemi Hatalı !")

    conn.commit()
    conn.close()

#---------------------------------------------------------------------------------------------------------------------
# TUR TABLO
def add_tur(turadi):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO Tur(turadi) VALUES (?)",(turadi,))
    conn.commit()
    conn.close()

def get_tur():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM Tur")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_tur(tur_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM Tur WHERE turno=?",(tur_id,))
    conn.commit()
    conn.close()

def update_tur(tur_id):
    conn=create_connection()
    c=conn.cursor()
    turguncel=st.text_input("Güncel Veriyi Giriniz: ", key=f"ttextbox{tur_id}")

    if st.button("Güncelle", key=f"tupdate{tur_id}"):
        if turguncel:
            c.execute(f"UPDATE Tur SET turadi='{turguncel}' WHERE turno=?", (tur_id,))
            conn.commit()
            st.success("Güncelleme İşlemi Tamamlanmıştır.")
        else:
            st.error("Güncelleme İşlemi Hatalı !")

    conn.commit()
    conn.close()

#---------------------------------------------------------------------------------------------------------------------
#YAZAR TABLOSU
def add_yazar(yazarad,yazarsoyad):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO Yazar(yazarad,yazarsoyad) VALUES(?,?)",(yazarad,yazarsoyad))
    conn.commit()
    conn.close()

def get_yazar():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM Yazar")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_yazar(yazar_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM Yazar WHERE yazarno=?",(yazar_id,))
    conn.commit()
    conn.close()

def update_yazar(yazar_id):
    conn=create_connection()
    c=conn.cursor()
    yazarsec = st.selectbox("Güncellemek İstediğiniz Veriyi Seçiniz!", ('yazarad','yazarsoyad'),key=f"yselectbox{yazar_id}")
    yazarguncel=st.text_input("Veriyi Giriniz: ", key=f"ytextbox{yazar_id}")

    if st.button("Güncelle", key=f"yupdate{yazar_id}"):
        if yazarguncel:
            c.execute(f"UPDATE Yazar SET {yazarsec}='{yazarguncel}' WHERE yazarno=?", (yazar_id,))
            conn.commit()
            st.success("Güncelleme İşlemi Tamamlanmıştır.")
        else:
            st.error("Güncelleme İşlemi Hatalı !")

    conn.commit()
    conn.close()

#---------------------------------------------------------------------------------------------------------------------
#KİTAP TABLOSU
def add_kitap(isbnno,kitapadi,yazarno,turno,sayfasayisi,puan):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO Kitap(isbnno,kitapadi,yazarno,turno,sayfasayisi,puan) VALUES(?,?,?,?,?,?)",(isbnno,kitapadi,yazarno,turno,sayfasayisi,puan))
    conn.commit()
    conn.close()

def get_kitap():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT kitapno,isbnno,kitapadi,yazarad,yazarsoyad,turadi,sayfasayisi,puan FROM Kitap k JOIN Yazar y ON k.yazarno=y.yazarno JOIN tur t ON k.turno=t.turno")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_kitap(kitap_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM Kitap WHERE kitapno=?",(kitap_id,))
    conn.commit()
    conn.close()

def update_kitap(kitap_id):
    conn=create_connection()
    c=conn.cursor()
    kitapsec = st.selectbox("Güncellemek İstediğiniz Veriyi Seçiniz!", ('isbnno','kitapadi','sayfasayisi','puan','yazarno','turno'),key=f"kselectbox{kitap_id}")
    kitapguncel=st.text_input("Veriyi Giriniz: ", key=f"ktextbox{kitap_id}")

    if st.button("Güncelle", key=f"kupdate{kitap_id}"):
        if kitapguncel:
            c.execute(f"UPDATE Kitap SET {kitapsec}='{kitapguncel}' WHERE kitapno=?", (kitap_id,))
            conn.commit()
            st.success("Güncelleme İşlemi Tamamlanmıştır.")
        else:
            st.error("Güncelleme İşlemi Hatalı !")

    conn.commit()
    conn.close()

#---------------------------------------------------------------------------------------------------------------------
#ISLEM TABLOSU
def add_islem(ogrno,kitapno,atarih,vtarih):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO Islem(ogrno,kitapno,atarih,vtarih) VALUES(?,?,?,?)",(ogrno,kitapno,atarih,vtarih))
    conn.commit()
    conn.close()

def get_islem():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT islemno,ograd,ogrsoyad,kitapadi,atarih,vtarih FROM Islem i JOIN Ogrenci o ON i.ogrno=o.ogrno JOIN Kitap k ON i.kitapno=k.kitapno")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_islem(islem_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM Islem WHERE islemno=?",(islem_id,))
    conn.commit()
    conn.close()

def update_islem(islem_id):
    conn=create_connection()
    c=conn.cursor()
    islemsec = st.selectbox("Güncellemek İstediğiniz Veriyi Seçiniz!", ('ogrno','kitapno','atarih','vtarih'),key=f"iselectbox{islem_id}")
    islemguncel=st.text_input("Veriyi Giriniz: ", key=f"itextbox{islem_id}")

    if st.button("Güncelle", key=f"iupdate{islem_id}"):
        if islemguncel:
            c.execute(f"UPDATE Islem SET {islemsec}='{islemguncel}' WHERE islemno=?", (islem_id,))
            conn.commit()
            st.success("Güncelleme İşlemi Tamamlanmıştır.")
        else:
            st.error("Güncelleme İşlemi Hatalı !")

    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

# SAYFA TASARIMI

# OGRENCI TABLOSU
st.title("Kütüphane Uygulaması")
st.header("Öğrenci Bilgileri")
st.write("---")

col1, col2 = st.columns(2)
with col1:
    ograd=st.text_input("Öğrenci Ad: ")
with col2:
    ogrsoyad=st.text_input("Öğrenci Soyad: ")
with col1:
    cinsiyet=st.text_input("Öğrenci Cinsiyet:" )
with col2:
    dtarih=st.date_input("Tarih: ")
with col1:
    sinif=st.text_input("Öğrenci Sınıf: ")
with col2:
    puan=st.text_input("Öğrenci Puan: ")

if st.button("Öğrenci Ekle"):
    if ograd and ogrsoyad and cinsiyet and dtarih and sinif and puan:
        add_ogrenci(ograd,ogrsoyad,cinsiyet,dtarih.isoformat(),sinif,puan)
        st.success(f"{ograd} {ogrsoyad} başarı ile eklendi")
    else:
        st.error("Başlık alanı gereklidir !")

st.header("Öğrenci Tablosu")
st.write("---")
con = get_ogrenci()
if con:
    for ogr in con:
        ogr_id,ogr_ad,ogr_soyad,ogr_cns,ogr_tarih,ogr_sinif,ogr_puan=ogr
        st.write(f"Kayıt: {ogr_id} | Ad: {ogr_ad} | Soyad: {ogr_soyad} | Sınıf: {ogr_sinif} | Cinsiyet: {ogr_cns} | Tarih: {ogr_tarih} | Puan: {ogr_puan}")

        col1,col2 = st.columns(2)
        with col1:
            onay = st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?", key=f"onay{ogr_id}")
            if onay:
                update_ogrenci(ogr_id)
        with col2:
            if st.button(f"Sil",key=f"delete{ogr_id}"):
                delete_ogrenci(ogr[0])
                st.success(f"{ogr_ad} {ogr_soyad} Başarı ile Silindi !")
else:
    st.write("Eklenmiş Öğrenci Kaydı Yoktur !")

st.header("Öğrenci Tablo Verileri")
df = pd.DataFrame(con)
df.columns=['ID','ÖĞRENCİ AD','ÖĞRENCİ SOYAD','CİNSİYET','TARİH','SINIF','PUAN']
st.write(df)

#---------------------------------------------------------------------------------------------------------------------
# TUR TASARIMI
st.header("Kitap Türü Bilgileri")
st.write("---")

turadi=st.text_input("Kitap Türü Giriniz: ")

if st.button("Tür Ekle"):
    if turadi:
        add_tur(turadi)
        st.success(f"{turadi} Türü Eklendi.")

st.header("Kitap Türleri")
tcon = get_tur()
if tcon:
    for tur in tcon:
        tur_id,tur_ad=tur
        st.write(f"Kayıt: {tur_id} | Kitap Türü: {tur_ad}")

        col1,col2 = st.columns(2)
        with col1:
            onay = st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?", key=f"tonay{tur_id}")
            if onay:
                update_tur(tur_id)
        with col2:
            if st.button(f"Sil",key=f"tdelete{tur_id}"):
                delete_tur(tur[0])
                st.success(f"{tur_ad} Başarı ile Silindi !")
else:
    st.write("Eklenmiş Öğrenci Kaydı Yoktur !")

st.header("Kitap Türü Tablo Verileri")
df = pd.DataFrame(tcon)
df.columns=['ID','KİTAP TÜRÜ']
st.write(df)

#---------------------------------------------------------------------------------------------------------------------
#YAZAR TASARIMI
st.header("Yazar Bilgileri")
st.write("---")
col1, col2 = st.columns(2)
with col1:
    yazarad=st.text_input("Yazar Adı: ")
with col2:
    yazarsoyad=st.text_input("Yazar Soyadı: ")

if st.button("Yazar Ekle"):
    if yazarad and yazarsoyad:
        add_yazar(yazarad,yazarsoyad)
        st.success(f"{yazarad} {yazarsoyad} Başarı ile Eklendi.")

col1,col2 = st.columns(2)
st.header("Yazar Tablosu")
st.write("---")
ycon = get_yazar()
if ycon:
    for yaz in ycon:
        yazar_id,yazar_ad,yazar_soyad=yaz
        st.write(f"Kayıt: {yazar_id} | Yazar Ad: {yazar_ad} | Yazar Soyad: {yazar_soyad}")
        col1,col2 = st.columns(2)
        with col1:
            onay = st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?", key=f"yonay{yazar_id}")
            if onay:
                update_yazar(yazar_id)
        with col2:
            if st.button(f"Sil",key=f"ydelete{yazar_id}"):
                delete_yazar(yaz[0])
                st.success(f"{yazar_ad} {yazar_soyad} Başarı ile Silindi !")
else:
    st.write("Eklenmiş Kitap Türü Kaydı Yoktur !")

st.header("Yazar Tablo Verileri")
df = pd.DataFrame(ycon)
df.columns=['ID','YAZAR AD','YAZAR SOYAD']
st.write(df)

#---------------------------------------------------------------------------------------------------------------------
#KİTAP TASARIMI
st.header("Kitap Bilgileri")
st.write("---")
col1, col2 = st.columns(2)
with col1:
    isbnno=st.text_input("ISBN No: ")
with col2:
    kitapadi=st.text_input("Kitap Adı: ")
with col1:
    sayfasayisi=st.text_input("Sayfa Sayısı: ")
with col2:
    kpuan=st.text_input("Puan: ")
with col1:
    yazarlar = get_yazar()  # Yazarları alıyoruz
    yazar_options = {f"{yazar[1]} {yazar[2]}": yazar[0] for yazar in yazarlar}  # Yazar adı soyad ve id
    yazarsec = st.selectbox("Kitap için Yazar Seçin:", options=list(yazar_options.keys()))
    if yazarsec:
        yazarno = yazar_options[yazarsec]
with col2:
    turler = get_tur()  # Kitap türlerini alıyoruz
    tur_options = {f"{tur[1]}": tur[0] for tur in turler}
    tursec = st.selectbox("Kitap için Tür Seçin:", options=list(tur_options.keys()))
    if tursec:
        turno = tur_options[tursec]

if st.button("Kitap Ekle"):
    if kitapadi and isbnno and sayfasayisi and kpuan:
        add_kitap(isbnno,kitapadi,yazarno,turno,sayfasayisi,kpuan)
        st.success(f"{kitapadi} Başarı ile Eklendi.")

st.header("Kitap Tablosu")
st.write("---")
kcon = get_kitap()
if kcon:
    for kit in kcon:
        k_id,k_isbn,k_ad,k_yad,k_ysoyad,k_tur,k_sayfa,k_puan=kit
        st.write(f"Kayıt: {k_id} | Kitap: {k_ad} | Yazar: {k_yad} {k_ysoyad} | ISBN No: {k_isbn} | Tür: {k_tur} | Sayfa: {k_sayfa} Puan: {k_puan}")
        col1,col2 = st.columns(2)
        with col1:
            onay = st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?", key=f"konay_{k_id}_{k_isbn}")
            if onay:
                update_kitap(k_id)
        with col2:
            if st.button(f"Sil",key=f"idelete{k_id}"):
                delete_kitap(kit[0])
                st.success(f"{k_id} Kaydı Başarı ile Silindi !")
else:
    st.write("Eklenmiş Kitap Türü Kaydı Yoktur !")

st.header("Kitap Tablo Verileri")
df = pd.DataFrame(kcon)
df.columns=['ID','ISBN NO','KİTAP','YAZAR AD','YAZAR SOYAD','KİTAP TÜRÜ','SAYFA SAYISI','PUAN']
st.write(df)

# ---------------------------------------------------------------------------------------------------------------------
# ISLEM TASARIMI
st.header("İşlem Bilgileri")
st.write("---")
col1, col2 = st.columns(2)
with col1:
    islemler = get_ogrenci()
    islem_options = {f"{islem[1]} {islem[2]}": islem[0] for islem in islemler}
    islemsec = st.selectbox("İşlem için Öğrenci Seçin:", options=list(islem_options.keys()))
    if islemsec:
        islemno = islem_options[islemsec]
with col2:
    kitaplar = get_kitap()
    kitap_options = {f"{kitap[2]}": kitap[0] for kitap in kitaplar}
    kitapsec = st.selectbox("İşlem için Kitap Seçin:", options=list(kitap_options.keys()))
    if kitapsec:
        kitapno = kitap_options[kitapsec]
with col1:
    atarih=st.date_input("Alış Tarih: ")
with col2:
    vtarih=st.date_input("Veriş Tarih: ")

if st.button("Ekle"):
    if atarih and vtarih:
        add_islem(islemno,kitapno,atarih.isoformat(),vtarih.isoformat())
        st.success(f"{kitapadi} Başarı ile Eklendi.")

st.header("İşlem Tablosu")
st.write("---")
icon = get_islem()
if icon:
    for isl in icon:
        isl_id,isl_ogr,isl_ogrsoyad,isl_kitad,isl_a,isl_v=isl
        st.write(f"Kayıt: {isl_id} | Öğrenci: {isl_ogr} {isl_ogrsoyad}  | Kitap: {isl_kitad}| Alış Tarihi: {isl_a} | Veriş Tarihi: {isl_v}")
        col1, col2 = st.columns(2)
        with col1:
            onay = st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?", key=f"ionay{isl_id}")
            if onay:
                update_islem(isl_id)
        with col2:
            if st.button(f"Sil", key=f"idelete{isl_id}_{isl_ogr}"):
                delete_islem(isl[0])
                st.success(f"{isl_id} Kaydı Başarı ile Silindi !")
else:
    st.write("Eklenmiş Kitap Türü Kaydı Yoktur !")

st.header("İşlem Tablo Verileri")
df = pd.DataFrame(icon)
df.columns=['ID','AD','SOYAD','KİTAP','ATARİH','VTARİH']
st.write(df)

kod='''
import streamlit as st
import sqlite3
import pandas as pd

def create_connection():
    conn=sqlite3.connect("Library.db")
    return conn

#OGRENCI TABLO
def add_ogrenci(ograd,ogrsoyad,cinsiyet,dtarih,sinif,puan):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO Ogrenci(ograd,ogrsoyad,cinsiyet,dtarih,sinif,puan) VALUES (?,?,?,?,?,?)",(ograd,ogrsoyad,cinsiyet,dtarih,sinif,puan))
    conn.commit()
    conn.close()

def get_ogrenci():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM Ogrenci")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_ogrenci(ogrenci_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM Ogrenci WHERE ogrno=?",(ogrenci_id,))
    conn.commit()
    conn.close()

def update_ogrenci(ogrenci_id):
    conn=create_connection()
    c=conn.cursor()
    ogrsec = st.selectbox("Güncellemek İstediğiniz Veriyi Seçiniz!", ('ograd', 'ogrsoyad', 'cinsiyet', 'dtarih','sinif','puan'),key=f"selectbox{ogrenci_id}")
    ogrguncel=st.text_input("Veriyi Giriniz: ", key=f"textbox{ogrenci_id}")

    if st.button("Güncelle", key=f"update{ogrenci_id}"):
        if ogrguncel:
            c.execute(f"UPDATE Ogrenci SET {ogrsec}='{ogrguncel}' WHERE ogrno=?", (ogrenci_id,))
            conn.commit()
            st.success("Güncelleme İşlemi Tamamlanmıştır.")
        else:
            st.error("Güncelleme İşlemi Hatalı !")

    conn.commit()
    conn.close()

#---------------------------------------------------------------------------------------------------------------------
# TUR TABLO
def add_tur(turadi):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO Tur(turadi) VALUES (?)",(turadi,))
    conn.commit()
    conn.close()

def get_tur():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM Tur")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_tur(tur_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM Tur WHERE turno=?",(tur_id,))
    conn.commit()
    conn.close()

def update_tur(tur_id):
    conn=create_connection()
    c=conn.cursor()
    turguncel=st.text_input("Güncel Veriyi Giriniz: ", key=f"ttextbox{tur_id}")

    if st.button("Güncelle", key=f"tupdate{tur_id}"):
        if turguncel:
            c.execute(f"UPDATE Tur SET turadi='{turguncel}' WHERE turno=?", (tur_id,))
            conn.commit()
            st.success("Güncelleme İşlemi Tamamlanmıştır.")
        else:
            st.error("Güncelleme İşlemi Hatalı !")

    conn.commit()
    conn.close()

#---------------------------------------------------------------------------------------------------------------------
#YAZAR TABLOSU
def add_yazar(yazarad,yazarsoyad):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO Yazar(yazarad,yazarsoyad) VALUES(?,?)",(yazarad,yazarsoyad))
    conn.commit()
    conn.close()

def get_yazar():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM Yazar")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_yazar(yazar_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM Yazar WHERE yazarno=?",(yazar_id,))
    conn.commit()
    conn.close()

def update_yazar(yazar_id):
    conn=create_connection()
    c=conn.cursor()
    yazarsec = st.selectbox("Güncellemek İstediğiniz Veriyi Seçiniz!", ('yazarad','yazarsoyad'),key=f"yselectbox{yazar_id}")
    yazarguncel=st.text_input("Veriyi Giriniz: ", key=f"ytextbox{yazar_id}")

    if st.button("Güncelle", key=f"yupdate{yazar_id}"):
        if yazarguncel:
            c.execute(f"UPDATE Yazar SET {yazarsec}='{yazarguncel}' WHERE yazarno=?", (yazar_id,))
            conn.commit()
            st.success("Güncelleme İşlemi Tamamlanmıştır.")
        else:
            st.error("Güncelleme İşlemi Hatalı !")

    conn.commit()
    conn.close()

#---------------------------------------------------------------------------------------------------------------------
#KİTAP TABLOSU
def add_kitap(isbnno,kitapadi,yazarno,turno,sayfasayisi,puan):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO Kitap(isbnno,kitapadi,yazarno,turno,sayfasayisi,puan) VALUES(?,?,?,?,?,?)",(isbnno,kitapadi,yazarno,turno,sayfasayisi,puan))
    conn.commit()
    conn.close()

def get_kitap():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT kitapno,isbnno,kitapadi,yazarad,yazarsoyad,turadi,sayfasayisi,puan FROM Kitap k JOIN Yazar y ON k.yazarno=y.yazarno JOIN tur t ON k.turno=t.turno")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_kitap(kitap_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM Kitap WHERE kitapno=?",(kitap_id,))
    conn.commit()
    conn.close()

def update_kitap(kitap_id):
    conn=create_connection()
    c=conn.cursor()
    kitapsec = st.selectbox("Güncellemek İstediğiniz Veriyi Seçiniz!", ('isbnno','kitapadi','sayfasayisi','puan','yazarno','turno'),key=f"kselectbox{kitap_id}")
    kitapguncel=st.text_input("Veriyi Giriniz: ", key=f"ktextbox{kitap_id}")

    if st.button("Güncelle", key=f"kupdate{kitap_id}"):
        if kitapguncel:
            c.execute(f"UPDATE Kitap SET {kitapsec}='{kitapguncel}' WHERE kitapno=?", (kitap_id,))
            conn.commit()
            st.success("Güncelleme İşlemi Tamamlanmıştır.")
        else:
            st.error("Güncelleme İşlemi Hatalı !")

    conn.commit()
    conn.close()

#---------------------------------------------------------------------------------------------------------------------
#ISLEM TABLOSU
def add_islem(ogrno,kitapno,atarih,vtarih):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO Islem(ogrno,kitapno,atarih,vtarih) VALUES(?,?,?,?)",(ogrno,kitapno,atarih,vtarih))
    conn.commit()
    conn.close()

def get_islem():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT islemno,ograd,ogrsoyad,kitapadi,atarih,vtarih FROM Islem i JOIN Ogrenci o ON i.ogrno=o.ogrno JOIN Kitap k ON i.kitapno=k.kitapno")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_islem(islem_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM Islem WHERE islemno=?",(islem_id,))
    conn.commit()
    conn.close()

def update_islem(islem_id):
    conn=create_connection()
    c=conn.cursor()
    islemsec = st.selectbox("Güncellemek İstediğiniz Veriyi Seçiniz!", ('ogrno','kitapno','atarih','vtarih'),key=f"iselectbox{islem_id}")
    islemguncel=st.text_input("Veriyi Giriniz: ", key=f"itextbox{islem_id}")

    if st.button("Güncelle", key=f"iupdate{islem_id}"):
        if islemguncel:
            c.execute(f"UPDATE Islem SET {islemsec}='{islemguncel}' WHERE islemno=?", (islem_id,))
            conn.commit()
            st.success("Güncelleme İşlemi Tamamlanmıştır.")
        else:
            st.error("Güncelleme İşlemi Hatalı !")

    conn.commit()
    conn.close()
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

# SAYFA TASARIMI

# OGRENCI TABLOSU
st.title("Kütüphane Uygulaması")
st.header("Öğrenci Bilgileri")
st.write("---")

col1, col2 = st.columns(2)
with col1:
    ograd=st.text_input("Öğrenci Ad: ")
with col2:
    ogrsoyad=st.text_input("Öğrenci Soyad: ")
with col1:
    cinsiyet=st.text_input("Öğrenci Cinsiyet:" )
with col2:
    dtarih=st.date_input("Tarih: ")
with col1:
    sinif=st.text_input("Öğrenci Sınıf: ")
with col2:
    puan=st.text_input("Öğrenci Puan: ")

if st.button("Öğrenci Ekle"):
    if ograd and ogrsoyad and cinsiyet and dtarih and sinif and puan:
        add_ogrenci(ograd,ogrsoyad,cinsiyet,dtarih.isoformat(),sinif,puan)
        st.success(f"{ograd} {ogrsoyad} başarı ile eklendi")
    else:
        st.error("Başlık alanı gereklidir !")

st.header("Öğrenci Tablosu")
st.write("---")
con = get_ogrenci()
if con:
    for ogr in con:
        ogr_id,ogr_ad,ogr_soyad,ogr_cns,ogr_tarih,ogr_sinif,ogr_puan=ogr
        st.write(f"Kayıt: {ogr_id} | Ad: {ogr_ad} | Soyad: {ogr_soyad} | Sınıf: {ogr_sinif} | Cinsiyet: {ogr_cns} | Tarih: {ogr_tarih} | Puan: {ogr_puan}")

        col1,col2 = st.columns(2)
        with col1:
            onay = st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?", key=f"onay{ogr_id}")
            if onay:
                update_ogrenci(ogr_id)
        with col2:
            if st.button(f"Sil",key=f"delete{ogr_id}"):
                delete_ogrenci(ogr[0])
                st.success(f"{ogr_ad} {ogr_soyad} Başarı ile Silindi !")
else:
    st.write("Eklenmiş Öğrenci Kaydı Yoktur !")

st.header("Öğrenci Tablo Verileri")
df = pd.DataFrame(con)
df.columns=['ID','ÖĞRENCİ AD','ÖĞRENCİ SOYAD','CİNSİYET','TARİH','SINIF','PUAN']
st.write(df)

#---------------------------------------------------------------------------------------------------------------------
# TUR TASARIMI
st.header("Kitap Türü Bilgileri")
st.write("---")

turadi=st.text_input("Kitap Türü Giriniz: ")

if st.button("Tür Ekle"):
    if turadi:
        add_tur(turadi)
        st.success(f"{turadi} Türü Eklendi.")

st.header("Kitap Türleri")
tcon = get_tur()
if tcon:
    for tur in tcon:
        tur_id,tur_ad=tur
        st.write(f"Kayıt: {tur_id} | Kitap Türü: {tur_ad}")

        col1,col2 = st.columns(2)
        with col1:
            onay = st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?", key=f"tonay{tur_id}")
            if onay:
                update_tur(tur_id)
        with col2:
            if st.button(f"Sil",key=f"tdelete{tur_id}"):
                delete_tur(tur[0])
                st.success(f"{tur_ad} Başarı ile Silindi !")
else:
    st.write("Eklenmiş Öğrenci Kaydı Yoktur !")

st.header("Kitap Türü Tablo Verileri")
df = pd.DataFrame(tcon)
df.columns=['ID','KİTAP TÜRÜ']
st.write(df)

#---------------------------------------------------------------------------------------------------------------------
#YAZAR TASARIMI
st.header("Yazar Bilgileri")
st.write("---")
col1, col2 = st.columns(2)
with col1:
    yazarad=st.text_input("Yazar Adı: ")
with col2:
    yazarsoyad=st.text_input("Yazar Soyadı: ")

if st.button("Yazar Ekle"):
    if yazarad and yazarsoyad:
        add_yazar(yazarad,yazarsoyad)
        st.success(f"{yazarad} {yazarsoyad} Başarı ile Eklendi.")

col1,col2 = st.columns(2)
st.header("Yazar Tablosu")
st.write("---")
ycon = get_yazar()
if ycon:
    for yaz in ycon:
        yazar_id,yazar_ad,yazar_soyad=yaz
        st.write(f"Kayıt: {yazar_id} | Yazar Ad: {yazar_ad} | Yazar Soyad: {yazar_soyad}")
        col1,col2 = st.columns(2)
        with col1:
            onay = st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?", key=f"yonay{yazar_id}")
            if onay:
                update_yazar(yazar_id)
        with col2:
            if st.button(f"Sil",key=f"ydelete{yazar_id}"):
                delete_yazar(yaz[0])
                st.success(f"{yazar_ad} {yazar_soyad} Başarı ile Silindi !")
else:
    st.write("Eklenmiş Kitap Türü Kaydı Yoktur !")

st.header("Yazar Tablo Verileri")
df = pd.DataFrame(ycon)
df.columns=['ID','YAZAR AD','YAZAR SOYAD']
st.write(df)

#---------------------------------------------------------------------------------------------------------------------
#KİTAP TASARIMI
st.header("Kitap Bilgileri")
st.write("---")
col1, col2 = st.columns(2)
with col1:
    isbnno=st.text_input("ISBN No: ")
with col2:
    kitapadi=st.text_input("Kitap Adı: ")
with col1:
    sayfasayisi=st.text_input("Sayfa Sayısı: ")
with col2:
    kpuan=st.text_input("Puan: ")
with col1:
    yazarlar = get_yazar()  # Yazarları alıyoruz
    yazar_options = {f"{yazar[1]} {yazar[2]}": yazar[0] for yazar in yazarlar}  # Yazar adı soyad ve id
    yazarsec = st.selectbox("Kitap için Yazar Seçin:", options=list(yazar_options.keys()))
    if yazarsec:
        yazarno = yazar_options[yazarsec]
with col2:
    turler = get_tur()  # Kitap türlerini alıyoruz
    tur_options = {f"{tur[1]}": tur[0] for tur in turler}
    tursec = st.selectbox("Kitap için Tür Seçin:", options=list(tur_options.keys()))
    if tursec:
        turno = tur_options[tursec]

if st.button("Kitap Ekle"):
    if kitapadi and isbnno and sayfasayisi and kpuan:
        add_kitap(isbnno,kitapadi,yazarno,turno,sayfasayisi,kpuan)
        st.success(f"{kitapadi} Başarı ile Eklendi.")

st.header("Kitap Tablosu")
st.write("---")
kcon = get_kitap()
if kcon:
    for kit in kcon:
        k_id,k_isbn,k_ad,k_yad,k_ysoyad,k_tur,k_sayfa,k_puan=kit
        st.write(f"Kayıt: {k_id} | Kitap: {k_ad} | Yazar: {k_yad} {k_ysoyad} | ISBN No: {k_isbn} | Tür: {k_tur} | Sayfa: {k_sayfa} Puan: {k_puan}")
        col1,col2 = st.columns(2)
        with col1:
            onay = st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?", key=f"konay_{k_id}_{k_isbn}")
            if onay:
                update_kitap(k_id)
        with col2:
            if st.button(f"Sil",key=f"idelete{k_id}"):
                delete_kitap(kit[0])
                st.success(f"{k_id} Kaydı Başarı ile Silindi !")
else:
    st.write("Eklenmiş Kitap Türü Kaydı Yoktur !")

st.header("Kitap Tablo Verileri")
df = pd.DataFrame(kcon)
df.columns=['ID','ISBN NO','KİTAP','YAZAR AD','YAZAR SOYAD','KİTAP TÜRÜ','SAYFA SAYISI','PUAN']
st.write(df)

# ---------------------------------------------------------------------------------------------------------------------
# ISLEM TASARIMI
st.header("İşlem Bilgileri")
st.write("---")
col1, col2 = st.columns(2)
with col1:
    islemler = get_ogrenci()
    islem_options = {f"{islem[1]} {islem[2]}": islem[0] for islem in islemler}
    islemsec = st.selectbox("İşlem için Öğrenci Seçin:", options=list(islem_options.keys()))
    if islemsec:
        islemno = islem_options[islemsec]
with col2:
    kitaplar = get_kitap()
    kitap_options = {f"{kitap[2]}": kitap[0] for kitap in kitaplar}
    kitapsec = st.selectbox("İşlem için Kitap Seçin:", options=list(kitap_options.keys()))
    if kitapsec:
        kitapno = kitap_options[kitapsec]
with col1:
    atarih=st.date_input("Alış Tarih: ")
with col2:
    vtarih=st.date_input("Veriş Tarih: ")

if st.button("Ekle"):
    if atarih and vtarih:
        add_islem(islemno,kitapno,atarih.isoformat(),vtarih.isoformat())
        st.success(f"{kitapadi} Başarı ile Eklendi.")

st.header("İşlem Tablosu")
st.write("---")
icon = get_islem()
if icon:
    for isl in icon:
        isl_id,isl_ogr,isl_ogrsoyad,isl_kitad,isl_a,isl_v=isl
        st.write(f"Kayıt: {isl_id} | Öğrenci: {isl_ogr} {isl_ogrsoyad}  | Kitap: {isl_kitad}| Alış Tarihi: {isl_a} | Veriş Tarihi: {isl_v}")
        col1, col2 = st.columns(2)
        with col1:
            onay = st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?", key=f"ionay{isl_id}")
            if onay:
                update_islem(isl_id)
        with col2:
            if st.button(f"Sil", key=f"idelete{isl_id}_{isl_ogr}"):
                delete_islem(isl[0])
                st.success(f"{isl_id} Kaydı Başarı ile Silindi !")
else:
    st.write("Eklenmiş Kitap Türü Kaydı Yoktur !")

st.header("İşlem Tablo Verileri")
df = pd.DataFrame(icon)
df.columns=['ID','AD','SOYAD','KİTAP','ATARİH','VTARİH']
st.write(df)
'''

st.header('Kaynak Kodları')
st.code(kod,language='python')
