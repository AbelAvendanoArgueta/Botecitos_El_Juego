import time
import pygame
import pygame.freetype
from src_server_cliente import Server_Client
from src_parametros_generales import *

# Importacion de Fuente
def tomar_fuente(fuente_T): # fuente_T = Tamaño de la fuente 
    return pygame.font.Font(import_fuente, fuente_T) # Se importa la fuente, y se pasa la variable "fuente_T" para definir tamaño de la fuente

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

    def dibujo_barco_opc(self, pantalla):
        for pocision in self.array:
            if self._color != negro:
                pygame.draw.rect(pantalla, self._color,
                                 pygame.Rect(pocision[0] * medidas['ventana_ancho_mini'] / 10,
                                             pocision[1] * medidas['ventana_alto_mini'] / 10,
                                             medidas['ventana_ancho_mini'] / 10,
                                             medidas['ventana_alto_mini'] / 10)
                                 )

    def traduccion_barcosIn_tab(self, cambio):
        temporal_inicio = (cambio[0] + self._inicio[0], cambio[1] + self._inicio[1])
        temporal_final = (cambio[0] + self._fin[0], cambio[1] + self._fin[1])
        if not self.verificar_limites(temporal_inicio, temporal_final):
            return
        self.creando_formacion_barcos(temporal_inicio, temporal_final)
        self._inicio, self._fin = temporal_inicio, temporal_final

    def rotacion_barco(self):
        cambio = (self._fin[0] - self._inicio[0], self._fin[1] - self._inicio[1])
        temporal_final = (cambio[1] + self._inicio[0], cambio[0] + self._inicio[1])
        if not self.verificar_limites(self._inicio, temporal_final):
            return
        self.creando_formacion_barcos(self._inicio, temporal_final)
        self._fin = temporal_final

    def proveer_estadoTo_barco(self, fase):
        self.estadoD_barco = fase
        if self.estadoD_barco == "no colocado":
            self.establece_color(negro)
        elif self.estadoD_barco == "en movimiento":
            self.establece_color(blanco)
        elif self.estadoD_barco == "colocado":
            self.establece_color(gris_claro)

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
        self._pantalla_texto = [self.renderizacionD_texto("Fase de colocación")]
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
        for index in self._barcos_jugador:
            intentos_realizados[index] = []
        intentos_realizados["Falla_Intento"] = []
        return intentos_realizados

    def inicializacionD_diccs_Coordenadas(self):
        # Crea diccionario de todas las coordenadas ocupadas por un mosaico de barco
        var_coordenadas = {}
        for index, barco in self._barcos_jugador.items():
            var_coordenadas[index] = barco.toma_formacion()
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
            self.dibuja_estado_actualD_barcos()
            if self.tomar_fase() != "Colocación":
                self.dibuja_disparos_realizados()
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

    def definir_fase_actual(self, fase, nombre=None):
        self.fase = fase
        self.actualizacion_de_texto(nombre)

    def validacionD_turno(self, turno):
        # Comprueba si ya el usuario cliente actual ha realizado un intento/turno
        for barco in self.tomaD_entradas_contra().values():
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

    # Comunicación con el host a travez del cliente
    # Usando los mensajes "Entra" y "Sale"
    # para validar acciones
    
    def intercambioD_mensajes(self, mensaje):
        # Recibe un mensaje del cliente y lo pasa a la función auxiliar correspondiente.
        # Si este proyecto tiene un talón de aquiles, sin duda es esta madre.
        nombre = mensaje[0]
        if len(mensaje) == 2:
            if mensaje[-1] == "Entra":
                self.procesaSi_C_une(nombre)
            elif mensaje[-1] == "Sale":
                self.procesaSi_C_sale(nombre)
            elif mensaje[-1] == "Listo":
                self.procesaSi_listo(nombre)

        else:
            if nombre != self._nombreD_jugador and mensaje[1] == "Movimiento_Reconocido":
                return self.procesaSi_movimiento(mensaje[2:])
            elif mensaje[1] == "Respuesta_Reconocida":
                respuesta = self.procesaSi_respuesta(nombre, mensaje[2:])
                return respuesta
            elif mensaje[1] == "Finaliza":
                self.definir_fase_actual("Termina", mensaje[2])
        return None

    # Funciones para clientes por individual

    def cambioD_turno(self):
        # Cambios de turno entre jugadores
        print("Cambio de turno")
        if self.tomar_fase() == "Turno del Oponente":
            self.definir_fase_actual("Turno del jugador")
        elif self.tomar_fase() == "Turno del jugador":
            self.definir_fase_actual("Turno del Oponente")
        else:
            return

    def tomaD_entradas_contra(self):
        # Devuelve la informacion del turno segun lo que el contricante haya 
        # Determinado y en sabe al turno actual
        if self.tomar_fase() == "Turno del Oponente":
            return self._intentos_del_oponente
        elif self.tomar_fase() == "Turno del jugador":
            return self._intentos_del_jugador

    def toma_barcosActualizados(self):
        # Devuelve los barcos para dibujar en función del turno actual.
        if self.tomar_fase() == "Turno del Oponente" or self.tomar_fase() == "Colocación":
            return self._barcos_jugador
        elif self.tomar_fase() == "Turno del jugador":
            return self._barcosD_oponente

    # Funcion que solo funcionan en cliente individual

    def dibuja_disparos_realizados(self):
        # Colorea y dibuja intentos en la pantalla.
        for nombre, intentos_realizados in self.tomaD_entradas_contra().items():
            if nombre != "Falla_Intento":
                color = rojo
            else:
                color = azul
            for turno in intentos_realizados:
                pygame.draw.circle(self._pantalla_ventana, color,
                                   (int((turno[0] + 0.5) * medidas['ventana_ancho_mini'] / 10),
                                    int((turno[1] + 0.5) * medidas['ventana_alto_mini'] / 10)),
                                   medidas['ventana_ancho_mini'] // 40)

    def dibuja_estado_actualD_barcos(self):
        barcos = self.toma_barcosActualizados()
        for barco in barcos.values():
            barco.dibujo_barco_opc(self._pantalla_ventana)

    def renderizacionD_texto(self, text, x=medidas['ventana_ancho_mini'] / 2, y=medidas['ventana_alto_mini'] / 20, color=blanco):
        superficieD_texto, rect = self._font.render(text, color)
        return [superficieD_texto, x - (rect.width / 2), y - (rect.height / 2)]

    def actualizacion_de_texto(self, nombre):
        # Esta funciona actualiza el texto superior segun el estado de turno actual
        # es decir, me toca o no me toca?
        if self.fase == "Esperando":
            self._pantalla_texto = [self.renderizacionD_texto("Esperando a otro jugador")]
        elif self.fase == "Turno del jugador":
            self._pantalla_texto = [self.renderizacionD_texto("Tu turno")]
        elif self.fase == "Turno del Oponente":
            self._pantalla_texto = [self.renderizacionD_texto("Turno Enemigo")]
        elif self.fase == "Termina":
            if nombre:
                self._pantalla_texto =[self.renderizacionD_texto("Jugador {} gana!".format(nombre))]
            else:
                self._pantalla_texto = [self.renderizacionD_texto("Contrincante abandona".format(nombre))]
            self._pantalla_texto.append(self.renderizacionD_texto("Regresa al lobby", medidas['ventana_ancho_mini'] / 2, medidas['ventana_alto_mini'] * 11 / 10 / 2, negro))

    # Reconocimiento de mensajes enemigos

    def procesaSi_movimiento(self, mensaje):
        # Recibe un movimiento (suposición) de otro jugador.
        # Comprueba si ha golpeado a algún barco. Luego mira si se ha hundido alguno.
        # Actualice las listas de conjeturas y devuelva la respuesta
        turno = (int(mensaje[0]), int(mensaje[1]))
        self._ultimo_intento = turno
        respuesta = "Respuesta_Reconocida,Falla"
        for index, barco in self._cantidad_de_intentos_validos.items():
            if index == "Falla_Intento":
                continue
            if turno in barco:
                respuesta = "Respuesta_Reconocida,disparo,{}".format(index)
                # Más uno ya que las conjeturas se actualizarán más tarde
                if len(self._intentos_del_oponente[index]) + 1 == len(barco):
                    respuesta = "Respuesta_Reconocida,Hundir,{}".format(index)
        return respuesta