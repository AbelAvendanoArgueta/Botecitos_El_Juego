# Abel Fernando Avendaño Argueta

import pygame, sys
from boton import Boton
from pygame.locals import *
from parametros_generales import *

#####
# VARIABLES
#####

    ###### 
    # CONSTANTES
    ######



    ###### 
    # NO CONSTANTES
    ######


pygame.init()
# vt = Ventana inicial
vt = pygame.display.set_mode((medidas['ventana_ancho'], medidas['ventana_alto'])) # Se le pasa una variable como parametro para definir tamaño de vt
pygame.display.set_caption("Botecitos 'El juego'") # Se le da una nombre a la ventana

#####
# FUNCIONES
#####

# Importacion de Fuente
def tomar_fuente(fuente_T): # fuente_T = Tamaño de la fuente 
    return pygame.font.Font("./recursos/tipografia/fuente.ttf", fuente_T) # Se importa la fuente, y se pasa la variable "fuente_T" para definir tamaño de la fuente

def main_menu():
    while True:
        vt = pygame.display.set_mode((800,600))
        cur_pos = pygame.mouse.get_pos()    
        fdpi = pygame.image.load("./recursos/imagenes/sec_rio/rio_1.png")
        vt.blit(fdpi, (0, 0))

        # Texto Botecitos en pantalla inicial
        titulo_juego = Boton(image=pygame.image.load("./recursos/imagenes/titulo_pant_inicial.png"), pos=(400, 150), 
                            text_input="", font=tomar_fuente(10), base_color=blanco, hovering_color=blanco)
        

        btn_jugar = Boton(image=pygame.image.load("./recursos/imagenes/boton_vt.png"), pos=(400, 350), 
                            text_input="Jugar", font=tomar_fuente(70), base_color=blanco, hovering_color=amarillo_per)
        btn_salir = Boton(image=pygame.image.load("./recursos/imagenes/boton_vt.png"), pos=(400, 475), 
                            text_input="Salir", font=tomar_fuente(70), base_color=blanco, hovering_color=amarillo_per)
        btn_coders = Boton(image=None, pos=(770, 570), 
                            text_input="❯", font=tomar_fuente(30), base_color=azul_per, hovering_color="Green")
             

        for button in [btn_jugar, btn_salir, btn_coders,titulo_juego]:
            button.changeColor(cur_pos)
            button.update(vt)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_jugar.checkForInput(cur_pos):
                    boton_jugar()
                if btn_salir.checkForInput(cur_pos):
                    pygame.quit()
                    sys.exit()
                if btn_coders.checkForInput(cur_pos):
                    caratula()
                

        pygame.display.update()

def boton_jugar():
    while True: # Se define ciclica la siguiente parte del codigo
        vt = pygame.display.set_mode((medidas['ventana_ancho'], medidas['ventana_alto']))
        cur_pos = pygame.mouse.get_pos()
        fdpmdj = pygame.image.load("./recursos/imagenes/fondo_modo_juego.png")
        vt.blit(fdpmdj, (0, 0))

        ## Texto Jugar
        # jugar_txt = da formato a nuestro texto
        btn_jugar_pve = Boton(image=pygame.image.load("./recursos/imagenes/boton_vt.png"), pos=(290, 435), 
                            text_input="PVE", font=tomar_fuente(70), base_color=blanco, hovering_color="Green")
        btn_jugar_pvp = Boton(image=pygame.image.load("./recursos/imagenes/boton_vt.png"), pos=(965, 215), 
                            text_input="PVP", font=tomar_fuente(70), base_color=blanco, hovering_color="Green")
        
        jtxt_retornar = Boton(image=None, pos=(640, 565), 
                            text_input="retornar", font=tomar_fuente(65), base_color=blanco, hovering_color=rojo)

        for button in [btn_jugar_pve, btn_jugar_pvp]:
            button.changeColor(cur_pos)
            button.update(vt)

        jtxt_retornar.changeColor(cur_pos)
        jtxt_retornar.update(vt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jtxt_retornar.checkForInput(cur_pos):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_jugar_pve.checkForInput(cur_pos):
                    boton_jugar_pve()
                if btn_jugar_pvp.checkForInput(cur_pos):
                    boton_jugar_pvp()
     
        pygame.display.update()

def caratula():
    while True:
        vt = pygame.display.set_mode((medidas['ventana_ancho'], medidas['ventana_alto']))
        cur_pos = pygame.mouse.get_pos()
        fdpmdj = pygame.image.load("./recursos/imagenes/caratula.png")
        vt.blit(fdpmdj, (0, 0))

        # Texto Pruebas

        jtxt_retornar = Boton(image=None, pos=(1150, 620), 
                        text_input="retornar", font=tomar_fuente(30), base_color="Orange", hovering_color="Green")

        for button in [jtxt_retornar]:
                button.changeColor(cur_pos)
                button.update(vt)

        jtxt_retornar.changeColor(cur_pos)
        jtxt_retornar.update(vt)    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jtxt_retornar.checkForInput(cur_pos):
                    main_menu()
        
        pygame.display.update()

def boton_jugar_pve():
    while True: # Se define ciclica la siguiente parte del codigo
        cur_pos = pygame.mouse.get_pos()
        fdpi = pygame.image.load("./recursos/imagenes/fondo_pantalla_inicial.png")
        vt.blit(fdpi, (0, 0))
        
        jtxt_retornar = Boton(image=None, pos=(140, 620), 
                            text_input="retornar", font=tomar_fuente(30), base_color=blanco, hovering_color=rojo)
        
        comenzar_jugar = Boton(image=None, pos=(1050, 620), 
                            text_input="Comenzar Juego", font=tomar_fuente(30), base_color=blanco, hovering_color="Green")

        for button in [jtxt_retornar, comenzar_jugar]:
            button.changeColor(cur_pos)
            button.update(vt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jtxt_retornar.checkForInput(cur_pos):
                    boton_jugar()
                if comenzar_jugar.checkForInput(cur_pos):
                    ventana_pruebas()

        pygame.display.update()

def boton_jugar_pvp():
    while True: # Se define ciclica la siguiente parte del codigo
        cur_pos = pygame.mouse.get_pos()
        fdpmdj = pygame.image.load("./recursos/imagenes/fondo_pantalla_inicial.png")
        vt.blit(fdpmdj, (0, 0))
        
        jtxt_retornar = Boton(image=None, pos=(640, 565), 
                            text_input="retornar", font=tomar_fuente(65), base_color=blanco, hovering_color=rojo)


        jtxt_retornar.changeColor(cur_pos)
        jtxt_retornar.update(vt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jtxt_retornar.checkForInput(cur_pos):
                    boton_jugar()   
        pygame.display.update()

def ventana_pruebas():
    while True:
        vt.fill(naranja)
        # Texto Pruebas
        cur_pos = pygame.mouse.get_pos()
        botecitos_txt = tomar_fuente(75).render("Pruebas", True, "#eb606b")
        botecitos_xy = botecitos_txt.get_rect(center=(640, 100))
        vt.blit(botecitos_txt, botecitos_xy)

        jtxt_retornar = Boton(image=None, pos=(140, 620), 
                        text_input="retornar", font=tomar_fuente(30), base_color=blanco, hovering_color=rojo)
        
        #
        
        #

        for button in [jtxt_retornar]:
                button.changeColor(cur_pos)
                button.update(vt)

        jtxt_retornar.changeColor(cur_pos)
        jtxt_retornar.update(vt)    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jtxt_retornar.checkForInput(cur_pos):
                    main_menu()
        
        pygame.display.update()

if __name__ == "__main__":
    main_menu()