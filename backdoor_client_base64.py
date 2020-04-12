import socket
import base64

server = input("Hey, where is server?>:")
port = input("Input port:>")
client_socket = socket.socket()
client_socket.connect((server, int(port)))

request = input("\nShell>:")
while request !="stop":
	request = base64.b64encode(request.encode())
	client_socket.send(request)
	response = client_socket.recv(1024)
	response = response.decode('utf-8')
	response = base64.b64decode(response)
	print(response.decode())
	request = input("\nShell>:")
client_socket.close()