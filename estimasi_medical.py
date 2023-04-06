import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('estimasi_medical.sav', 'rb'))

st.title('Estimasi Biaya Medis dalam US Dolar')

age = st.number_input('Input Umur (tahun)')
sex = st.number_input('Input Jenis Kelamin (F = 2 or M = 1)')
bmi = st.number_input('Input BMI')
children = st.number_input('Input Jumlah Anak Yang di Cover Asuransi')
smoker = st.number_input('Apakah Anda Merokok? (N = 2 or Y = 1)')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[age,sex,bmi,children,smoker]]
    )
    st.write ('Estimasi Biaya Medis dalam US Dolar : ', predict)
    st.write ('Estimasi Biaya Medis dalam IDR (Juta) :', predict*15000)