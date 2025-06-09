import socket

# Configuration
server_port = 5060  # Update port number to avoid conflicts
buffer_size = 16
encoding = "utf-8"
disconnect_signal = "Stop"

host_ip = "127.0.0.1"  # Ensure this matches the client IP

# Server address setup
server_address = (host_ip, server_port)

# Create and configure the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    server_socket.bind(server_address)
    server_socket.listen()
    print("Server is ready to accept connections")

    while True:
        client_connection, client_address = server_socket.accept()
        print("Client connected from", client_address)
        connection_active = True

        while connection_active:
            length_info = client_connection.recv(buffer_size).decode(encoding)
            print("Received message length:", length_info)

            if length_info:
                message_length = int(length_info)
                received_message = client_connection.recv(message_length).decode(encoding)
                if received_message == disconnect_signal:
                    client_connection.send("Goodbye. It was a pleasure serving you.".encode(encoding))
                    print("Closing connection with", client_address)
                    connection_active = False
                else:
                    vowels = "aeiouAEIOU"
                    total_vowels = sum(1 for char in received_message if char in vowels)
                    if total_vowels == 0:
                        client_connection.send("Not enough vowels".encode(encoding))
                    elif total_vowels <= 2:
                        client_connection.send("Enough vowels".encode(encoding))
                    else:
                        client_connection.send("Too many vowels".encode(encoding))

        client_connection.close()

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    server_socket.close()
