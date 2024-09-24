Este projeto é um aplicativo web que permite aos usuários fazer upload de uma imagem, extrair texto da imagem usando OCR (Optical Character Recognition) e converter o texto extraído em áudio usando a tecnologia de conversão de texto em fala (TTS).


# Estrutura do Projeto

- `app.py`: Código do servidor Flask com endpoints para fazer upload de imagens e recuperar arquivos de áudio.
- `main.py`: Código do aplicativo Streamlit.
- `.gitignore`: Especifica arquivos e diretórios a serem ignorados pelo Git.
- `requirements.txt`: Lista as dependências necessárias para o projeto.
- `test/`: Diretório contendo código de teste.


# Pré-requisitos

    Python 3.x
    Pip (gerenciador de pacotes do Python)
    Tesseract OCR


# Instalação

1. Clone o repositório e navegue até o diretório do projeto:
    ```sh
    git clone https://github.com/yourusername/image-to-audio-converter.git
    cd image-to-audio-converter
    ```

2. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Unix ou MacOS
    ```

3. Instale as dependências do projeto:
    ```sh
    pip install -r requirements.txt
    ```

# Execução do App

1. Inicie o servidor Flask:
    ```sh
    python app.py
    ```
    O serviço vai estar disponível em `http://localhost:5000`.

2. Num segundo terminal, inicie o app do Streamlit:
    ```sh
    streamlit run streamlit_app.py
    ```
    O serviço vai estar disponível em `http://localhost:8501`.


## Como usar ?

1. Abra seu navegador e vá para `http://localhost:8501` para acessar o aplicativo Streamlit.
2. Carregue um arquivo de imagem.
3. O aplicativo irá processar a imagem, extrair o texto, convertê-lo em áudio e disponibilizar um reprodutor de áudio para ouvir o áudio gerado.


# Tecnologias Utilizadas

- **Python**
- **Flask**
- **Tesseract OCR**
- **Google Text-to-Speech API**
- **Streamlit**
