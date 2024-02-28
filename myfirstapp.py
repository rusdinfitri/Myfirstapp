%%writefile Advertising.py
import streamlit as st
import pandas as pd
import pickle

st.write("""
# Sales Prediction App

This app predicts the **Sales** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV= st.sidebar.slider('TV', 0.7, 297.0, 100.0) #all Float
    Radio = st.sidebar.slider('Radio', 0, 50.0, 15.0)
    Newspaper = st.sidebar.slider('Newspaper', 0.3, 114.0, 20.0)

    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper,}

    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("Advertisingmodel.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
