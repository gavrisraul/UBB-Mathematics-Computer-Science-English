import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('172.30.112.93', 8888))
buff, addr = s.recvfrom(100)
print(buff)
s.sendto('Raul Gavris Mate Info Engleza Anul2')
