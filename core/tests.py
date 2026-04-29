from pydub import AudioSegment

audio = AudioSegment.silent(duration=1000)  # 1 segundo
audio.export("teste.mp3", format="mp3")