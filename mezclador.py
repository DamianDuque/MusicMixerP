from multiprocessing import Process, Manager
from pydub import AudioSegment
import mezclador_aux as aux


#Funcion a ejecutar en un nuevo proceso 
def MezcladorDeSonido(estado_proceso, track1, track2):
    try:
        #Cargar Pista 1track1, track2
        pista1 = AudioSegment.from_file(track1, format="mp3")
        print(pista1)

        #Cargar Pista 2
        pista2 = AudioSegment.from_file(track2, format="mp3")
        print(pista2)


        # Determinar cual es la pista con mayor duracion
        if len(pista1) > len(pista2):

            # Mezclar las pistas
            mezcla = pista1.overlay(pista2)
        else:
            mezcla = pista2.overlay(pista1)
        
        # Generar id unico para cada mezcla
        id_mezcla = aux.generarId()

        #Exportar la mezcla
        mezcla.export("Mezclas//" + str(id_mezcla) + ".mp3", format='mp3')

        # Actualizar el estado del proceso reportando que termino OK
        estado_proceso.value = 0

        
    except Exception as e:
        print(f"Error en el proceso {e}")

        # Actualizar el estado del proceso reportando que termino con errores
        estado_proceso.value = 1


#Flujo principal
def main(track1, track2):

    # Crear un objeto Manager para compartir el estado de salida del proceso
    manager = Manager()
    estado_proceso = manager.Value('i', -1)  # Valor inicial -1 indica que el proceso aún no ha terminado

    # crear un nuevo proceso
    process = Process(target=MezcladorDeSonido, args=(estado_proceso, track1, track2))


    # ejecutar el proceso
    process.start()

    # Esperar a la ejecucion del proceso
    print('Realizando mezcla...')
    process.join()

    estado_proceso_final = estado_proceso.value
    
    if estado_proceso_final == 0:
        print("El proceso terminó adecuadamente.")
        
    elif estado_proceso_final == 1:
        print("El proceso terminó con errores.")
        
    else:
        print("El estado de salida del proceso es desconocido.")

if __name__ == "__main__":
    main("Pistas//HellsParadise.mp3", "Pistas//Hades.mp3")