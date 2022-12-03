# !/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from src_parametros_generales import conexiones


class Server:
    def __init__(self):
        # Aqui inicializa la ejecucion de la clase cuando se le llama
        self.clients = {}
        self.addresses = {}
        self.inicia_serv()

    def inicia_serv(self):
        # Empieza la escucha de puertos del host
        servidor.listen(5)
        print("Esperando la conexión...")
        accept_thread = Thread(target=self.aceptar_conexiones_entrantes)
        accept_thread.start()
        accept_thread.join()
        servidor.close()

    def aceptar_conexiones_entrantes(self):
        # Configura el manejo para las clientes entrantes
        num_clients = 0
        while True:
            client, client_address = servidor.accept()
            self.addresses[client] = client_address
            print("%s:%s se ha conectado." % client_address)
            Thread(target=self.manejoD_cliente, args=(client,)).start()

    def manejoD_cliente(self, client):
        # Maneja una sola conexión de cliente.
        name = str(len(self.clients) + 1)
        self.clients[client] = name
        self.broadcast(name, bytes("Entra", "utf8"))

        while True:
            mensaje = client.recv(tamano_buffer)
            if mensaje != bytes("Sale", "utf8"):
                self.broadcast(name, mensaje)
            else:
                client.close()
                del self.clients[client]
                print("%s:%s se ha desconectado." % self.addresses[client])
                self.broadcast(name, bytes("Sale", "utf8"))
                del self.addresses[client]
                break

    def broadcast(self, name, mensaje):
        # Transmite un mensaje a todos los clientes.
        for sock in self.clients:
            sock.send(bytes(name + ",", "utf8") + mensaje)


if __name__ == "__main__":
    host = ''
    puerto = conexiones['puerto']
    tamano_buffer = conexiones['buffer']
    dirección = (host, puerto)

    servidor = socket(AF_INET, SOCK_STREAM)
    servidor.bind(dirección)

    server = Server()
