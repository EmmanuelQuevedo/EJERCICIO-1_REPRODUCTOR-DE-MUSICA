from tkinter import *
import pygame, sys
from pygame.locals import*
from tkinter import filedialog
from PIL import ImageTk, Image
import os 

pygame.init() #Iniciamos modulo de pygame

#Funcion boton abrir cancion 

def abrirArchivo():
    cancion= filedialog.askopenfilename() #Guardar el nombre o cancion que queremos reproducir
    print(cancion)
    pygame.mixer.music.load(cancion)
    

def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def pauseSong():
    pygame.mixer.music.pause()

def resumeSong():
    pygame.mixer.music.unpause()

def volumenUp():
    volumenLevel = pygame.mixer.music.get_volume() + 0.5
    print(volumenLevel)
    pygame.mixer.music.set_volume

def volumenDown():
    volumenLevel = pygame.mixer.music.get_volume() - 0.5
    print(volumenLevel)
    pygame.mixer.music.set_volume



raiz = Tk()
raiz.title("Reproductor MP3-GUI")
raiz.iconbitmap("auriculares.ico")
#flaticon.com    descargar en png
#convertir png a ico

raiz.geometry("800x500")
raiz.resizable(0,0)

#Crear frame 

framePrincipal = Frame(raiz, bg="#4a4a4a")
framePrincipal.pack(fill="both", expand=1)


#Titulo Reproductor
tituloReproductor = Label(framePrincipal, text="Reproductor MP3-GUI", font=("Roboto", 30, "bold"), bg="#4a4a4a", fg="#fbfbfb")
tituloReproductor.place(relx=0.25, rely=0.4)


#Boton Open song
botonOpensong= Button(framePrincipal, text="Open song", bg="#42ab49", fg="#fbfbfb", font=("Roboto", 12, "bold"), width=10, height=2, command=abrirArchivo)
botonOpensong.place(relx=0.1, rely=0.6)

#Boton Play Song
botonPlaysong= Button(framePrincipal, text="Play", bg="#42ab49", fg="#150D0B", font=("Roboto", 12, "bold"), width=10, height=2, command=playSong)
botonPlaysong.place(relx=0.25, rely=0.6)

#Boton Stop song

botonStopsong= Button(framePrincipal, text="Stop", bg="#42ab49", fg="#e2504c", font=("Roboto", 12, "bold"), width=10, height=2, command=stopSong)
botonStopsong.place(relx=0.4, rely=0.6)

#Boton Resume

botonResumesong= Button(framePrincipal, text="Resume", bg="#42ab49", fg="#ffc400", font=("Roboto", 12, "bold"), width=10, height=2, command=resumeSong)
botonResumesong.place(relx=0.55, rely=0.6)

#Boton Pause 

botonPausesong= Button(framePrincipal, text="Pause", bg="#42ab49", fg="#550099", font=("Roboto", 12, "bold"), width=10, height=2, command=pauseSong)
botonPausesong.place(relx=0.7, rely=0.6)


#Boton volumen +
botonvolumenMas= Button(framePrincipal, text="Volumen: +", bg="#42ab49", fg="#150D0B", font=("Roboto", 12, "bold"), width=10, height=2,command=volumenUp)
botonvolumenMas.place(relx=0.55, rely=0.8)

#Boton volumen -
botonvolumenMenos= Button(framePrincipal, text="Volumen: -", bg="#42ab49", fg="#150D0B", font=("Roboto", 12, "bold"), width=10, height=2, command=volumenDown)
botonvolumenMenos.place(relx=0.25, rely=0.8)



raiz.mainloop()