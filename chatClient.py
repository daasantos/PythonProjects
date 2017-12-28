#!/usr/bin/env python3
# python3.5.3
import socket
import threading
import time

tLock = threading.Lock()
shutdown = False


def receiving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)  # Will throw an error when no data is available, breaking the while
                data = decode(data, "UTF-8")
                print(data)
        except:
            pass
        finally:
            tLock.release()


host, port = "127.0.0.1", 6666
server = ("127.0.0.1", 5555)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind((host, port))  # Takes a tuple!
except socket.error as serror:
    print("Bind failed: ".format(serror))
    raise SystemExit
s.setblocking(0)

rT = threading.Thread(target=receiving, args=("RecvThread", s))
rT.start()

alias = input("Username?\n")
message = input("{}:".format(alias))

while message != "q":
    if message != "":
        s.sendto("{}:{}".format(alias, message), server)
    tLock.acquire()
    message = input("{}:".format(alias))
    tLock.release()
    time.sleep(0.2)

shutdown = true
rT.join()
s.close()
raise SystemExit
