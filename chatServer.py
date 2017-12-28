#!/usr/bin/env python3
# python3.5.3
import socket
import time


def main():
    host, port, clients = "127.0.0.1", 5555, []

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.bind((host, port))  # Takes a tuple!
    except socket.error as serror:
        print("Bind failed: ".format(serror))
        raise SystemExit
    s.setblocking(0)
    quitting = False
    print("Server started.")

    while not quitting:
        try:
            data, addr = s.recvfrom(1024)
            if "Quit" in str(data):
                quitting = True
            if addr not in clients:
                clients.append(addr)
            print("{}:{}:{}".format(time.ctime(time.time()), str(addr), str(data)))
            for client in clients:
                s.sendto(data, client)
        except:
            pass
    s.close()
    raise SystemExit


if __name__ == "__main__":
    main()
