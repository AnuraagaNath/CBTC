import streamlit as st
from tensorflow import keras
import pandas as pd

model = keras.models.load_model('model.keras')

data = pd.read_csv('Spam Email Detection/Spam Email Detection - spam.csv', usecols=['v2'])
st.title('Spam message Detector 📬')

st.markdown('### Enter your message to check if it is spam or not')
samples = data.sample(10)
samples = samples.reset_index()
samples = samples.drop('index', axis=1)
samples.columns = ['sample messages']
st.write(samples)

sentence = st.text_input(label='Enter your message text here',max_chars=200, placeholder='Free donuts, send your message id for free followers on facebook')

if sentence:
    if model.predict(pd.Series(sentence)) > 0.5:
        st.warning('The message is Spam!')
    else:
        st.success('The message is not Spam!')

