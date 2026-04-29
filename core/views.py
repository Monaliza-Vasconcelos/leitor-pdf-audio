from django.shortcuts import render
from .forms import UploadPDFForm
import PyPDF2

import os
import uuid
import asyncio
import edge_tts
from django.conf import settings

from pydub import AudioSegment


# 🔹 dividir texto
def dividir_texto(texto, tamanho=3000):
    return [texto[i:i+tamanho] for i in range(0, len(texto), tamanho)]


# 🔹 gerar áudio de um pedaço
async def gerar_audio_async(texto, caminho):
    tts = edge_tts.Communicate(
        text=texto,
        voice="pt-BR-AntonioNeural"
    )
    await tts.save(caminho)


# 🔹 gerar vários áudios
def gerar_audio_completo(texto):
    partes = dividir_texto(texto)
    arquivos = []

    for i, parte in enumerate(partes):
        nome = f"{uuid.uuid4()}_{i}.mp3"
        caminho = os.path.join(settings.MEDIA_ROOT, nome)

        asyncio.run(gerar_audio_async(parte, caminho))
        arquivos.append(caminho)

    return arquivos


# 🔹 juntar áudios
def juntar_audios(lista_arquivos):
    audio_final = AudioSegment.empty()

    for arquivo in lista_arquivos:
        som = AudioSegment.from_mp3(arquivo)
        audio_final += som

    nome_final = f"{uuid.uuid4()}_final.mp3"
    caminho_final = os.path.join(settings.MEDIA_ROOT, nome_final)

    audio_final.export(caminho_final, format="mp3")

    return settings.MEDIA_URL + nome_final


# 🔥 VIEW PRINCIPAL
def upload_pdf(request):
    texto = ""
    audio_url = None

    if request.method == "POST":
        form = UploadPDFForm(request.POST, request.FILES)

        if form.is_valid():
            arquivo = request.FILES['arquivo']

            leitor = PyPDF2.PdfReader(arquivo)

            for pagina in leitor.pages:
                if pagina.extract_text():
                    texto += pagina.extract_text()

            # 🔊 AGORA SEM LIMITE
            if texto.strip():
                arquivos = gerar_audio_completo(texto)
                audio_url = juntar_audios(arquivos)

    else:
        form = UploadPDFForm()

    return render(request, "upload.html", {
        "form": form,
        "texto": texto,
        "audio_url": audio_url
    })