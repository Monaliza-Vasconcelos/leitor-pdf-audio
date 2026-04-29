# 📄 Leitor de PDF com Áudio

Aplicação web feita com Django que permite enviar um PDF e transformá-lo em áudio automaticamente.

---

## 🚀 Funcionalidades

- Upload de arquivos PDF
- Extração de texto com PyPDF2
- Conversão de texto em áudio usando Edge TTS
- Geração de áudio completo (sem limite de caracteres)
- Player de áudio integrado

---

## 🛠️ Tecnologias utilizadas

- Python
- Django
- PyPDF2
- edge-tts
- pydub
- FFmpeg

---

## 📦 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/leitor-pdf-audio.git
cd leitor-pdf-audio
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Instale o FFmpeg

Baixe e adicione ao PATH:
```bash
https://ffmpeg.org/download.html
```

### 5. Rode o servidor
```bash
python manage.py runserver
```

Acesse:
```bash
http://127.0.0.1:8000/
