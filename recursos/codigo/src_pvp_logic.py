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