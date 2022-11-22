# Abel Fernando Avendaño Argueta

import sys
import pygame
from boton import Boton
from pygame.locals import *
#abel: el lic se nos va morir.
#1

# los tres estamos trabajando en Github como unos campeones

#####
# VARIABLES
#####

    ###### 
    # CONSTANTES
    ######

pant_alt = 650 # pant_alt = pantalla_altura
pant_anc = 1280 # pant_anc = pantalla_ancho

    ###### 
    # NO CONSTANTES
    ######


pygame.init()
# vt = Ventana inicial
vt = pygame.display.set_mode((pant_anc, pant_alt)) # Se le pasa una variable como parametro para definir tamaño de vt
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
        botecitos_txt = tomar_fuente(75).render("BOTECITOS", True, "#eb606b")
        botecitos_xy = botecitos_txt.get_rect(center=(640, 100))
        vt.blit(botecitos_txt, botecitos_xy)

        eljogo_txt = tomar_fuente(75).render("'El Juego'", True, "#eb606b")
        eljogo_xy = eljogo_txt.get_rect(center=(640, 200))
        vt.blit(eljogo_txt, eljogo_xy)

        btn_jugar = Boton(image=pygame.image.load("./recursos/imagenes/boton_vt.png"), pos=(640, 350), 
                            text_input="Jugar", font=tomar_fuente(70), base_color="White", hovering_color="#f7eb95")
        btn_salir = Boton(image=pygame.image.load("./recursos/imagenes/boton_vt.png"), pos=(640, 475), 
                            text_input="Salir", font=tomar_fuente(70), base_color="White", hovering_color="#f7eb95")
        btn_coders = Boton(image=None, pos=(1250, 620), 
                            text_input="❯", font=tomar_fuente(30), base_color="#3daee9", hovering_color="Green")
             

        for button in [btn_jugar, btn_salir, btn_coders]:
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
        vt = pygame.display.set_mode((pant_anc, pant_alt))
        cur_pos = pygame.mouse.get_pos()
        fdpmdj = pygame.image.load("./recursos/imagenes/fondo_modo_juego.png")
        vt.blit(fdpmdj, (0, 0))

        ## Texto Jugar
        # jugar_txt = da formato a nuestro texto
        btn_jugar_pve = Boton(image=pygame.image.load("./recursos/imagenes/boton_vt.png"), pos=(290, 435), 
                            text_input="PVE", font=tomar_fuente(70), base_color="White", hovering_color="Green")
        btn_jugar_pvp = Boton(image=pygame.image.load("./recursos/imagenes/boton_vt.png"), pos=(965, 215), 
                            text_input="PVP", font=tomar_fuente(70), base_color="White", hovering_color="Green")
        
        jtxt_retornar = Boton(image=None, pos=(640, 565), 
                            text_input="retornar", font=tomar_fuente(65), base_color="White", hovering_color="Red")

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
                            text_input="retornar", font=tomar_fuente(30), base_color="White", hovering_color="Red")
        
        comenzar_jugar = Boton(image=None, pos=(1050, 620), 
                            text_input="Comenzar Juego", font=tomar_fuente(30), base_color="White", hovering_color="Green")

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
                            text_input="retornar", font=tomar_fuente(65), base_color="White", hovering_color="Red")

        #for button in [btn_jugar_pve, btn_jugar_pvp]:
        #    button.changeColor(cur_pos)
        #   button.update(vt)

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
        vt.fill("orange")
        # Texto Pruebas
        cur_pos = pygame.mouse.get_pos()
        botecitos_txt = tomar_fuente(75).render("Pruebas", True, "#eb606b")
        botecitos_xy = botecitos_txt.get_rect(center=(640, 100))
        vt.blit(botecitos_txt, botecitos_xy)

        jtxt_retornar = Boton(image=None, pos=(140, 620), 
                        text_input="retornar", font=tomar_fuente(30), base_color="White", hovering_color="Red")
        
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