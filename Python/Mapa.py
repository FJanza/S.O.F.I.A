import requests     #para poder conectarnos con la api 
import urllib       #para poder manejar mejor las urls

api_url = "http://www.mapquestapi.com/directions/v2/route?"

key = "DXOzV2WjMEodSemHC1AvVDwjiGMhpNqH"

while True:

    origin = "Buenos Aires"

    destination = "Mendoza"

    """
    origin = input("ingrese el origen: ")
    if origin == 'q':
        break
    destination = input("ingrese el destino: ")
    if destination == 'q':
        break

    """


    url = api_url + urllib.parse.urlencode({"key":key,"from":origin,"to":destination,"unit":"K","destinationManeuverDisplay":True,"locale":"es_MX"})
    json_data = requests.get(url).json()
    
    status_code = json_data["info"]["statuscode"]

    if status_code == 0:
        
        duracion_viaje = json_data["route"]["formattedTime"]
        largo_viaje = json_data["route"]["distance"]

        indicaciones = []
        
        indicaciones.append(json_data["route"]["legs"][0]["origNarrative"])


        for each in json_data["route"]["legs"][0]["maneuvers"]:
            
            
            indicaciones.append((each["distance"],each["narrative"]))  #guardo en cuantos km flatan para tal accion ej en 1km girar a la derecha

        print(indicaciones[1][1])

    break