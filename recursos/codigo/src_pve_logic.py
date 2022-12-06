import pygame, sys
from pygame.locals import *
from random import *
from time import *
from recursos.codigo.src_parametros_generales import *

vt = pygame.display.set_mode((medidas['ventana_ancho'], medidas['ventana_alto']))
reloj = pygame.time.Clock()

def tomar_fuente(fuente_T): # fuente_T = Tamaño de la fuente 
    return pygame.font.Font(import_fuente, fuente_T) # Se importa la fuente, y se pasa la variable "fuente_T" para definir tamaño de la fuente
def boton_jugar_pve():
    vt = pygame.display.set_mode((medidas['ventana_ancho'], medidas['ventana_alto']))
    fdpi = pygame.image.load(imagen_mar)
    vt.blit(fdpi, (0, 0))

class pve_logic():
    def llamada_de_funciones(primer_tablero, segundo_tablero, pos_barcos_first_tab, pos_barcos_sec_tab):
        # se llaman funcionar principales para definir tableros y barcos
        boton_jugar_pve()
        teclas = []
        continua_curso_juego = True

        while continua_curso_juego:
            pve_logic.dibuja_tableros(primer_tablero, segundo_tablero)
            sleep(0.1)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_F10:
                        boton_jugar_pve()
                        pve_logic.dibuja_tableros(primer_tablero, segundo_tablero)
                    teclas.append(event.key)
                if ((len(teclas)>=3) or
                    (teclas and
                    (teclas[-1] in (pygame.K_RETURN, pygame.K_ESCAPE)))
                    ):
                    if (len(teclas)>=3) and (teclas[2]==pygame.K_RETURN):
                        coordenadas = chr(teclas[0]) + chr(teclas[1])

                        x,y = pve_logic.traducir_coordenadas(coordenadas)
                        disparo_ok = ((0<=x<cuadros_perLado) and
                                    (0<=y<cuadros_perLado) )
                    else:
                        disparo_ok = False
                    teclas = []

                    if disparo_ok:
                        print()
                        pve_logic.imprimir_tablero(primer_tablero)
                        print()
                        pve_logic.imprimir_tablero(segundo_tablero)
                        print(coordenadas)
                        pve_logic.comprueba_unidad_destruida(segundo_tablero, pos_barcos_sec_tab, x, y)
                        segundo_tablero = pve_logic.ejecucion_Ddisparo(segundo_tablero, x, y)

                        if pve_logic.ha_terminado(segundo_tablero):
                            pve_logic.dibuja_tableros(primer_tablero, segundo_tablero)
                            pygame.display.update()
                            sleep(3)
                            continua_curso_juego = False
                        pve_logic.dibuja_tableros(primer_tablero, segundo_tablero)
                        sleep(1)
                        x,y = pve_logic.ataque_pc_nivel_2(pve_logic.oculta_posde_barcos(primer_tablero))
                        print(pve_logic.traducir_coordenadas_al_reves(x,y))
                        pve_logic.comprueba_unidad_destruida(primer_tablero, pos_barcos_first_tab, x, y)
                        primer_tablero = pve_logic.ejecucion_Ddisparo(primer_tablero, x, y)
                        if pve_logic.ha_terminado(primer_tablero):
                            pygame.display.update()
                            sleep(3)
                            pve_logic.dibuja_tableros(primer_tablero, segundo_tablero)
                            continua_curso_juego = False
                    else:
                        print('??')
                        print(texto_coordenadas_erroneas)

    ### Dibujo, trazado y analisis de tableros
    def atravezar_tablero(tablero_de_juego):
        cruzando_tablero = [[' ']*cuadros_perLado for _ in range(cuadros_perLado)]
        for i in range(cuadros_perLado):
            for j in range(cuadros_perLado):
                cruzando_tablero[i][j] = tablero_de_juego[j][i]
        return cruzando_tablero

    def imprimir_tablero(tablero_de_juego):
        cruzando_tablero = pve_logic.atravezar_tablero(tablero_de_juego)
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

        pve_logic.d_cuadricula_dTabs(Coordenadas_en_X0,Coordenadas_en_Y0)
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
        pve_logic.dib_tablero_de_juego(Coordenadas_en_X0,Coordenadas_en_Y0,primer_tablero)
        Coordenadas_en_X0 = medidas['margen'] + medidas['separacion'] + medidas['lado_cuadrado']*cuadros_perLado
        Coordenadas_en_Y0 = medidas['margen']

        # Segundo Tablero
        segundo_tablero_OcuPos = pve_logic.oculta_posde_barcos(segundo_tablero)
        pve_logic.dib_tablero_de_juego(Coordenadas_en_X0,Coordenadas_en_Y0,segundo_tablero_OcuPos)
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
            print('El ordenador dispara:', pve_logic.traducir_coordenadas_al_reves(x, y))
        else:
            print('aquí ya he disparado, mejor vuelvo a lanzar los dados')
            x,y = pve_logic.ataque_pc_nivel_1(tablero_de_juego)
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
        vecinos = pve_logic.verificar_posicionTab(x,y)
        return any(tablero_de_juego[x_vecino][y_vecino]=='X'
                for (x_vecino, y_vecino) in vecinos)

    def ataque_pc_nivel_2(tablero_de_juego):
        # En base a la verificacion de casillas vecinas se trata de dar
        # un ejecucion_Ddisparo certero
        casillas_prioritarias = [
            (x,y) for x in range(cuadros_perLado)
                for y in range(cuadros_perLado)
            if (tablero_de_juego[x][y]==' ') and pve_logic.se_verifica_VecinoX(tablero_de_juego, x,y)
            ]
        if len(casillas_prioritarias) > 0:
            x,y = choice(casillas_prioritarias)
        else:
            x,y = pve_logic.ataque_pc_nivel_1(tablero_de_juego)
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
        if not pve_logic.se_verifica_VecinoX(tablero_de_juego, x, y):
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
                    print(texto_alerta_hundido)
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
            pve_logic.dibuja_barcos_Dur_Col(largo, x + columna*medidas['lado_cuadrado'], y, False, color)
            barco_en_columna[columna:columna+largo] = [j]*largo
            columna = columna + largo + 1
        return barco_en_columna

    def se_puede_colocar(largo, fila, columna, vertical, tablero_de_juego):
        # Con esta funcion verificamos que la pocisiones en el tablero no 
        # esten ocupadas y que podamos colocar el barco sin traslparlo
        # con otro barco
        if (vertical and fila+largo>cuadros_perLado):
            print(texto_alerta_fuera)
            return False
        if (not vertical and columna+largo>cuadros_perLado):
            print(texto_alerta_fuera)
            return False
        if vertical:
            for y in range(max(0,fila-1), min(fila+largo+1, cuadros_perLado)):
                for x in range(max(0,columna-1), min(columna + 2, cuadros_perLado)):
                    if tablero_de_juego[x][y]=='B':
                        print(texto_alerta_barcos_juntos)
                        return False
        else:
        # con este condificonal limitamos entre los distintos barcos
            for y in range(max(0,fila-1), min(fila+2, cuadros_perLado)):
                for x in range(max(0,columna-1), min(columna + largo+1, cuadros_perLado)):
                    if tablero_de_juego[x][y]=='B':
                        print(texto_alerta_barcos_juntos)
                        return False
        return True

    def coloca_barcos(tablero_de_juego, x, y):
        # Con esta funcion se colocan los barcos en tablero
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
                            elemento_nuevo = 'B'
                        elif elemento_antiguo=='B':
                            elemento_nuevo = ' '
                        else:
                            elemento_nuevo = elemento_antiguo
                        fila_nueva.append(elemento_nuevo)
                tablero_procesado.append(fila_nueva)
        return tablero_procesado

    def coloca_un_barco(tablero_de_juego, x, y, largo, vertical):
        # Se marcan como ocupadas las casillas de la cuadricula
        # segun si el barco se pocisiona en x (filas), o en y (columnas)
        if vertical:
            for j in range(largo):
                tablero_de_juego = pve_logic.coloca_barcos(tablero_de_juego, x + j, y)
        else:
            for j in range(largo):
                tablero_de_juego = pve_logic.coloca_barcos(tablero_de_juego, x, y + j)
        return tablero_de_juego

    def colocar_barcos_viejo():
        # Con esta funciona se cargan los barcos colocados
        # previamente, y renderiza el tableto con las
        # pocisiones ocupadas
        primer_tablero = pve_logic.tablero_vacio()
        segundo_tablero = pve_logic.tablero_vacio()
        seguir_colocando = True
        while seguir_colocando:
            pve_logic.dibuja_tableros(primer_tablero, segundo_tablero)
            sleep(0.1)
            events = pygame.event.get()
            # proceed events
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    seguir_colocando = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    print(x,y)
                    if ((medidas['margen'] <= x < medidas['margen'] + cuadros_perLado*medidas['lado_cuadrado']) and
                        (medidas['margen'] <= y < medidas['margen'] + cuadros_perLado*medidas['lado_cuadrado'])):
                        columna = (x - medidas['margen'])//medidas['lado_cuadrado']
                        fila = (y - medidas['margen'])//medidas['lado_cuadrado']
                        print(columna, fila)
                        print(pve_logic.traducir_coordenadas_al_reves(fila, columna))
                        primer_tablero = pve_logic.coloca_barcos(primer_tablero, fila, columna)
        return primer_tablero

    ### Colocacion de barcos enemigos
    ### Pc coloca sus propios barcos
    def pc_colocar_un_barco(tablero_de_juego, largo):
        # pc coloca un solo barco
        buena_posicion = False
        while not buena_posicion:
            vertical = choice([True, False])
            if vertical:
                columna = randint(0, cuadros_perLado-1)
                fila = randint(0, cuadros_perLado-1-largo)
            else: # if horizontal
                columna = randint(0, cuadros_perLado-1-largo)
                fila = randint(0, cuadros_perLado-1)
            buena_posicion = pve_logic.se_puede_colocar(largo, fila, columna, vertical, tablero_de_juego)
        tablero_procesado = pve_logic.coloca_un_barco(tablero_de_juego, fila, columna, largo, vertical)
        if vertical:
            posiciones_barco = [
                (columna, fila + j) for j in range(largo)
            ]
        else:
            posiciones_barco = [(columna+k, fila) for k in range(largo)]
        return tablero_procesado, posiciones_barco

    def pc_verfica_barcos(longitud_barcos):
        # pc verifica tablero, tipo de barcos y cantidad de barcos
        # luego llama funcion "pc_colocar_un_barco" para colocarlos
        tablero_de_juego = pve_logic.tablero_vacio()
        posiciones_barcos = {}
        for n,largo in enumerate(longitud_barcos):
            tablero_de_juego, posiciones_barco = pve_logic.pc_colocar_un_barco(tablero_de_juego, largo)
            posiciones_barcos[n] = posiciones_barco
        return tablero_de_juego, posiciones_barcos

    ### Colocacion de barcos
    def colocar_barcos():
        boton_jugar_pve()
        num_barcos = len(longitud_barcos)
        posiciones_barcos = {j:[] for j in range(num_barcos)}
        primer_tablero = pve_logic.tablero_vacio()
        segundo_tablero = pve_logic.tablero_duda()
        y_coloca_barcos_min = medidas['margen'] + medidas['lado_cuadrado']*(cuadros_perLado+2)
        y_coloca_barcos_max = y_coloca_barcos_min + medidas['lado_cuadrado']
        x_coloca_barcos_min = medidas['separacion']
        x_coloca_barcos_max = (x_coloca_barcos_min
            + sum(largo for largo in longitud_barcos)*medidas['lado_cuadrado']
            + sum(1 for largo in longitud_barcos)*medidas['lado_cuadrado']
        )
        seguir_colocando = True
        barco_seleccionado = -1
        barcos_colocados = [False]*len(longitud_barcos)
        vertical = False
        while seguir_colocando:
            sleep(0.1)
            pve_logic.dibuja_tableros(primer_tablero, segundo_tablero)
            barco_en_columna = pve_logic.opc_disp_barcos_dejugador(
                x_coloca_barcos_min, y_coloca_barcos_min,
                barco_seleccionado, barcos_colocados)
            if ((barco_seleccionado >= 0) and
                (medidas['margen'] <= x < medidas['margen'] + cuadros_perLado*medidas['lado_cuadrado']) and
                (medidas['margen'] <= y < medidas['margen'] + cuadros_perLado*medidas['lado_cuadrado'])):
                columna = (x - medidas['margen'])//medidas['lado_cuadrado']
                fila = (y - medidas['margen'])//medidas['lado_cuadrado']
                largo = longitud_barcos[barco_seleccionado]
                if vertical and (fila+largo <= cuadros_perLado):
                    pve_logic.dibuja_barcos_Dur_Col(largo, medidas['margen']+columna*medidas['lado_cuadrado'], medidas['margen']+fila*medidas['lado_cuadrado'], vertical, color=gris)
                elif (not vertical) and (columna + largo <= cuadros_perLado):
                    pve_logic.dibuja_barcos_Dur_Col(largo, medidas['margen']+columna*medidas['lado_cuadrado'], medidas['margen']+fila*medidas['lado_cuadrado'], vertical, color=gris)
            pygame.display.update()
            events = pygame.event.get()
            # proceed events
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if sum(barcos_colocados)<num_barcos:
                        print(texto_alerta_sin_terminar)
                    else:
                        seguir_colocando = False
                elif event.type == pygame.MOUSEMOTION:
                    x,y = pygame.mouse.get_pos()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    if event.button==3:
                        vertical = not vertical
                    elif ((barco_seleccionado>=0) and
                        (medidas['margen'] <= x < medidas['margen'] + cuadros_perLado*medidas['lado_cuadrado']) and
                        (medidas['margen'] <= y < medidas['margen'] + cuadros_perLado*medidas['lado_cuadrado'])):
                        columna = (x - medidas['margen'])//medidas['lado_cuadrado']
                        fila = (y - medidas['margen'])//medidas['lado_cuadrado']
                        if pve_logic.se_puede_colocar(largo, fila, columna, vertical, primer_tablero):
                            primer_tablero = pve_logic.coloca_un_barco(primer_tablero, fila, columna, largo, vertical)
                            barcos_colocados[barco_seleccionado] = True
                            if vertical:
                                posiciones_barcos[barco_seleccionado] = [
                                    (columna, fila + j) for j in range(largo)
                                ]
                            else:
                                posiciones_barcos[barco_seleccionado] = [
                                    (columna + j, fila) for j in range(largo)
                                ]
                            barco_seleccionado = -1
                    elif ((x_coloca_barcos_min <= x < x_coloca_barcos_max) and
                        (y_coloca_barcos_min <= y < y_coloca_barcos_max)):
                        columna = (x - x_coloca_barcos_min)//medidas['lado_cuadrado']
                        barco_seleccionado = barco_en_columna[columna]
                        if barcos_colocados[barco_seleccionado]:
                            for columna, fila in posiciones_barcos[barco_seleccionado]:
                                primer_tablero[columna][fila] = ' '
                            barcos_colocados[barco_seleccionado] = False
        return primer_tablero, posiciones_barcos

    def ha_terminado(tablero_de_juego):
        for linea in tablero_de_juego:
            for elemento in linea:
                if elemento=='B':
                    return False
        return True

    def texto_jugador(texto):
        wth = tomar_fuente(20).render(texto, True, negro)
        pygame.draw.rect(vt, blanco,
                        (medidas['margen'] + medidas['tamaño_letra'] + medidas['lado_cuadrado']*cuadros_perLado, medidas['margen'],
                        2*medidas['tamaño_letra'], medidas['tamaño_letra']))
        vt.blit(wth, (medidas['margen'] + medidas['tamaño_letra'] + medidas['lado_cuadrado']*cuadros_perLado, medidas['margen']))

    def texto_ordenador(texto):
        wth = tomar_fuente(20).render(texto, True, rojo)
        pygame.draw.rect(vt, blanco,
                        (medidas['margen'] + medidas['tamaño_letra'] + medidas['lado_cuadrado']*cuadros_perLado, medidas['margen'] + medidas['lado_cuadrado'],
                        2*medidas['tamaño_letra'], medidas['tamaño_letra']))
        vt.blit(wth, (medidas['margen'] + medidas['tamaño_letra'] + medidas['lado_cuadrado']*cuadros_perLado, medidas['margen'] + medidas['lado_cuadrado']))

    def texto_victoria(texto):
        x = 50
        y = 800 - medidas['tamaño_letra']*4
        pve_logic.dibuja_texto_largo(texto, x, y, tomar_fuente(20), medidas['tamaño_letra'])

    def dibuja_texto_largo(texto, x, y, font, fontsize):
        lineas = texto.splitlines()
        for i, l in enumerate(lineas):
            vt.blit(font.render(l, True, negro), (x, y + fontsize*i))

    def pantalla_texto(texto_total):
        boton_jugar_pve()
        wth = tomar_fuente(20).render(título, True, negro)
        vt.blit(wth, (medidas['ventana_ancho']/2 - wth.get_bounding_rect().width/2, 50))
        tiempo_inicial = pygame.time.get_ticks()
        while True:
            reloj.tick(40)
            hasta_aqui = int((pygame.time.get_ticks() - tiempo_inicial)/velocidad_texto)
            texto = texto_total[:hasta_aqui]
            pve_logic.dibuja_texto_largo(texto, 100, 200, tomar_fuente(20), medidas['tamaño_letra'])
            pygame.display.update()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif (event.type == pygame.KEYDOWN and
                    event.key in (pygame.K_RETURN, pygame.K_ESCAPE)):
                    return event.key
                elif (event.type == pygame.KEYDOWN and
                    event.key in (pygame.K_SPACE, pygame.K_DOWN)):
                    # un truco para que ponga todo el texto
                    tiempo_inicial = -100000

    def volver_a_jugar():
        tecla = pve_logic.pantalla_texto(texto_volver_a_jugar)
        if tecla == pygame.K_RETURN:
            return True
        elif tecla == pygame.K_ESCAPE:
            return False
