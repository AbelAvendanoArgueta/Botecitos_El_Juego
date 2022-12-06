from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from recursos.codigo.src_parametros_generales import conexiones
# from src_parametros_generales import conexiones

class Server_Host:
    def __init__(self):
        # Aqui inicializa la ejecucion de la clase cuando se le llama
        self.clientes = {}
        self.direcciones = {}
        self.inicia_serv()

    def inicia_serv(self):
        # Empieza la escucha de puertos del host
        servidor.listen(5)
        print("Esperando la conexión...")
        # comunicacion directa con recibe_hiloD_com
        acepta_hilo = Thread(target=self.aceptar_conexiones_entrantes)
        acepta_hilo.start()
        acepta_hilo.join()
        servidor.close()

    def aceptar_conexiones_entrantes(self):
        # Configura el manejo para las clientes entrantes
        num_clients = 0
        while True:
            cliente, direccion_cliente = servidor.accept()
            self.direcciones[cliente] = direccion_cliente
            print("%s:%s se ha conectado." % direccion_cliente)
            Thread(target=self.manejoD_cliente, args=(cliente,)).start()

    def manejoD_cliente(self, cliente):
        # Maneja una sola conexión de cliente.
        nombre = str(len(self.clientes) + 1)
        self.clientes[cliente] = nombre
        self.broadcast(nombre, bytes("Entra", "utf8"))

        while True:
            mensaje = cliente.recv(tamano_buffer)
            if mensaje != bytes("Sale", "utf8"):
                self.broadcast(nombre, mensaje)
            else:
                cliente.close()
                del self.clientes[cliente]
                print("%s:%s se ha desconectado." % self.direcciones[cliente])
                self.broadcast(nombre, bytes("Sale", "utf8"))
                del self.direcciones[cliente]
                break

    def broadcast(self, nombre, mensaje):
        # Transmite un mensaje a todos los clientes.
        for sock in self.clientes:
            sock.send(bytes(nombre + ",", "utf8") + mensaje)

if __name__ == "__main__":
    host = ''
    puerto = conexiones['puerto']
    tamano_buffer = conexiones['buffer']
    dirección = (host, puerto)
    servidor = socket(AF_INET, SOCK_STREAM)
    servidor.bind(dirección)
    server = Server_Host()
