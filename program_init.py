import pygame
from pygame.locals import *
from boton import Boton
import sys

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


# fdpi = fondo de pantalla inicial en vt
fdpi = pygame.image.load("./recursos/imagenes/fondo_pantalla_inicial.png").convert_alpha()

#####
# FUNCIONES
#####

# Importacion de Fuente
def tomar_fuente(fuente_T): # fuente_T = Tamaño de la fuente 
    return pygame.font.Font("./recursos/tipografia/fuente.ttf", fuente_T) # Se importa la fuente, y se pasa la variable "fuente_T" para definir tamaño de la fuente

def jugar():
    while True: # Se define ciclica la siguiente parte del codigo
        # cur_pos = posición del cursor
        cur_pos = pygame.mouse.get_pos() # obtener la posición del cursor del mouse

        # funcion fill no ayudara a cambiar el color de la pantalla luego que demos click en alguna función
        color_opc = (94, 126, 181) # color_opc sera el que se usara luego de dar click en una opcion
        vt.fill(color_opc) # se pasa color_opc como parametro
        
        ## Texto Jugar
        # jugar_txt = da formato a nuestro texto
        jugar_txt = tomar_fuente(45).render("Esta es la pantalla JUGAR.", True, "White")
        # jugar_rect = se dan coordenadas de donde el texto debe ir ubicado
        jugar_rect = jugar_txt.get_rect(center=(640, 260))
        vt.blit(jugar_txt, jugar_rect) # Dibujar en una imagen sobre otra

        jtxt_retornar = Boton(image=None, pos=(640, 460), 
                            text_input="Retornar", font=tomar_fuente(75), base_color="White", hovering_color="Green")

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
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        vt.fill("white")

        OPTIONS_TEXT = tomar_fuente(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        vt.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Boton(image=None, pos=(640, 460), 
                            text_input="BACK", font=tomar_fuente(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(vt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        vt.blit(fdpi, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = tomar_fuente(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Boton(image=pygame.image.load("./recursos/imagenes/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=tomar_fuente(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Boton(image=pygame.image.load("./recursos/imagenes/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=tomar_fuente(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Boton(image=pygame.image.load("./recursos/imagenes/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=tomar_fuente(75), base_color="#d7fcd4", hovering_color="White")

        vt.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(vt)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    jugar()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
