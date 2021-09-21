# pip install spotipy
# pip install pyautogui


from os import name
from sys import _OptExcInfo
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser as web
import pyautogui
from time import sleep

from Reconocimiento_voz import Reconocimiento

from TTS import tts




client_id = 
client_secret = 


def Play_musica():

    tts("¿cual es el nombre del autor?")
    author = Reconocimiento()
    author = " ".join(author)                                                                      #convierto la lista de entrada en un str
    
    
    tts("¿cual es el nombre de la canción?")
    song = Reconocimiento()
    song = " ".join(song) 
    

    flag = 0

    author = author.capitalize()

    song = song.upper()                                                                                                                                   # upper() es para que siempre la primer letra este en mayuscula




    if len(author) > 0:

        print(author)
        print(song)

        print("entro1")

        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
       
        result = sp.search(author)  


        for i in range(0, len(result["tracks"]["items"])):                                                                                                            #itera para traer un conteo total de los items

            name_song = result["tracks"]["items"][i]["name"].upper()

            if song ==  name_song:

                flag = 1

                web.open(result["tracks"]["items"][i]["uri"])
                
                break

                


    # if song by artist not found
    if flag == 0:
        
        tts("No se encontro la cancion solocitada, si desea escuchar la lista de temas de este author diga si")
        opcion = Reconocimiento()

        if opcion == "si" or opcion == "Si":
            tts("estas son las canciones de {}".format(author))

            for i in range(0, len(result["tracks"]["items"])):                                                                                                            #itera para traer un conteo total de los items
               name_song = result["tracks"]["items"][i]["name"].upper()
               tts(name_song)

        else:
            tts("okey")
            
    

        

def Play_Pause():

    web.open('spotify')

    pyautogui.press("tab")  

    sleep(3)

    pyautogui.press(" ")                                    # apreta spacebar para que de play 

