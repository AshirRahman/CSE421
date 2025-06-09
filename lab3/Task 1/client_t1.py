import socket

# Configuration
client_port = 5090  # Update port number to avoid conflicts
buffer_size = 16
disconnect_message = "Stop"
encoding = "utf-8"
local_hostname = socket.gethostname()
local_ip = socket.gethostbyname(local_hostname)

# Server address setup
server_address = (local_ip, client_port)

# Create and connect the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)


def send_message(message):
    encoded_message = message.encode(encoding)
    message_length = len(encoded_message)
    length_str = str(message_length).encode(encoding)
    length_str += b" " * (buffer_size - len(length_str))

    client_socket.send(length_str)
    client_socket.send(encoded_message)

    response = client_socket.recv(2048).decode(encoding)
    print(response)


# Send client information and disconnect message
send_message(f"Client's IP address: {local_ip} and device name: {local_hostname}")
send_message(disconnect_message)

client_socket.close()
