#!/usr/bin/python3
import random
import socket

# Createe a datagram socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1',12000))
print("UDP Server is UP ...")

# Listen for incoming datagrams
while True:
	message, address = server_socket.recvfrom(1024)
	print(f'Client {address} send {message}')
