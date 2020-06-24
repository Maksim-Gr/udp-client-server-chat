#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket


udp_port = 3000
udp_ip = ""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))


try:
    print("Waiting for connection...")

    while True:
        message, addr = sock.recvfrom(1024)
        print("Connected: ", addr)
        if not message:
            break
        print(f"Client UDP: ", message.decode())
        if message == "exit":
            break
        not sock.sendto(input("Server UDP:").encode(), addr)
    print("Connection closed")
except Exception as error:
    print("Error: ", error)
finally:
    sock.close()
