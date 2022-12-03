import pickle
import streamlit as st

# membaca model
transfusion_model = pickle.load(open('blood_transfusion.sav', 'rb'))

#Judul Web
st.title(' Data Mining Prediksi  Mendonorkan Darah')

Recency  = st.text_input('Masukan Berapa Bulan Sejak Terakhir Mendonorkan darah Dengan Range (0, ...., 74 )')

Frequency  = st.text_input('Masukan Jumlah Frekuensi Total Donasi Darah Dengan Range ( 1, ...., 50 ) ')

Monetary = st.text_input('Masukan Total Darah Yang Didonasikan Dalam c.c. Dengan Range( 250, ...., 12500)')

Time  = st.text_input('Masukan Berapa Bulan Sejak Donasi Pertama Dengan Range (2, ...., 98 )')

# kode prediksi 
transfusion_diagnosis =''

# membuat tombol untuk prediksi
if st.button(' Prediksi Mendonorkan Darah'):
    transfusion_prediction = transfusion_model.predict([[Recency, Frequency, Monetary, Time]])
    
    if(transfusion_prediction[0]==0):
        transfusion_diagnosis = 'Bersedia Mendonorkan Darah'
    else :
        transfusion_diagnosis = 'Tidak Bersedia Mendorokan Darah'
st.success(transfusion_diagnosis)

