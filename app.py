import streamlit as st
import pickle
import numpy as np

st.set_page_config(layout="wide")

st.header('CS, TS and FS Prediction App')

st.write('Please provide the following inputs:\n')

# inputs

col1, col2 = st.columns(2)
with col1:
    cement = st.number_input('Cement')
    fly_ash = st.number_input('Fly Ash C')
    bsf = st.number_input('BSF')
    w_b = st.number_input('Water/Binder')
    fibre_length = st.number_input('Fibre Length')
    fibre_elasticity = st.number_input('Fibre Elasticity')
    fibre_density = st.number_input('Fibre Density')
with col2:
    sand = st.number_input('Sand')
    limestone = st.number_input('Limestone')
    silica_fume = st.number_input('Silica Fume')
    sp = st.number_input('SP')
    fibre_volume = st.number_input('Fibre Volume(%)')
    fibre_dia = st.number_input('Fibre Dia(Um)')

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