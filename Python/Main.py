#------------------------------LIBRERIAS--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from Reconocimiento_voz import Reconocimiento

from TTS import tts

#-------------------------------MAIN-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def main():

    opcion = Reconocimiento()

    #print (opcion)

    if opcion:

        if(opcion[0] == "Sofía"):                                                                                                                                              #reconoce la palabra comando Sofía 
            
            if(opcion[1] == "buscar" or opcion[1] == "Buscar"):
                print("1")
                tts("Buscando la informacion")
                pass

            elif(opcion[1] == "mostrar" or opcion[1] == "Mostrar"):
                print("2")
                pass
            
            elif((opcion[1] == "Estado" or opcion[1] == "estado") and (opcion[2] == "del" or opcion[2] == "Del") and (opcion[3] == "Sistema" or opcion[2] == "sistema")):
                print("3")
                pass

            elif(opcion[1] == "analiza" or opcion[1] == "Analiza" or opcion[1] == "analizar" or opcion[1] == "Analizar"):
                print("4")
                pass

            elif(opcion[1] == "hora" or opcion[1] == "Hora"):
                print("5")
                pass

            elif(opcion[1] == "play" or opcion[1] == "Play"):
                print("6")
                pass
        
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

