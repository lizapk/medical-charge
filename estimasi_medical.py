import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('estimasi_medical.sav', 'rb'))

st.title('Estimasi Biaya Medis dalam US Dolar')

age = st.number_input('Input Umur (tahun)')
sex = st.number_input('Input Jenis Kelamin (F/M)')
bmi = st.number_input('Input BMI')
children = st.number_input('Input Jumlah Anak Yang di Cover Asuransi')
smoker = st.number_input('Apakah Anda Merokok? (N/Y)')

df = pd.DataFrame({'sex': ['M', 'F', 'F', 'M']})
def convert_gender(sex):
    if sex == 'M':
        return 1
    elif sex == 'F':
        return 2
    else:
        return None
df2 = pd.DataFrame({'smoker': ['Y', 'N', 'N', 'Y']})
def convert_smoker(smoker):
    if smoker == 'Y':
        return 1
    elif smoker == 'N':
        return 2
    else:
        return None

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[age,sex,bmi,children,smoker]]
    )
    st.write ('Estimasi Biaya Medis dalam US Dolar : ', predict)
    st.write ('Estimasi Biaya Medis dalam IDR (Juta) :', predict*15000)
