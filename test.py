from pydub import AudioSegment
import os

directorio = "C:\\Users\\ilope\\OneDrive - Universidad de Medellin\\Desktop\\EAFIT\\Quinto_semestre\\Organizacion de computadores\\ParcialFinal\\Pistas"
archivos = os.listdir(directorio)
print(archivos)
pista1 = AudioSegment.from_mp3(directorio, 'Hades.mp3')
pista2 = AudioSegment.from_mp3(directorio, 'Hades-Soundtrack')

#mezcla = pista1.overlay(pista2)

#mezcla.export(os.path.join(directorio, "mezcla.mp3"), format="mp3")