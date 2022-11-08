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
    pygame.display.flip() # se muestran lo cambios en pantalla
    
    #boton

    manager = pygame_gui.UIManager((800,600))
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350,275),(100,50)),
                                             text='Say Hello',
                                             manager=manager)

                            


    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()