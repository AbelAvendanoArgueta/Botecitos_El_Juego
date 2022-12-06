import time
import pygame
import pygame.freetype
from src_server_cliente import Server_Client
from src_parametros_generales import *

class Barcos:
    def __init__(self, inicio, fin, color):
        self._inicio = inicio
        self._fin = fin
        self._color = color
        self.estadoD_barco = "no colocado"
        self.array = []
        self.creando_formacion_barcos(self._inicio, self._fin)
        self.tamano = len(self.array)

    def creando_formacion_barcos(self, inicio, fin):
        self.array = []
        x, y = inicio
        if inicio[0] == fin[0]:
            for y in range(inicio[1], fin[1] + 1):
                self.array.append((x, y))

        elif inicio[1] == fin[1]:
            for x in range(inicio[0], fin[0] + 1):
                self.array.append((x, y))

    def dibujo_barco_opc(self, screen):
        for pocision in self.array:
            if self._color != negro:
                pygame.draw.rect(screen, self._color,
                                 pygame.Rect(pocision[0] * medidas['ventana_ancho_mini'] / 10,
                                             pocision[1] * medidas['ventana_alto_mini'] / 10,
                                             medidas['ventana_ancho_mini'] / 10,
                                             medidas['ventana_alto_mini'] / 10)
                                 )

    def traduccion_barcosIn_tab(self, cambio):
        temporal_inicio = (cambio[0] + self._inicio[0], cambio[1] + self._inicio[1])
        temporal_final = (cambio[0] + self._fin[0], cambio[1] + self._fin[1])
        if not self._check_boundaries(temporal_inicio, temporal_final):
            return
        self.creando_formacion_barcos(temporal_inicio, temporal_final)
        self._inicio, self._fin = temporal_inicio, temporal_final

    def rotacion_barco(self):
        cambio = (self._fin[0] - self._inicio[0], self._fin[1] - self._inicio[1])
        temporal_final = (cambio[1] + self._inicio[0], cambio[0] + self._inicio[1])
        if not self._check_boundaries(self._inicio, temporal_final):
            return
        self.creando_formacion_barcos(self._inicio, temporal_final)
        self._fin = temporal_final

    def proveer_estadoTo_barco(self, fase):
        self.estadoD_barco = fase
        if self.estadoD_barco == "no colocado":
            self._set_colour(negro)
        elif self.estadoD_barco == "en movimiento":
            self._set_colour(blanco)
        elif self.estadoD_barco == "colocado":
            self._set_colour(gris_claro)

    def verificar_limites(self, inicio, fin):
        if (inicio[0] < 0 or inicio[0] > 9
                or inicio[1] < 1 or inicio[1] > 10
                or fin[0] < 0 or fin[0] > 9
                or fin[1] < 1 or fin[1] > 10):
            return False
        else:
            return True

    def se_puede_colocar(self, barcos):
        for barco in barcos.values():
            if barco.toma_estadoD_barco() == "colocado":
                for pocision in self.toma_formacion():
                    if pocision in barco.toma_formacion():
                        return True
        return False

    def toma_tamano(self):
        return self.tamano

    def establece_color(self, color):
        self._color = color

    def toma_formacion(self):
        return self.array

    def toma_estadoD_barco(self):
        return self.estadoD_barco

    def __toma_objeto__(self, item):
        return self.array[item]


class Tablero:
    # Clase que representa el tablero del jugador. Contiene naves y conjeturas de jugadores y oponentes.
    def __init__(self, pantalla, font):
        self.fase = "Colocación"  # Puede ser colocación, espera, Turno del jugador, Turno del Oponente, final
        self._pantalla_ventana = pantalla
        self._font = font
        self._pantalla_texto = [self._render_text("Fase de colocación")]
        self._barcos_jugador = {'1': Barcos((0, 1), (4, 1), blanco),
                              '2': Barcos((0, 1), (3, 1), negro),}
                              #'3': Barcos((0, 1), (2, 0), negro),
                              #'4':Barcos((0, 1), (1, 0), negro),
                              #'5':Barcos((0, 1), (1, 0), negro),
                              #  }
        self.cantidadD_barcos_disp = len(self._barcos_jugador)
        self._cantidad_de_intentos_validos = {}
        self._intentos_del_oponente = self.inicializacionD_diccionarios()
        self._intentos_del_jugador = self.inicializacionD_diccionarios()
        self._barcosD_oponente = {}
        self._ultimo_intento = None
        self._nombreD_jugador = None
        self._juego_listoP_empezar = False
        self._numero_de_hundidos = 0

    # Initialisation functions

    def inicializacionD_diccionarios(self):
        # Crea diccionario de listas vacías para cada barco, así como fallas.
        intentos_realizados = {}
        for idx in self._barcos_jugador:
            intentos_realizados[idx] = []
        intentos_realizados["Falla_Intento"] = []
        return intentos_realizados


    def inicializacionD_diccs_Coordenadas(self):
        # Crea diccionario de todas las coordenadas ocupadas por un mosaico de barco
        var_coordenadas = {}
        for idx, barco in self._barcos_jugador.items():
            var_coordenadas[idx] = barco.toma_formacion()
        return var_coordenadas

    # Funciones para definir parametros de ventana y tablero
    def dibuja_tableros(self):
        # Dibuja el tablero a la superficie de pygame.
        self._pantalla_ventana.fill(gris)
        for x in range(1, 11):
            pygame.draw.line(self._pantalla_ventana, gris_claro,
                             (medidas['ventana_ancho_mini'] * x / 10, medidas['ventana_alto_mini'] / 10),
                             (medidas['ventana_ancho_mini'] * x / 10, medidas['ventana_alto_mini'] + medidas['ventana_alto_mini'] / 10), 1)
            pygame.draw.line(self._pantalla_ventana, gris_claro,
                             (0, medidas['ventana_alto_mini'] * x / 10),
                             (medidas['ventana_ancho_mini'], medidas['ventana_alto_mini'] * x / 10), 1)

        if self.tomar_fase() not in ["Termina", "Esperando"]:
            self._draw_ships()
            if self.tomar_fase() != "Colocación":
                self._draw_guesses()
        elif self.tomar_fase() == "Termina":
            pygame.draw.rect(self._pantalla_ventana, blanco,
                             pygame.Rect((medidas['ventana_ancho_mini'] / 2) - (medidas['ventana_ancho_mini'] / 4),
                                         (medidas['ventana_alto_mini'] * 11 / 10 / 2) - (medidas['ventana_alto_mini'] / 10),
                                         medidas['ventana_ancho_mini'] / 2,
                                         medidas['ventana_alto_mini'] / 5))

        for objetoD_texto in self._pantalla_texto:
            self._pantalla_ventana.blit(objetoD_texto[0], (objetoD_texto[1], objetoD_texto[2]))

    def tomar_fase(self):
        return self.fase

    def definir_fase_actual(self, fase, name=None):
        self.fase = fase
        self._update_text(name)

    def validacionD_turno(self, turno):
        # Comprueba si ya el usuario cliente actual ha realizado un intento/turno
        for barco in self._get_guesses().values():
            if turno in barco:
                return False
        self._ultimo_intento = turno
        return True

    # Colocamiento de barcos

    def mover_barco(self, barco_index, key):
        # Mueve el barco en/por el tablero segun la entrada del usuario
        # a travez de las teclas arriba, abajo, derecha e izquierda
        if key == pygame.K_r:
            self._barcos_jugador[barco_index].rotacion_barco()
        if key == pygame.K_UP:
            self._barcos_jugador[barco_index].traduccion_barcosIn_tab((0, -1))
        if key == pygame.K_DOWN:
            self._barcos_jugador[barco_index].traduccion_barcosIn_tab((0, 1))
        if key == pygame.K_LEFT:
            self._barcos_jugador[barco_index].traduccion_barcosIn_tab((-1, 0))
        if key == pygame.K_RIGHT:
            self._barcos_jugador[barco_index].traduccion_barcosIn_tab((1, 0))

    def colocar_barco(self, barco_index):
        # Intentos de confirmar la posición de una pieza en fase de colocación. 
        # Comprueba si hay colisiones primero o si un barco esta cruzado con otro
        if not self._barcos_jugador[str(barco_index)].se_puede_colocar(self._barcos_jugador):
            self._barcos_jugador[str(barco_index)].proveer_estadoTo_barco("colocado")
            if barco_index < 2:
                self._barcos_jugador[str(barco_index + 1)].proveer_estadoTo_barco("en movimiento")
            return True
        return False