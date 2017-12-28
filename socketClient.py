#!/usr/bin/env python3
# python3.5.3
import socket


def main():
    host, port = "127.0.0.1", 6666

    s = socket.socket()
    s.connect((host, port))

    message = input("Out: ")
    while message != "q":
        s.send(message.encode("UTF-8"))
        data = s.recv(1024).decode("UTF-8")
        print("In: {}".format(data))
        message = input("Out: ")
    s.close()
    raise SystemExit


if __name__ == "__main__":
    main()
