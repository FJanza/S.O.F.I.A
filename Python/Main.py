#------------------------------LIBRERIAS--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from Reconocimiento_voz import Reconocimiento

from TTS import tts

from Buscar_info import Buscar_info

from Musica import Play_musica

from Musica import Play_Pause

#-------------------------------MAIN-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def main():

    opcion = Reconocimiento()

    #print (opcion)

    if opcion:

        if(opcion[0] == "Sofía"):                                                                                                                                              #reconoce la palabra comando Sofía 
            
            if(opcion[1] == "buscar" or opcion[1] == "Buscar"):

                opcion.pop(0)                                                                                                                                                   #elimina Sofía de la lista
                opcion.pop(0)                                                                                                                                                   #elimina buscar/Buscar de la lista

                #print(Buscar_info(opcion))

                tts("Buscando la informacion")                                                                                                                                  #avisa que va a buscar la informacion
                tts(Buscar_info(opcion))                                                                                                                                        #responde con la informacion solicitada


            elif(opcion[1] == "buenos" or opcion[1] == "Buenos") and (opcion[2] == "días" or opcion[2] == "Días"):
                tts("Buenos dias Janza")
                
            
            elif(opcion[1] == "mostrar" or opcion[1] == "Mostrar"):
                print("2")
                pass
            
            elif((opcion[1] == "Estado" or opcion[1] == "estado") and (opcion[2] == "del" or opcion[2] == "Del") and (opcion[3] == "Sistema" or opcion[3] == "sistema")):
                print("3")
                pass

            elif(opcion[1] == "analiza" or opcion[1] == "Analiza" or opcion[1] == "analizar" or opcion[1] == "Analizar"):
                print("4")
                pass

            elif(opcion[1] == "hora" or opcion[1] == "Hora"):
                print("5")
                pass

            elif(opcion[1] == "play" or opcion[1] == "Play"):

                 Play_musica()
                
            
            elif(opcion[1] == "pausa" or opcion[1] == "Pausa"):
              
                Play_Pause()
            

        
        elif(opcion[0] == 'Rocket' and opcion[1] == 'League'):                                                                                                                    #comando de salida Rocket League CAMBIAR COMANDO A UNO MAS SENCILLO
            print("rocket league")
            pass

        else:                                                                                                                                                                     #error de comando
            print("sin comando")
            pass    
    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

