# Configuracion de pantalla y tableros
medidas = {
    'lado_cuadrado': 30,
    'separacion': 100,
    'margen': 100, # Debe ser mayor que LADO_CUADRADO
    'tamaño_letra': 15,
    'tamaño_letra_grande': 30,
    'ventana_ancho': 1280,
    'ventana_alto': 650,
}

# Conexiones
conexiones = {
    "host": "127.0.0.1",
    "puerto": 33000,
    "buffer": 1024,
}

# colores
blanco = (255,255,255)
negro = (0,0,0)
gris = (61,76,79)
gris_claro = (152, 161, 162)
rojo = (255,0,0)
verde = (0, 255, 0)
azul = (0, 0, 255)
celeste = (61,174,233)
amarillo = (247, 235, 149)
naranja = (244, 56, 34)
rosado = (153, 29, 132)


# Tipeo de texto
velocidad_texto = 100

# Parametros de juego
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
longitud_barcos = [1]
    # Esta variable nos permite facilmente cambiar
    # la forma en la que trabaja la funcion
    # opc_disp_barcos_dejugador()
cuadros_perLado = 2 # no puede ser menor a 2
    # cuadros por lado define el tamaño
    # del tablero por medio de la cuadricula
    # por lado 

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