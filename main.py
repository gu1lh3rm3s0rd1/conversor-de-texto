import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/upload"

st.title('Conversor de Imagem para Áudio')

uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "png", "jpeg", "gif"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Imagem carregada', use_column_width=True)

    with st.spinner('Processando a imagem...'):
        files = {'file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        audio_url = response.json()['audio_url']
        st.audio(audio_url)
    else:
        st.error("Erro ao processar a imagem. Tente novamente.")

with st.container():
    st.write("------")