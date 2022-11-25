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

def imprimir_tablero(tablero_de_juego):
    cruzando_tablero = atravezar_tablero(tablero_de_juego)
    for fila in cruzando_tablero:
        print(fila)

def d_cuadricula_dTabs(Coordenadas_en_X0, Coordenadas_en_Y0): 
    # Dibujo de Cuadricula de los tableros
    pygame.draw.rect(vt, blanco,
                     (Coordenadas_en_X0, Coordenadas_en_Y0,
                      lado*medidas['lado_cuadrado'], lado*medidas['lado_cuadrado']))
    # Lineas horizontales
    for j in range(0,lado+1):
        pygame.draw.line(vt, negro,
                         (Coordenadas_en_X0, Coordenadas_en_Y0 + medidas['lado_cuadrado']*j),
                         (Coordenadas_en_X0 + medidas['lado_cuadrado']*lado, Coordenadas_en_Y0 +medidas['lado_cuadrado']*j), 1)
    # Letras en las filas
    for j in range(0,lado):
        letra = tomar_fuente(20).render(letras[j], True, negro)
        vt.blit(letra, (Coordenadas_en_X0-medidas['lado_cuadrado'], Coordenadas_en_Y0 + medidas['lado_cuadrado']*j))

    # Lineas verticales
    for j in range(0,lado+1):
        pygame.draw.line(vt, negro,
                         (Coordenadas_en_X0 + medidas['lado_cuadrado']*j, Coordenadas_en_Y0),
                         (Coordenadas_en_X0 + medidas['lado_cuadrado']*j, Coordenadas_en_Y0 +medidas['lado_cuadrado']*lado), 1)

    # Numeros en las columnas
    for j in range(0,lado):
        letra = tomar_fuente(20).render(str(j+1), True, negro)
        vt.blit(letra, (Coordenadas_en_X0 + medidas['lado_cuadrado']*j + (medidas['lado_cuadrado'] - medidas['tamaño_letra']), Coordenadas_en_Y0 +medidas['lado_cuadrado']*lado))