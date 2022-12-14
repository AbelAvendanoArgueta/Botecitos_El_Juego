from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from recursos.codigo.src_parametros_generales import conexiones

class Server_Client:
    def __init__(self, board):
        self.host = conexiones['host']
        self.puerto = conexiones['puerto']
        self.tamano_buffer = conexiones['buffer']
        self.nombre = None
        self.socketD_cliente = None
        self.board = board
        self.inicia_client()

    def inicia_client(self):
        # inicializa ejecucion de cliente
        self.socketD_cliente = socket(AF_INET, SOCK_STREAM)
        self.socketD_cliente.connect((self.host, self.puerto))

        # thread de comunicacion con el servidor
        recibe_hiloD_com = Thread(target=self.recibe_paquetes)
        recibe_hiloD_com.start()

    def recibe_paquetes(self):
        # Maneja la recepción de mensajes / paquetes
        while True:
            try:
                mensaje = self.socketD_cliente.recv(self.tamano_buffer).decode("utf8")
                mensaje = mensaje.split(',')
                print("recibió {}".format(mensaje))
                respuesta = self.board.intercambioD_mensajes(mensaje)
                if respuesta:
                    self.envio_paquetes(respuesta)
            except OSError:
                break

    def envio_paquetes(self, mensaje):
        # Maneja el envío de mensajes / paquetes
        print("envia {}".format(mensaje))
        self.socketD_cliente.send(bytes(mensaje, "utf8"))

    def close(self):
        self.envio_paquetes("Sale")

if __name__ == "__main__":
    client = Server_Client()
