import socket

# Configuration
client_port = 5091  # Update port number to match the server
buffer_size = 1024  # Update buffer size
encoding = "utf-8"

server_ip = "127.0.0.1"  # Localhost


def initiate_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, client_port))

    while True:
        user_input = input("Type your message to send to the server (type 'Stop' to disconnect): ")
        message_length = len(user_input)
        length_str = str(message_length).encode(encoding)
        length_str += b" " * (buffer_size - len(length_str))  # Padding to match buffer size

        client_socket.send(length_str)
        client_socket.send(user_input.encode(encoding))

        if user_input == "Stop":
            final_reply = client_socket.recv(buffer_size).decode(encoding)
            print("Server's final reply:", final_reply)
            break
        else:
            server_reply = client_socket.recv(buffer_size).decode(encoding)
            print("Server reply:", server_reply)

    client_socket.close()


if __name__ == "__main__":
    initiate_client()
