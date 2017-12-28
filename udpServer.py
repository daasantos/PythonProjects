#!/usr/bin/env python3
# python3.5.3
import socket


def main():
    host, port = "127.0.0.1", 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.bind((host, port))  # Takes a tuple!
    except socket.error as serror:
        print("Bind failed: ".format(serror))
        raise SystemExit

    print("Server has started.")
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        data = data.decode("UTF-8")
        print("{}: {}".format(str(addr), data))
        data = data.upper()
        print("Sending: ".format(data))
        s.sendto(data.encode("UTF-8"), addr)
    s.close()
    raise SystemExit


if __name__ == "__main__":
    main()
