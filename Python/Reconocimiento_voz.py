import speech_recognition as sr



#-------------------------RECONOCIMIENTO-DE-VOZ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def Reconocimiento() -> list :


    r = sr.Recognizer()



    with sr.Microphone() as source:

        print("Escuchando")
        
        audio_data = r.listen(source)                                                            #Lee el auido del microfono

        

                                                                 
        texto = r.recognize_google(audio_data, language="es-AR")                                 #Convierte el audio en texto
        
       

        texto_lista = texto.split(' ')

        

        if( texto_lista[0] == 'Sofía'):                                                          #Reconoce como palabra clave Sofía


            print("Procesando...")


            return(texto_lista)                                                                        #Muestra por terminal lo escuchado
        
        elif( texto_lista[0] == 'Rocket' and texto_lista[1] == 'League'):                        #Reconoce como combinacion de escape Rocket League gracias Ernesto <3
            
            salida = ["out"]

            return(salida)

        else:
            pass




