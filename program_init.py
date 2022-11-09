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
pant_alt = 550 # pant_alt = pantalla_altura
pant_anc = 1440 # pant_anc = pantalla_ancho

    ###### 
    # NO CONSTANTES
    ######

#####
# FUNCIONES
#####

pygame.init()
# vt = Ventana inicial
VT = pygame.display.set_mode((pant_anc, pant_alt))
pygame.display.set_caption("Botecitos 'El juego'") 


# fdpi = fondo de pantalla inicial
fdpi = pygame.image.load("./recursos/imagenes/fondo_pantalla_inicial.png").convert_alpha()

VT.blit(fdpi, (0, -100))
pygame.display.flip() # se muestran lo cambios en pantalla

# Codigo para cerrar la ventana                                                    
while 1 == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# Importacion de Fuente
def get_font(fuente_T): # fuente_T = Tamaño de la fuente 
    return pygame.font.Font("./recursos/Tipografia/font.ttf", fuente_T)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        VT.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        VT.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Boton(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(VT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        VT.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        VT.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Boton(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(VT)

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
        VT.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Boton(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Boton(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Boton(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        VT.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(VT)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
