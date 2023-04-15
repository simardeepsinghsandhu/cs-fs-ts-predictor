import streamlit as st
import pickle
import numpy as np

st.set_page_config(layout="wide")

st.header('CS, TS and FS Prediction App')

st.write('Please provide the following inputs:\n')

# inputs

col1, col2 = st.columns(2)
with col1:
    cement = st.number_input('Cement', min_value = 0.231, max_value = 1.266)
    sand = st.number_input('Sand', min_value = 0.0, max_value = 6.9)
    bsf = st.number_input('BSF', min_value = 0.0, max_value = 2.3)
    w_b = st.number_input('Water/Binder', min_value = 0.0, max_value = 3.6)
    fibre_length = st.number_input('Fibre Length', min_value = 6.0, max_value = 19.0)
    fibre_elasticity = st.number_input('Fibre Elasticity', min_value = 16.9, max_value = 66.0)
    fibre_density = st.number_input('Fibre Density', min_value = 970.0, max_value = 1846.0)
with col2:
    fly_ash = st.number_input('Fly Ash C', min_value = 0.0, max_value = 4.4)
    limestone = st.number_input('Limestone', min_value = 0.0, max_value = 3.3)
    silica_fume = st.number_input('Silica Fume', min_value = 0.0, max_value = 0.75)
    sp = st.number_input('SP', min_value = 0.0, max_value = 16.85)
    fibre_volume = st.number_input('Fibre Volume(%)', min_value = 0.0, max_value = 11.21)
    fibre_dia = st.number_input('Fibre Dia(Um)', min_value = 12.0, max_value = 200.0)

features = np.array([cement, fly_ash, sand, limestone, bsf, silica_fume, w_b, sp, fibre_length, fibre_volume, fibre_elasticity, fibre_dia, fibre_density])
features = features.reshape(1, -1)
print(features.shape)
option = st.selectbox(
    'Please select the entity to be predicted:',
    ('Compressive Strength(Mpa)', 'Tensile Strain Capacity(%)', 'Flexural Strength(Mpa)'))

st.write('You selected:', option)

if st.button('Predict'):
    if option=='Compressive Strength(Mpa)':
        model = pickle.load(open('cs.sav', 'rb'))
        pred = model.predict(features)
        st.write('CS value:', pred)
    elif option=='Tensile Strain Capacity(%)':
        model = pickle.load(open('ts.sav', 'rb'))
        pred = model.predict(features)
        st.write('TS value:', pred)
    else:
        model = pickle.load(open('fs.sav', 'rb'))
        pred = model.predict(features)
        st.write('FS value:', pred)
