from importlib.resources import path
from pytube import YouTube
import moviepy.editor as mp
import os
import re


# digite o link do video e o local onde será salvo o video em mp3 #
link = input("Digite o link do video que deseja baixar: ")
path = input("Digite o local onde deseja salvar o video: ")
yt = YouTube(link)

# baixa o video #
print("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download completo!")

#Converte de mp3 para mp4#
print("Convertendo...")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        new_file.close()
        os.remove(mp4_path)
print("Conversão completa!")
