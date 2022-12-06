#BOTECITOS: El Juego
#Contributors
# Misael Estuardo Gonzalez Gonzales (ElMisaaa)
# Rene Alejandro Osorio Natareno (RidiConHuracanes)
# Abel Fernando Avendano Argueta (AbelAvendanoArgueta)

#*--Importacion de librerias / clases / funciones--*
import pygame, sys
from pygame.locals import *
from recursos.codigo.src_boton import *
from recursos.codigo.src_parametros_generales import *
from recursos.codigo.src_pve_logic import *
from recursos.codigo.src_pvp_logic import *

#*--Inicio programa--*
pygame.init()

# vt = Ventana inicial (Se le pasa una variable como parametro para definir tamano de vt)
vt = pygame.display.set_mode((medidas['ventana_ancho'], medidas['ventana_alto'])) 
# Se le da un titulo o nombre a la ventana
pygame.display.set_caption("Botecitos 'El juego'") 

# FUNCIONES

#Funcion sobre Texto
# Importacion de Fuente
def tomar_fuente(fuente_T): # fuente_T = Tamaño de la fuente 
    return pygame.font.Font(import_fuente, fuente_T) # Se importa la fuente, y se pasa la variable "fuente_T" para definir tamano de la fuente

#Funcion sobre el menú
def main_menu():
    while True:
        vt = pygame.display.set_mode((800,600))
        cur_pos = pygame.mouse.get_pos()    
        fdpi = pygame.image.load(imagen_menu_inicial)
        vt.blit(fdpi, (0, 0))

        # Texto Botecitos en pantalla inicial
        titulo_juego = Boton(image=pygame.image.load(imagen_botecitos_titulos), pos=(400, 150), 
                            text_input="", font=tomar_fuente(10), base_color=blanco, hovering_color=blanco)
        
        #Botones del menú principal
        btn_jugar = Boton(image=pygame.image.load(imagen_boton), pos=(400, 350), 
                            text_input="Jugar", font=tomar_fuente(70), base_color=blanco, hovering_color=amarillo) #Boton "JUGAR" 
        btn_salir = Boton(image=pygame.image.load(imagen_boton), pos=(400, 475), 
                            text_input="Salir", font=tomar_fuente(70), base_color=blanco, hovering_color=amarillo) #Boton "SALIR"
        btn_coders = Boton(image=None, pos=(770, 570), 
                            text_input="❯", font=tomar_fuente(30), base_color=celeste, hovering_color=verde) #Boton con icono [?] donde se muestra a los creadores
             
        #evento donde si el mouse esta posicionado encima del boton este cambie de color
        for button in [btn_jugar, btn_salir, btn_coders,titulo_juego]:
            button.changeColor(cur_pos)
            button.update(vt)
        
        #evento donde el mouse da click sucede un evento
        for event in pygame.event.get():
            #evento QUIT (cerrar)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #evento MOUSEBUTTONDOWN (click)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_jugar.checkForInput(cur_pos):
                    boton_jugar() #redireccion a boton jugar
                if btn_salir.checkForInput(cur_pos):
                    pygame.quit() #redireccion a boton salir
                    sys.exit()
                if btn_coders.checkForInput(cur_pos):
                    caratula() #redireccion a ventana de creadores (coders)
                
        pygame.display.update() #actualizacion de vt

#funcion de boton jugar
def boton_jugar():
    while True: # Se define ciclica la siguiente parte del codigo
        vt = pygame.display.set_mode((1280,650)) #abre nueva ventana con los parametros establecidos para pantalla jugar
        cur_pos = pygame.mouse.get_pos() #posicion de cursor 
        fdpmdj = pygame.image.load(imagen_modo_juego) #carga imagen de fondo
        vt.blit(fdpmdj, (0, 0))

        ## Texto Jugar
        # jugar_txt = da formato a nuestro texto
        btn_jugar_pve = Boton(image=pygame.image.load(imagen_boton), pos=(290, 435), 
                            text_input="PVE", font=tomar_fuente(70), base_color=blanco, hovering_color=verde) #boton pve
        btn_jugar_pvp = Boton(image=pygame.image.load(imagen_boton), pos=(965, 215), 
                            text_input="PVP", font=tomar_fuente(70), base_color=blanco, hovering_color=verde) #boton pvp
        
        jtxt_retornar = Boton(image=None, pos=(640, 565), 
                            text_input="retornar", font=tomar_fuente(65), base_color=blanco, hovering_color=rojo) #boton retornar

        #evento sobre la posicion del cursor
        for button in [btn_jugar_pve, btn_jugar_pvp]:
            button.changeColor(cur_pos)
            button.update(vt)

        #evento sobre la posicion del texto retornar
        jtxt_retornar.changeColor(cur_pos)
        jtxt_retornar.update(vt)

        #evento donde el mouse da click sucede un evento
        for event in pygame.event.get():
            #evento QUIT (cerrar)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #evento MOUSEBUTTONDOWN (click)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jtxt_retornar.checkForInput(cur_pos):
                    main_menu() #redireccion a retornar
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_jugar_pve.checkForInput(cur_pos):
                    boton_jugar_pve() #redireccion a pve
                    iniciar_juego_pve() #redireccion a pvp
                if btn_jugar_pvp.checkForInput(cur_pos):
                    iniciar_juego_pvp()
     
        #actualiza pantalla
        pygame.display.update()


#funcion de 
def caratula():
    while True:
        vt = pygame.display.set_mode((medidas['ventana_ancho'], medidas['ventana_alto']))
        cur_pos = pygame.mouse.get_pos()
        fdpmdj = pygame.image.load(imagen_caratula)
        vt.blit(fdpmdj, (0, 0))

        # Texto Pruebas

        jtxt_retornar = Boton(image=None, pos=(1150, 620), 
                        text_input="retornar", font=tomar_fuente(30), base_color=naranja, hovering_color=verde)

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

### Funciones principales
# Para inicializar la modalidad de juego requerida
def iniciar_juego_pve():
    ## Esta funcion se llama en el momento que hacemos click 
    ## en el boton PVE e inicializa toda la logica del juego
    llamada_de_funciones_pve()


def iniciar_juego_pvp(): 
    ## Esta funcion se llama en el momento que hacemos click 
    ## en el boton PVP e inicializa toda la logica del juego
    llamada_de_funciones_pvp()
    
if __name__ == "__main__": 
    # Cuando ejecutamos el programa
    # esta es la primera funcion que se llama
    main_menu()