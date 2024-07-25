import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('22611027_onlinefoods_model.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Penjualan Online')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Age = st.text_input ('input nilai Age')

with col2 :
    Gender = st.text_input ('input nilai Gender')

with col1 :
    MaritalStatus = st.text_input ('input nilai Blood Marital Status')

with col2 :
    Occupation = st.text_input ('input nilai Skin Occupation')

with col1 :
    MonthlyIncome = st.text_input ('input nilai Monthly Income')

with col2 :
    EducationQualifications = st.text_input ('input nilai Educational Qualifications')

with col1 :
    Familysize = st.text_input ('input nilai Diabetes Family size')

with col2 :
    latitude = st.text_input ('input nilai latitude')

with col2 :
    longitude = st.text_input ('input nilai longitude')

with col2 :
    Pincode = st.text_input ('input nilai Pin code')

with col2 :
    Output = st.text_input ('input nilai Output')

with col2 :
    Feedback = st.text_input ('input nilai Feedback')
# code untuk prediksi
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Age, Gender, MaritalStatus, Occupation, MonthlyIncome, EducationQualifications, Familysize, latitude, longitude, Pincode, Output, Feedback]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'
st.success(diab_diagnosis)