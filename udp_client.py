#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

udp_port = 3000
udp_ip = "localhost"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    print("Connected...")
    sock.connect((udp_ip, udp_port))
    while True:
        sock.sendto(input("Client UDP: ").encode(), ("", udp_port))
        message, addr = sock.recvfrom(1024)
        print(f"Server UDP: ", message.decode())
        if not message:
            break
except Exception as error:
    print("Error: ", error)
finally:
    sock.close()
