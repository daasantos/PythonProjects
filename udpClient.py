#!/usr/bin/env python3
# python3.5.3
import socket


def main():
    host, port = "127.0.0.1", 6666

    server = ("127.0.0.1", 5000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.bind((host, port))  # Takes a tuple!
    except socket.error as serror:
        print("Bind failed: ".format(serror))
        raise SystemExit

    message = input("Out: ")
    while message != "q":
        s.sendto(message.encode("UTF-8"), server)
        data, addr = s.recvfrom(1024)
        data = data.decode("UTF-8")
        print("In: ".format(data))
        message = input("Out: ")
    s.close()
    raise SystemExit


if __name__ == "__main__":
    main()
