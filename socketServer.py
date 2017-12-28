#!/usr/bin/env python3
# python3.5.3
import socket
# import threading


""" 
def handle_client_connection(client):
    while True:
        data = client.recv(1024).decode("UTF-8")
        if not data:
            break
        print("In: " + data)
        data = data.upper()
        print("Out: " + data)
        client.send(data.encode("UTF-8"))
    client.close() 
"""


def main():
    host, port = "127.0.0.1", 5555

    s = socket.socket()
    try:
        s.bind((host, port))  # Takes a tuple!
    except socket.error as serror:
        print("Bind failed: ".format(serror))
        raise SystemExit

    s.listen(1)  # Only 1 client
    c, addr = s.accept()
    print("Incoming connection from: {}".format(addr))

    while True:
        data = c.recv(1024).decode("UTF-8")
        if not data:
            break
        print("In: {}".format(data))
        data = data.upper()
        print("Out: {}".format(data))
        c.send(data.encode("UTF-8"))

        """
        client_thread = threading.Thread(target=handle_client_connection,args=(c,))
        client_thread.start()
        """

    raise SystemExit


if __name__ == "__main__":
    main()
