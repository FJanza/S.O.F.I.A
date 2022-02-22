from pygame import init
import requests     #para poder conectarnos con la api 
import urllib       #para poder manejar mejor las urls

from Reconocimiento_voz import Reconocimiento

from TTS import tts

def Mapa(origin,destination):
    api_url = "http://www.mapquestapi.com/directions/v2/route?"

    key = "DXOzV2WjMEodSemHC1AvVDwjiGMhpNqH"

    url = api_url + urllib.parse.urlencode({"key":key,"from":origin,"to":destination,"unit":"K","destinationManeuverDisplay":True,"locale":"es_MX"})
    json_data = requests.get(url).json()

    status_code = json_data["info"]["statuscode"]

    if status_code == 0:
        
        duracion_viaje = json_data["route"]["formattedTime"]

        largo_viaje = json_data["route"]["distance"]

        indicaciones_data = []
        
        indicaciones_data.append(json_data["route"]["legs"][0]["origNarrative"])


        for each in json_data["route"]["legs"][0]["maneuvers"]:
            
            
            indicaciones_data.append((each["distance"],each["narrative"]))  #guardo en cuantos km flatan para tal accion ej en 1km girar a la derecha

        
        indicaciones = ""

        indicaciones = indicaciones + indicaciones_data[0]

        for i in range(1,len(indicaciones_data)):
            if indicaciones_data[i][0] < 1:
                indicaciones = indicaciones+ "En " + str(indicaciones_data[i][0]*100) + " metros " + indicaciones_data[i][1] + " "
            else:
                indicaciones = indicaciones+ "En " + str(indicaciones_data[i][0]) + " Km " + indicaciones_data[i][1] + " " 

        info = []

        info.append(origin)
        info.append(destination)
        info.append(indicaciones)
        info.append(duracion_viaje)
        info.append(largo_viaje)

        return(info)

    else:
        print("status code error")
        return

def Mapa_bot():

    tts("Decime la ubicacion de origen")

    origen = Reconocimiento()
    origen = " ".join(origen)
    

    tts("muy bien, ahora decime el lugar de destino")

    destino = Reconocimiento()
    destino = " ".join(destino)
    

    info = Mapa(origen,destino)

    texto = ""
    texto = texto + "EL viaje desde " + info[0] + " " + "a " + info[1] + " " + "tiene una duracion estimada de " + str(info[3]) + " " +"con un total de " + str(info[4]) + "km " + "Las indicaciones son las siguientes: " + info[2]

    tts("¿quieres que imprima las indicaciones?")
    respuesta = Reconocimiento()
    

    if respuesta[0] == "sí" or respuesta[0] == "Sí":
        print(texto)

    else:
        tts("Entonces te lo dicto")
        tts(texto)
    
    
