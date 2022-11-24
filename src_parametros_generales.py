# Configuracion de pantalla y tableros
medidas = {
    'lado_cuadrado': 30,
    'separacion': 100,
    'margen': 100, #Debe ser mayor que LADO_CUADRADO
    'tamaño_letra': 15,
    'tamaño_letra_grande': 30,
    'ventana_ancho': 1280,
    'ventana_alto': 650,
}

# colores
blanco = (255,255,255)
negro = (0,0,0)
gris = ("#3d4c4f")
rojo = (255,0,0)
verde = (0, 255, 0)
azul = (0, 0, 255)
azul_per = ("#3daee9")
amarillo_per = ("#f7eb95")
naranja = ("Orange")


# tipeo de texto
velocidad_texto = 100

# Parametros de juego
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
longitud_barcos = [1]
lado = 2

# Acceso a recursos de forma dinamica
import_fuente = "./recursos/tipografia/fuente.ttf"
imagen_menu_inicial = "./recursos/imagenes/fondo_rio.png"
imagen_botecitos_titulos = "./recursos/imagenes/titulo_pant_inicial.png"
imagen_boton = "./recursos/imagenes/boton_vt.png"
imagen_modo_juego = "./recursos/imagenes/fondo_modo_juego.png"
imagen_caratula = "./recursos/imagenes/caratula.png"
imagen_mar = "./recursos/imagenes/fondo_mar.png"

# Alertas
texto_longitud_barco='un barco de longitud'
texto_configurar='Pulsa F10 para configurar idioma y resolución de pantalla'
texto_continuar = '\nPulsa ENTER para continuar'
texto_alerta_fuera='No puedes sacar un barco del tablero'
texto_alerta_barcos_juntos = 'No se puede colocar un barco al lado de otro'
texto_coordenadas_erroneas = 'Tienes que escribir una letra seguida de un número'
texto_alerta_sin_terminar = 'No has terminado de colocar los barcos'
texto_alerta_hundido = 'Barco hundido'
texto_has_perdido = '¡Has perdido la batalla esperamos qué otros tengan más suerte qué tú!'
título = 'Botecitos el juego'
texto_volver_a_jugar = '''Pulsa Enter para volver a jugar,
Escape para salir

'''