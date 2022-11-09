import pygame
import pygame_gui
from pygame.locals import *
import sys

#####
# VARIABLES
#####

    ###### 
    # CONSTANTES
    ######
pantalla_altura = 550
pantalla_ancho = 1440

    ###### 
    # NO CONSTANTES
    ######

#####
# FUNCIONES
#####


pygame.init()
Ventana_inicial = pygame.display.set_mode((pantalla_ancho, pantalla_altura))
pygame.display.set_caption("Botecitos 'El juego'") 

fondo_de_pantalla_inicial = pygame.image.load("./recursos/imagenes/fondo_pantalla_inicial.png").convert_alpha()

Ventana_inicial.blit(fondo_de_pantalla_inicial, (0, -100))
pygame.display.flip() # se muestran lo cambios en pantalla

# Codigo para cerrar la ventana                                                    
while 1 == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# Importacion de Fuente
def get_font(fuente_T): # fuente_T = Tamaño de la fuente 
    return pygame.font.Font("./recursos/Tipografia/font.ttf", fuente_T)
