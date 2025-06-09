import socket

# Configuration
server_port = 5090  # Updated port number to avoid conflicts
buffer_size = 16  # Updated buffer size
encoding = "utf-8"
disconnect_signal = "Stop"

local_hostname = socket.gethostname()
local_ip = socket.gethostbyname(local_hostname)

server_address = (local_ip, server_port)

# Create and bind the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)

server_socket.listen()
print("Server is ready to accept connections")

while True:
    client_connection, client_address = server_socket.accept()
    print("Client connected from", client_address)
    is_active = True

    while is_active:
        length_info = client_connection.recv(buffer_size).decode(encoding)
        print("Received message length:", length_info)

        if length_info:
            length_info = int(length_info)
            received_message = client_connection.recv(length_info).decode(encoding)
            if received_message == disconnect_signal:
                client_connection.send("Goodbye. It was a pleasure serving you.".encode(encoding))
                print("Closing connection with", client_address)
                is_active = False
            else:
                print("Message received:", received_message)
                client_connection.send("Message received successfully".encode(encoding))

    client_connection.close()
