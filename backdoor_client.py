import socket

server = input("Where is server>:  ")
client_socket = socket.socket()
client_socket.connect((server, 8888))

request = input("\nShell>: ")
while request !="stop":
	client_socket.send(request.encode())
	response = client_socket.recv(1024)
	print(response.decode('utf-8'))
	request = input("\nShell>: ")
client_socket.close()