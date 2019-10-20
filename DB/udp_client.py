import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"Raul Gavris", ("172.30.112.93", 8888))

print(s.recvfrom(40))
