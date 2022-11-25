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
    cruzando_tablero = [[' ']*cuadros_perLado for _ in range(cuadros_perLado)]
    for i in range(cuadros_perLado):
        for j in range(cuadros_perLado):
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
                      cuadros_perLado*medidas['lado_cuadrado'], cuadros_perLado*medidas['lado_cuadrado']))
    # Lineas horizontales
    for j in range(0,cuadros_perLado+1):
        pygame.draw.line(vt, negro,
                         (Coordenadas_en_X0, Coordenadas_en_Y0 + medidas['lado_cuadrado']*j),
                         (Coordenadas_en_X0 + medidas['lado_cuadrado']*cuadros_perLado, Coordenadas_en_Y0 +medidas['lado_cuadrado']*j), 1)
    # Letras en las filas
    for j in range(0,cuadros_perLado):
        letra = tomar_fuente(20).render(letras[j], True, negro)
        vt.blit(letra, (Coordenadas_en_X0-medidas['lado_cuadrado'], Coordenadas_en_Y0 + medidas['lado_cuadrado']*j))

    # Lineas verticales
    for j in range(0,cuadros_perLado+1):
        pygame.draw.line(vt, negro,
                         (Coordenadas_en_X0 + medidas['lado_cuadrado']*j, Coordenadas_en_Y0),
                         (Coordenadas_en_X0 + medidas['lado_cuadrado']*j, Coordenadas_en_Y0 +medidas['lado_cuadrado']*cuadros_perLado), 1)

    # Numeros en las columnas
    for j in range(0,cuadros_perLado):
        letra = tomar_fuente(20).render(str(j+1), True, negro)
        vt.blit(letra, (Coordenadas_en_X0 + medidas['lado_cuadrado']*j + (medidas['lado_cuadrado'] - medidas['tamaño_letra']), Coordenadas_en_Y0 +medidas['lado_cuadrado']*cuadros_perLado))

def dib_tablero_de_juego(Coordenadas_en_X0,Coordenadas_en_Y0,tablero_de_juego):
    # Se dibuja tablero de juego

    d_cuadricula_dTabs(Coordenadas_en_X0,Coordenadas_en_Y0)
    # se toman las coordenadas de la cuadricula de los tableros
    for fila in range(cuadros_perLado):
        for columna in range(cuadros_perLado):
            casilla = tablero_de_juego[fila][columna]
            if casilla in 'BOX':
                if casilla=='B':
                    color = gris
                elif casilla=='O':
                    color = azul
                elif casilla=='X':
                    color = rojo
                pygame.draw.circle(vt, color,
                             (Coordenadas_en_X0+medidas['lado_cuadrado']*fila+medidas['lado_cuadrado']//2, Coordenadas_en_Y0 + medidas['lado_cuadrado']*columna+medidas['lado_cuadrado']//2),
                             medidas['lado_cuadrado']//2
                    )
            elif (casilla == ' ') or (casilla == '.'):
                pass
            else:
                letra = tomar_fuente(20).render(casilla, True, negro)
                vt.blit(letra, (Coordenadas_en_X0 + medidas['lado_cuadrado']*fila, Coordenadas_en_Y0 +medidas['lado_cuadrado']*columna))

def oculta_posde_barcos(tablero_de_juego):
    tablero_procesado = [] 
    for fila in tablero_de_juego:
        nueva_fila = [(' ' if casilla=='B' else casilla) for casilla in fila]
        tablero_procesado.append(nueva_fila)
    return tablero_procesado # Retorna un nuevo tablero con las pocisiones correctas

def dibuja_tableros(primer_tablero, segundo_tablero):
    # Primer Tablero
    Coordenadas_en_X0 = medidas['margen']
    Coordenadas_en_Y0 = medidas['margen']
    dib_tablero_de_juego(Coordenadas_en_X0,Coordenadas_en_Y0,primer_tablero)
    Coordenadas_en_X0 = medidas['margen'] + medidas['separacion'] + medidas['lado_cuadrado']*cuadros_perLado
    Coordenadas_en_Y0 = medidas['margen']

    # Segundo Tablero
    segundo_tablero_OcuPos = oculta_posde_barcos(segundo_tablero)
    dib_tablero_de_juego(Coordenadas_en_X0,Coordenadas_en_Y0,segundo_tablero_OcuPos)
    pygame.display.update() # necesario para refrescar con tablero sub-procesado
    # Se procesa tablero de oponente para ocultar pocisiones de barcos, y devolver
    # un tablero donde lo unico que se ve es la cuadricula

def tablero_vacio():
    # Refrescamiento de tableros
    return [[' ']*cuadros_perLado for _ in range(cuadros_perLado)]

def tablero_duda():
    # Refrescamiento exclusivamente para segundo tablero
    return [[' ']*cuadros_perLado for _ in range(cuadros_perLado)]

### Inteligencia enemiga

def ataque_pc_nivel_1(tablero_de_juego): 
    # ataque mas basico del pc
    # literalmente tu harias esto, probar al azar
    x = randint(0,cuadros_perLado-1)
    y = randint(0,cuadros_perLado-1)
    #Puede ser desconocido, o barco, porque el tablero_de_juego llega ofuscado
    if tablero_de_juego[x][y]==' ':
        print('El ordenador dispara:', traducir_coordenadas_al_reves(x, y))
    else:
        print('aquí ya he disparado, mejor vuelvo a lanzar los dados')
        x,y = ataque_pc_nivel_1(tablero_de_juego)
    return x,y

def traducir_coordenadas_al_reves(x,y):
    numero = str(x + 1)
    letra = chr(ord('A') + y)
    ejecucion_Ddisparo = letra + numero
    return ejecucion_Ddisparo

def traducir_coordenadas(ejecucion_Ddisparo):
    if len(ejecucion_Ddisparo)<2:
        return -1, -1
    letra, numero = ejecucion_Ddisparo[:2]
    x = ord(numero) - ord('1')
    y = ord(letra.upper())- ord('A')
    return x,y

def verificar_posicionTab(x,y):
    # Se verifica en que posicion del tablero esta ubicado
    vecinos = []
    if x>0:
        vecinos.append((x-1,y))
    if x<cuadros_perLado-1:
        vecinos.append((x+1,y))
    if y>0:
        vecinos.append((x,y-1))
    if y<cuadros_perLado-1:
        vecinos.append((x,y+1))
    return vecinos

def se_verifica_VecinoX(tablero_de_juego, x, y):
    # Se verifica si casilla vecina en X puede ser posicion enemiga
    vecinos = verificar_posicionTab(x,y)
    return any(tablero_de_juego[x_vecino][y_vecino]=='X'
               for (x_vecino, y_vecino) in vecinos)

def ataque_pc_nivel_2(tablero_de_juego):
    # En base a la verificacion de casillas vecinas se trata de dar
    # un ejecucion_Ddisparo certero
    casillas_prioritarias = [
        (x,y) for x in range(cuadros_perLado)
              for y in range(cuadros_perLado)
        if (tablero_de_juego[x][y]==' ') and se_verifica_VecinoX(tablero_de_juego, x,y)
        ]
    if len(casillas_prioritarias) > 0:
        x,y = choice(casillas_prioritarias)
    else:
        x,y = ataque_pc_nivel_1(tablero_de_juego)
    return x,y

def ejecucion_Ddisparo(tablero_de_juego, x, y):
    elemento_antiguo = tablero_de_juego[x][y]
    if elemento_antiguo in ' .':
        elemento_nuevo = 'O'
    elif elemento_antiguo=='B':
        elemento_nuevo = 'X'
        if x>0 and y>0 and tablero_de_juego[x-1][y-1] == ' ':
            tablero_de_juego[x-1][y-1] = '.'
        if x>0 and y<cuadros_perLado-1 and tablero_de_juego[x-1][y+1] == ' ':
            tablero_de_juego[x-1][y+1] = '.'
        if x<cuadros_perLado-1 and y>0 and tablero_de_juego[x+1][y-1] == ' ':
            tablero_de_juego[x+1][y-1] = '.'
        if x<cuadros_perLado-1 and y<cuadros_perLado-1 and tablero_de_juego[x+1][y+1] == ' ':
            tablero_de_juego[x+1][y+1] = '.'
    else:
        elemento_nuevo = elemento_antiguo
    tablero_de_juego[x][y] = elemento_nuevo
    return tablero_de_juego


def verificar_disparo_Prevrealizado(tablero_de_juego, x, y):
    # Se verifica si la casilla en la que se intenta disparar
    # es una casilla en la que se disparo previamente
    # luego se actualiza tablero
    tablero_procesado = []
    for numero_fila in range(cuadros_perLado):
        if numero_fila != y:
            fila_antigua = tablero_de_juego[numero_fila]
            tablero_procesado.append(fila_antigua)
        else:
            fila_antigua = tablero_de_juego[numero_fila]
            fila_nueva = []
            for numero_columna in range(cuadros_perLado):
                if numero_columna != x:
                    elemento_antiguo = fila_antigua[numero_columna]
                    fila_nueva.append(elemento_antiguo)
                else:
                    elemento_antiguo = fila_antigua[numero_columna]
                    if elemento_antiguo==' ':
                        elemento_nuevo = 'O'
                    elif elemento_antiguo=='B':
                        elemento_nuevo = 'X'
                    else:
                        elemento_nuevo = elemento_antiguo
                    fila_nueva.append(elemento_nuevo)
            tablero_procesado.append(fila_nueva)
            # se procesa tablero nuevo con casillas en filas y
            # columnas en las que ya hubo disparos
    if elemento_nuevo=='X':
        # marcamos con diagonales con punto
        pass
    return tablero_procesado

def comprueba_unidad_destruida(tablero_de_juego, posiciones_barcos, x, y):
    if tablero_de_juego[x][y] != 'B':
        return False
    if not se_verifica_VecinoX(tablero_de_juego, x, y):
        return False
    for j, posiciones_barco in posiciones_barcos.items():
        if any( (xbarco==x ) and (ybarco==y)
                for xbarco, ybarco in posiciones_barco ):
            #estoy disparando al barco j
            daño = sum(1 for xbarco, ybarco in posiciones_barco
                       if tablero_de_juego[xbarco][ybarco]=='X')
            largo = len(posiciones_barco)
            if daño == largo-1:
#                import pudb; pudb.set_trace()
                x_primer, y_primer = posiciones_barco[0]
                x_ultima, y_ultima = posiciones_barco[-1]
                if x_primer == x_ultima:
                    # vertical
                    # primera_casilla
                    x = x_primer
                    y = y_primer - 1
                    if y>=0 and tablero_de_juego[x][y] == ' ':
                        tablero_de_juego[x][y] = '.'
                    # ultima_casilla
                    x = x_primer
                    y = y_ultima + 1
                    if y<cuadros_perLado and tablero_de_juego[x][y] == ' ':
                        tablero_de_juego[x][y] = '.'
                else:
                    # horizontal
                    # primera_casilla
                    x = x_primer - 1
                    y = y_primer
                    if x>=0 and tablero_de_juego[x][y] == ' ':
                        tablero_de_juego[x][y] = '.'
                    # ultima_casilla
                    x = x_ultima + 1
                    y = y_ultima
                    if x<cuadros_perLado and tablero_de_juego[x][y] == ' ':
                        tablero_de_juego[x][y] = '.'
                alerta(texto_alerta_hundido)
                return True

### Trazado de barcos
### Jugador coloca sus barcos

def dibuja_barcos_Dur_Col(largo, x, y, vertical, color=gris):
    # Dibuja los barcos durante la colocacion en los tableros
    if vertical:
        pygame.draw.polygon(vt, color, [
            (x, y  + medidas['lado_cuadrado']//2),
            (x, y + medidas['lado_cuadrado']//2 + medidas['lado_cuadrado']*(largo-1)),
            (x + medidas['lado_cuadrado']//2, y + medidas['lado_cuadrado']*largo),
            (x + medidas['lado_cuadrado'], y + medidas['lado_cuadrado']//2 + medidas['lado_cuadrado']*(largo-1)),
            (x + medidas['lado_cuadrado'], y  + medidas['lado_cuadrado']//2),
            (x + medidas['lado_cuadrado']//2, y)
            ])
    else: # horizontal
        pygame.draw.polygon(vt, color, [
            (x + medidas['lado_cuadrado']//2, y),
            (x + medidas['lado_cuadrado']//2 + medidas['lado_cuadrado']*(largo-1), y),
            (x + medidas['lado_cuadrado']*largo, y + medidas['lado_cuadrado']//2),
            (x + medidas['lado_cuadrado']//2 + medidas['lado_cuadrado']*(largo-1), y + medidas['lado_cuadrado']),
            (x + medidas['lado_cuadrado']//2, y + medidas['lado_cuadrado']),
            (x, y + medidas['lado_cuadrado']//2)
            ])

def opc_disp_barcos_dejugador(x, y, barco_seleccionado, barcos_colocados):
    # Opciones disponible para el jugador
    # Dibuja opciones a elegir para acomodar en el tablero
    # Esta funcion facilmente puede ser editada desde
    # el archivo de parametros_generales longitud_barcos 
    barco_en_columna = [-1]*(sum(longitud_barcos) + len(longitud_barcos))
    columna = 0
    for j,largo in enumerate(longitud_barcos):
        if j == barco_seleccionado:
            color = azul
        elif barcos_colocados[j]:
            color = verde
        else:
            color = gris
        dibuja_barcos_Dur_Col(largo, x + columna*medidas['lado_cuadrado'], y, False, color)
        barco_en_columna[columna:columna+largo] = [j]*largo
        columna = columna + largo + 1
    return barco_en_columna
    
def alerta(texto):
    # Funcion para lanzar alertas segun parametro
    # pasado a travez de variable 'texto'
    # normamente los texto que imprimiran las alertas
    # estan ubicadas  en archivo de parametros generales
    global texto_alerta, tiempo_ultima_alerta
    tiempo_ultima_alerta = pygame.time.get_ticks()
    texto_alerta = texto