import socket

# Configuration
client_port = 5060  # Update port number to match server changes
buffer_size = 16
encoding = "utf-8"

server_ip = "127.0.0.1"  # Ensure this matches the server IP

# Create and connect the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, client_port))

    connection_active = True
    while connection_active:
        user_message = input("Type your message to send to the server (type 'Stop' to disconnect): ")
        message_length = len(user_message)
        length_str = str(message_length).encode(encoding)
        length_str += b" " * (buffer_size - len(length_str))  # Padding to match buffer size

        client_socket.send(length_str)
        client_socket.send(user_message.encode(encoding))

        if user_message == "Stop":
            connection_active = False
            final_reply = client_socket.recv(buffer_size).decode(encoding)
            print("Server's final reply:", final_reply)
        else:
            server_reply = client_socket.recv(buffer_size).decode(encoding)
            print("Server reply:", server_reply)

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    client_socket.close()
