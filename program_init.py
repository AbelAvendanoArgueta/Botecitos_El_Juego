import sys
import pygame
from boton import Boton
from pygame.locals import *

#####
# VARIABLES
#####

    ###### 
    # CONSTANTES
    ######

pant_alt = 650 # pant_alt = pantalla_altura
pant_anc = 1280 # pant_anc = pantalla_ancho

    ###### 
    # NO CONSTANTES hola soy rama de pruebas
    ######


pygame.init()
# vt = Ventana inicial
vt = pygame.display.set_mode((pant_anc, pant_alt)) # Se le pasa una variable como parametro para definir tamaño de vt
pygame.display.set_caption("Botecitos 'El juego'") # Se le da una nombre a la ventana


# fdpi = fondo de pantalla inicial en vt
fdpi = pygame.image.load("./recursos/imagenes/fondo_pantalla_inicial.png").convert_alpha()

#####
# FUNCIONES
#####

# Importacion de Fuente
def tomar_fuente(fuente_T): # fuente_T = Tamaño de la fuente 
    return pygame.font.Font("./recursos/tipografia/fuente.ttf", fuente_T) # Se importa la fuente, y se pasa la variable "fuente_T" para definir tamaño de la fuente

def main_menu():
    while True:
        vt.blit(fdpi, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

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
                            

        for button in [btn_jugar, btn_salir]:
            button.changeColor(menu_mouse_pos)
            button.update(vt)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_jugar.checkForInput(menu_mouse_pos):
                    boton_jugar()
                if btn_salir.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def boton_jugar():
    while True: # Se define ciclica la siguiente parte del codigo
        # cur_pos = posición del cursor
        cur_pos = pygame.mouse.get_pos() # obtener la posición del cursor del mouse

        # funcion fill no ayudara a cambiar el color de la pantalla luego que demos click en alguna función
        # color_opc = (94, 126, 181) # color_opc sera el que se usara luego de dar click en una opcion
        # vt.fill(color_opc) # se pasa color_opc como parametro
        # fdpmdj = fondo de pantalla de ventana modo de juego
        fdpmdj = pygame.image.load("./recursos/imagenes/fondo_modo_juego.png")
        vt.blit(fdpmdj, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        ## Texto Jugar
        # jugar_txt = da formato a nuestro texto
        btn_jugar_pve = Boton(image=pygame.image.load("./recursos/imagenes/boton_vt.png"), pos=(290, 435), 
                            text_input="PVE", font=tomar_fuente(70), base_color="White", hovering_color="Green")
        btn_jugar_pvp = Boton(image=pygame.image.load("./recursos/imagenes/boton_vt.png"), pos=(965, 215), 
                            text_input="PVP", font=tomar_fuente(70), base_color="White", hovering_color="Green")
        
        jtxt_retornar = Boton(image=None, pos=(640, 565), 
                            text_input="retornar", font=tomar_fuente(65), base_color="White", hovering_color="Red")

        for button in [btn_jugar_pve, btn_jugar_pvp]:
            button.changeColor(menu_mouse_pos)
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
                if btn_jugar_pve.checkForInput(menu_mouse_pos):
                    boton_jugar_pve()
                if btn_jugar_pvp.checkForInput(menu_mouse_pos):
                    boton_jugar_pvp()
     
        pygame.display.update()

def boton_jugar_pve():
    while True: # Se define ciclica la siguiente parte del codigo
        # cur_pos = posición del cursor
        cur_pos = pygame.mouse.get_pos() # obtener la posición del cursor del mouse

        # funcion fill no ayudara a cambiar el color de la pantalla luego que demos click en alguna función
        # color_opc = (94, 126, 181) # color_opc sera el que se usara luego de dar click en una opcion
        # vt.fill(color_opc) # se pasa color_opc como parametro
        # fdpmdj = fondo de pantalla de ventana modo de juego
        fdpmdj = pygame.image.load("./recursos/imagenes/fondo_pantalla_inicial.png")
        vt.blit(fdpmdj, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()
        
        jtxt_retornar = Boton(image=None, pos=(640, 565), 
                            text_input="retornar", font=tomar_fuente(65), base_color="White", hovering_color="Red")

        #for button in [btn_jugar_pve, btn_jugar_pvp]:
        #    button.changeColor(menu_mouse_pos)
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

def boton_jugar_pvp():
    while True: # Se define ciclica la siguiente parte del codigo
        # cur_pos = posición del cursor
        cur_pos = pygame.mouse.get_pos() # obtener la posición del cursor del mouse

        # funcion fill no ayudara a cambiar el color de la pantalla luego que demos click en alguna función
        # color_opc = (94, 126, 181) # color_opc sera el que se usara luego de dar click en una opcion
        # vt.fill(color_opc) # se pasa color_opc como parametro
        # fdpmdj = fondo de pantalla de ventana modo de juego
        fdpmdj = pygame.image.load("./recursos/imagenes/fondo_pantalla_inicial.png")
        vt.blit(fdpmdj, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()
        
        jtxt_retornar = Boton(image=None, pos=(640, 565), 
                            text_input="retornar", font=tomar_fuente(65), base_color="White", hovering_color="Red")

        #for button in [btn_jugar_pve, btn_jugar_pvp]:
        #    button.changeColor(menu_mouse_pos)
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


if __name__ == "__main__":
    main_menu()