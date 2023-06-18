import pickle
import numpy as np 
import streamlit as st 

# membaca model
model = pickle.load(open('Penyakit_Jantung.sav', 'rb'))

#judul web
st.title('Home Checking Your Heart')

col1, col2, col3 = st.columns(3)

with col1 :
    age = st.number_input('Usia')
with col2 : 
    sex = st.number_input('Jenis Kelamin (1: Pria ; 0: Wanita)')
with col3 :
    cp = st.number_input ('Jenis Nyeri Dada')
with col1 :
    trestbps = st.number_input ('Tekanan Darah')
with col2 :
    chol = st.number_input ('Nilai Kolestrol')
with col3 :
    fbs = st.number_input ('Gula Darah')
with col1 :
    restecg = st.number_input ('Hasil Elektrokadiografi')
with col2 :
    thalach = st.number_input ('Detak Jantung Max.')
with col3 :
    exang = st.number_input ('Induksi Angina')
with col1 :
    oldpeak = st.number_input ('ST Depression')
with col2 :
    slope =  st.number_input ('Slope')
with col3 :
    ca = st.number_input ('Nilai CA')
with col1 :
    thal = st.number_input ('Nilai Thal')

# Kode Prediksi
heart_diagnosis = ''

# Membuat tombol prediksi
if st.button ('Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if(heart_prediction[0] == 1):
        heart_diagnosis = 'Pasien Terindikasi Penyakit Jantung'
    else :
        heart_diagnosis = 'Pasien Tidak Terindikasi Penyakit Jantung'
st.success(heart_diagnosis)