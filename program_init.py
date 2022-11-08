import pygame
from pygame.locals import *
import sys

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

#####
# FUNCIONES
#####

def main():
    pygame.init()
    Ventana_inicial = pygame.display.set_mode((pantalla_ancho, pantalla_largo))
    pygame.display.set_caption("Botecitos 'El juego'") 

    fondo_de_pantalla_inicial = pygame.image.load("./recursos/imagenes/fondo_pantalla_inicial.png").convert_alpha()

    Ventana_inicial.blit(fondo_de_pantalla_inicial, (0, -100))
    # se muestran lo cambios en pantalla
    pygame.display.flip()
    

    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()