import pygame
from pygame.locals import *

#####
# VARIABLES
#####

    ###### 
    # CONSTANTES
    ######
pantalla_largo = 500
pantalla_ancho = 700

    ###### 
    # NO CONSTANTES
    ######


def main():
    pygame.init()
    screen = pygame.display.set_mode((pantalla_ancho, pantalla_largo))
    pygame.display.set_caption("Botecitos 'El juego'")