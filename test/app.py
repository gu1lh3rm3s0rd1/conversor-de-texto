from flask import Flask, request, jsonify, redirect, url_for, send_from_directory
# from main import get_imagens, converte_voz
import os
import cv2
import pytesseract
from gtts import gTTS

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
AUDIO_FOLDER = 'audio'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(AUDIO_FOLDER):
    os.makedirs(AUDIO_FOLDER)


# @app.route("/")
# # class Home():
# def home():
#     return '''
#         <!doctype html>
#         <title>Upload an Image</title>
#         <h1>Upload an Image</h1>
#         <form method=post enctype=multipart/form-data action="/upload">
#         <input type=file name=file>
#         <input type=submit value=Upload>
#         </form>
# '''


@app.route('/upload', methods=['POST'])
# class Upload():
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhuma imagem carregada.'})
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Nenhuma imagem selecionada.'})
    
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

    # extrai o texto da imagem
    img = cv2.imread(filepath)
    text = pytesseract.image_to_string(img)

    # converte o texto em áudio
    tts = gTTS(text)
    audio_filename = filename + '.mp3'
    audio_path = os.path.join(app.config['AUDIO_FOLDER'], audio_filename)
    tts.save(audio_path)

    return jsonify({'audio_url': url_for('uploaded_file', filename=audio_filename, _external=True)})


@app.route('/uploads/<filename>')
# class UploadedFile():
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# @app.route("/imagem")
# class Imagem():
#     def get_imagens(method='GET'):


if __name__ == '__main__':
    app.run(debug=True)
