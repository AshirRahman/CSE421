import socket
import threading

# Configuration
server_port = 5091  # Update port number to avoid conflicts
buffer_size = 1024  # Update buffer size
encoding = "utf-8"
vowel_chars = "aeiouAEIOU"


def handle_client_connection(client_socket, client_address):
    print(f"Client connected from {client_address}")
    while True:
        try:
            length_info = client_socket.recv(buffer_size).decode(encoding)
            if not length_info:
                break
            message_length = int(length_info)
            received_message = client_socket.recv(message_length).decode(encoding)

            if received_message == "Stop":
                client_socket.send("Goodbye. It was a pleasure serving you.".encode(encoding))
                print(f"Closing connection with {client_address}")
                break
            else:
                vowel_count = sum(1 for char in received_message if char in vowel_chars)
                if vowel_count == 0:
                    response = "Not enough vowels"
                elif vowel_count <= 2:
                    response = "Enough vowels I guess"
                else:
                    response = "Too many vowels"

                client_socket.send(response.encode(encoding))
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    client_socket.close()


def start_server():
    local_ip = "127.0.0.1"  # Localhost
    server_address = (local_ip, server_port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(server_address)
    server_socket.listen()
    print("Server is ready to accept connections")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, client_address))
            client_thread.start()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
