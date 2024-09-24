from flask import Flask, request, redirect, url_for, send_from_directory, jsonify
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


# rota para upload da imagem a ser convertida
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo carregado.'}), 400
    file = request.files['file']
    if file.arquivo == '':
        return jsonify({'error': 'Nenhum arquivo selecionado.'}), 400
    if file:
        arquivo = file.arquivo
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], arquivo)
        file.save(filepath)

        img = cv2.imread(filepath)
        text = pytesseract.image_to_string(img)

        tts = gTTS(text)
        arquivo_audio = arquivo + '.mp3'
        audio_path = os.path.join(app.config['AUDIO_FOLDER'], arquivo_audio)
        tts.save(audio_path)

        return jsonify({'audio_url': url_for('uploaded_file', arquivo=arquivo_audio, _external=True)})


# rota para servir o arquivo de áudio
@app.route('/audio/<arquivo>')
def uploaded_file(arquivo):
    return send_from_directory(app.config['AUDIO_FOLDER'], arquivo)


if __name__ == '__main__':
    app.run(debug=True)
