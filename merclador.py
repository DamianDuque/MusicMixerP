from pydub import AudioSegment
import os
#from os import mkdir

#eCarpeta = os.path.isdir("Pistas")
#nombre_carpeta = "Pistas"
#if eCarpeta == False:
#    mkdir(nombre_carpeta)

#ruta = os.path.abspath(nombre_carpeta)
#print(ruta)

pista1 = AudioSegment.from_file("Pistas//Hades.mp3", format="mp3")
print(pista1)
pista2 = AudioSegment.from_file("Pistas//HellsParadise.mp3", format="mp3")
print(pista2)

# Ajustar la frecuencia de muestreo y la resolución de bits de las pistas
#pista1 = pista1.set_frame_rate(44100).set_sample_width(2)
#pista2 = pista2.set_frame_rate(44100).set_sample_width(2)

# Mezclar las pistas
mezcla = pista1.overlay(pista2)

#Exportar la mezcla
mezcla.export("Mezcla.mp3", format='mp3')

