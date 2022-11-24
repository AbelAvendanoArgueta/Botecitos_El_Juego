import pygame, sys
from pygame.locals import *
from random import *
from time import *
from src_parametros_generales import *
from program_init import boton_jugar_pve

vt = pygame.display.set_mode((medidas['ventana_ancho'], medidas['ventana_alto']))
reloj = pygame.time.Clock()

def tomar_fuente(fuente_T): # fuente_T = Tamaño de la fuente 
    return pygame.font.Font(import_fuente, fuente_T) # Se importa la fuente, y se pasa la variable "fuente_T" para definir tamaño de la fuente
### Dibujo, trazado y analisis de tableros
def atravezar_tablero(tablero_de_juego):
    cruzando_tablero = [[' ']*lado for _ in range(lado)]
    for i in range(lado):
        for j in range(lado):
            cruzando_tablero[i][j] = tablero_de_juego[j][i]
    return cruzando_tablero