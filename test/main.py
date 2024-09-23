import cv2
import pytesseract
from gtts import gTTS
import os
# import streamlit as st

# executável do tesseract
path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_imagens():
    imagem = cv2.imread('img/image3.png')
    pytesseract.pytesseract.tesseract_cmd = path
    texto = pytesseract.image_to_string(imagem, lang='por')
    
    return texto
    # print(texto)
    

def converte_voz():
    texto = get_imagens()
    tts = gTTS(text=texto, lang='pt')
    tts.save('output.mp3')
    os.system("start output.mp3")
    
    return texto


# põe 10zao de voz ai pra nois
# tts = gTTS(text=texto, lang='pt')
# tts.save('output.mp3')
# os.system("start output.mp3")

# output_path = 'outputs/resultado.txt'

# lendo_imagem(texto, output_path)

# st.title("Image to Text and Speech Converter")
# uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])


# if uploaded_file is not None:
#     # Save the uploaded file to a temporary location
#     with open("temp_image.png", "wb") as f:
#         f.write(uploaded_file.getbuffer())
    
#     # Display the uploaded image
#     st.image("temp_image.png", caption="Uploaded Image", use_column_width=True)
    
#     # Convert image to text
#     texto = get_imagens("temp_image.png")
#     st.write("Extracted Text:")
#     st.write(texto)
    
#     # Convert text to speech
#     if st.button("Convert to Speech"):
#         audio_file = converte_voz(texto)
#         audio_bytes = open(audio_file, "rb").read()
#         st.audio(audio_bytes, format="audio/mp3")