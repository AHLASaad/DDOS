#!/usr/bin/python3
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',1234))
server_socket.listen()
while True:
	conn, addr = server_socket.accept()
	while True:
		data = conn.recv(1024)
		if not data:
			pass
		conn.sendall(data)
