import socket

ip = input ("Digite o IP ou Host: ")
porta = int(input("Digite a porta: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, porta))
banner = s.recv(1024)
print(banner)