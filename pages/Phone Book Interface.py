import streamlit as st
import sqlite3
import pandas as pd

def create_connection():
    conn=sqlite3.connect("phoneBook.db")
    return conn

def add_contact(name,surname,phone,email):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO contacts(name,surname,phone,email) VALUES (?,?,?,?)",(name,surname,phone,email))
    conn.commit()
    conn.close()

def get_contacts():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM contacts")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_contact(contact_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM contacts where id=?",(contact_id,))
    conn.commit()
    conn.close()

def full_delete():
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM contacts")
    conn.commit()
    conn.close()

def update_contact(contact_id):
    conn = create_connection()
    c = conn.cursor()
    deger = st.selectbox("Güncellemek İstediğiniz Veriyi Seçiniz!", ('name', 'surname', 'phone', 'email'),key=f"selectbox{contact_id}")
    veri = st.text_input("Veriyi Giriniz:",key=f"textbox{contact_id}")

    if st.button("Güncelle",key=f"update{contact_id}"):
        if veri:  # Veri girilip girilmediğini kontrol et
            c.execute(f"UPDATE contacts SET {deger}='{veri}' WHERE id=?", (contact_id,))
            conn.commit()
            st.success("Başarı ile güncellendi!")
        else:
            st.error("Lütfen güncellemek için bir değer giriniz.")
    conn.commit()
    conn.close()

#streamlit Arayüzü
st.title("Telefon Rehberi Arayüzü")

#kişi ekleme
st.header("Yeni Kişi Ekle")

col1,col2,col3,col4 = st.columns(4)
with col1:
    name=st.text_input("İsim")
with col2:
    surname=st.text_input("Soyisim")
with col3:
    phone=st.text_input("Telefon Numarası")
with col4:
    email=st.text_input("E-Posta Adresi")

if st.button("Kişi Ekle"):
    if name and surname and phone:
        add_contact(name,surname,phone,email)
        st.success(f"{name} {surname} başarı ile eklendi.")
    else:
        st.error("İsim, Soyisim ve Telefon Numarası boş geçilemez !")

st.header("Kayıtlı Kişiler")

con = get_contacts()
if con:
    for contact in con:
        con_id,con_name,con_surname,con_tel,con_eposta=contact
        st.write(f"Kayıt:{con_id} - İsim: {con_name} | Soyisim: {con_surname} | Telefon No: {con_tel} | E-Posta: {con_eposta}")
        col1,col2 = st.columns(2)
        with col1:
            onay=st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?",key=f"onay{con_id}")
            if onay:
                update_contact(con_id)
        with col2:
            if st.button("Sil", key=f"delete-{con_id}"):
                delete_contact(contact[0])
                st.success(f"{con_name} {con_surname} Başarı ile Silindi.")
    if st.button("Tümünü Sil"):
        full_delete()
        st.warning("Tüm Kayıtlar Silindi !")
else:
    st.write("Eklenmiş Rehber Kaydı Yoktur !")

st.header("Rehber Görünümü")
df = pd.DataFrame(con)
df.columns=['ID','AD','SOYAD','TELEFON','EMAIL']
st.write(df)

kod='''
import streamlit as st
import sqlite3
import pandas as pd

def create_connection():
    conn=sqlite3.connect("phoneBook.db")
    return conn

def add_contact(name,surname,phone,email):
    conn=create_connection()
    c=conn.cursor()
    c.execute("INSERT INTO contacts(name,surname,phone,email) VALUES (?,?,?,?)",(name,surname,phone,email))
    conn.commit()
    conn.close()

def get_contacts():
    conn=create_connection()
    c=conn.cursor()
    c.execute("SELECT * FROM contacts")
    rows=c.fetchall()
    conn.close()
    return rows

def delete_contact(contact_id):
    conn=create_connection()
    c=conn.cursor()
    c.execute("DELETE FROM contacts where id=?",(contact_id,))
    conn.commit()
    conn.close()

def full_delete():
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM contacts")
    conn.commit()
    conn.close()

def update_contact(contact_id):
    conn = create_connection()
    c = conn.cursor()
    deger = st.selectbox("Güncellemek İstediğiniz Veriyi Seçiniz!", ('name', 'surname', 'phone', 'email'),key=f"selectbox{contact_id}")
    veri = st.text_input("Veriyi Giriniz:",key=f"textbox{contact_id}")

    if st.button("Güncelle",key=f"update{contact_id}"):
        if veri:  # Veri girilip girilmediğini kontrol et
            c.execute(f"UPDATE contacts SET {deger}='{veri}' WHERE id=?", (contact_id,))
            conn.commit()
            st.success("Başarı ile güncellendi!")
        else:
            st.error("Lütfen güncellemek için bir değer giriniz.")
    conn.commit()
    conn.close()

#streamlit Arayüzü
st.title("Telefon Rehberi Arayüzü")

#kişi ekleme
st.header("Yeni Kişi Ekle")

col1,col2,col3,col4 = st.columns(4)
with col1:
    name=st.text_input("İsim")
with col2:
    surname=st.text_input("Soyisim")
with col3:
    phone=st.text_input("Telefon Numarası")
with col4:
    email=st.text_input("E-Posta Adresi")

if st.button("Kişi Ekle"):
    if name and surname and phone:
        add_contact(name,surname,phone,email)
        st.success(f"{name} {surname} başarı ile eklendi.")
    else:
        st.error("İsim, Soyisim ve Telefon Numarası boş geçilemez !")

st.header("Kayıtlı Kişiler")

con = get_contacts()
if con:
    for contact in con:
        con_id,con_name,con_surname,con_tel,con_eposta=contact
        st.write(f"Kayıt:{con_id} - İsim: {con_name} | Soyisim: {con_surname} | Telefon No: {con_tel} | E-Posta: {con_eposta}")
        col1,col2 = st.columns(2)
        with col1:
            onay=st.checkbox("Güncelleme Yapmak İstiyor Musunuz ?",key=f"onay{con_id}")
            if onay:
                update_contact(con_id)
        with col2:
            if st.button("Sil", key=f"delete-{con_id}"):
                delete_contact(contact[0])
                st.success(f"{con_name} {con_surname} Başarı ile Silindi.")
    if st.button("Tümünü Sil"):
        full_delete()
        st.warning("Tüm Kayıtlar Silindi !")
else:
    st.write("Eklenmiş Rehber Kaydı Yoktur !")

st.header("Rehber Görünümü")
df = pd.DataFrame(con)
df.columns=['ID','AD','SOYAD','TELEFON','EMAIL']
st.write(df)
'''

st.header('Kaynak Kodları')
st.code(kod,language='python')
